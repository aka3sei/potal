import streamlit as st
from streamlit_js_eval import get_geolocation
from geopy.distance import geodesic
import requests
import pandas as pd

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: ボタンのデザインとスコアボックス
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .main-title { font-size: 24px; font-weight: bold; text-align: center; color: #1a365d; margin-bottom: 30px; }
    .score-box { background-color: #f0f4f8; padding: 20px; border-radius: 20px; text-align: center; border: 2px solid #1a365d; }
    .score-number { font-size: 3.5rem; font-weight: bold; color: #1a365d; line-height: 1; margin-bottom: 10px; }
    .score-details { font-size: 0.85rem; color: #2c5282; font-weight: bold; }
    div.stButton > button { width: 100%; border-radius: 15px; height: 60px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- 機能: 暮らしのスコア診断用ロジック ---
def get_nearby_facilities_with_dist(lat, lon):
    overpass_url = "https://overpass-api.de/api/interpreter"
    overpass_query = f"""[out:json][timeout:30];(
      node["amenity"~"school|kindergarten|hospital|clinic|doctors|post_office|bank"](around:1200,{lat},{lon});
      way["amenity"~"school|kindergarten|hospital|clinic|doctors|post_office|bank"](around:1200,{lat},{lon});
      node["shop"~"supermarket|convenience|drugstore"](around:1200,{lat},{lon});
      way["shop"~"supermarket|convenience|drugstore"](around:1200,{lat},{lon});
      node["leisure"="park"](around:1200,{lat},{lon});
      way["leisure"="park"](around:1200,{lat},{lon});
    );out center;"""
    try:
        response = requests.get(overpass_url, params={'data': overpass_query}, timeout=20)
        data = response.json()
    except: return pd.DataFrame()
    
    current_pos, facilities = (lat, lon), []
    if data and 'elements' in data:
        for element in data['elements']:
            tags = element.get('tags', {})
            name = tags.get('name') or tags.get('brand') or tags.get('operator')
            f_lat = element.get('lat') or element.get('center', {}).get('lat')
            f_lon = element.get('lon') or element.get('center', {}).get('lon')
            if not f_lat or not f_lon: continue
            dist_m = geodesic(current_pos, (f_lat, f_lon)).meters
            if dist_m > 1200: continue
            
            amenity, shop, leisure = tags.get('amenity', ''), tags.get('shop', ''), tags.get('leisure', '')
            if amenity in ['post_office', 'bank']: cat, cid = "📮 郵便局", "post"
            elif leisure == 'park': cat, cid = "🌳 公園", "park"
            elif amenity in ['school', 'kindergarten']: cat, cid = "🏫 学校", "school"
            elif amenity in ['hospital', 'clinic']: cat, cid = "🏥 病院", "hospital"
            elif shop in ['supermarket', 'convenience']: cat, cid = "🛒 買物", "shop"
            else: continue
            
            facilities.append({"施設名": name or "近隣施設", "種別": cat, "距離": f"約{int(dist_m)}m", "dist_raw": dist_m, "cat_id": cid})
    return pd.DataFrame(facilities).sort_values("dist_raw").drop_duplicates(subset="施設名") if facilities else pd.DataFrame()

# --- 状態管理 ---
if 'authenticated' not in st.session_state: st.session_state['authenticated'] = False
if 'page' not in st.session_state: st.session_state['page'] = "menu"

# --- 画面表示 ---
if not st.session_state['authenticated']:
    st.markdown('<div class="main-title">🔒 営業支援システム</div>', unsafe_allow_html=True)
    if st.text_input("パスワード", type="password") == "1234":
        if st.button("ログイン"):
            st.session_state['authenticated'] = True
            st.rerun()
else:
    if st.session_state['page'] == "menu":
        st.markdown('<div class="main-title">📱 業務アプリ一覧</div>', unsafe_allow_html=True)
        if st.button("🏙️ 暮らしのスコア診断"):
            st.session_state['page'] = "score"
            st.rerun()
        st.info("※他アプリも順次合体可能です")
        if st.button("ログアウト"):
            st.session_state['authenticated'] = False
            st.rerun()

    elif st.session_state['page'] == "score":
        if st.button("🔙 メニューに戻る"):
            st.session_state['page'] = "menu"
            st.rerun()
        
        st.subheader("🏙️ 暮らしのスコア診断")
        loc = get_geolocation()
        if loc:
            lat, lon = loc['coords']['latitude'], loc['coords']['longitude']
            df = get_nearby_facilities_with_dist(lat, lon)
            if not df.empty:
                counts = {cid: len(df[df['cat_id'] == cid]) for cid in ['school', 'hospital', 'shop', 'post', 'park']}
                score = min(55 + (len(df) * 0.8), 99)
                st.markdown(f"""<div class="score-box"><p class="score-number">{int(score)}</p>
                    <p class="score-details">🏫:{counts['school']} 🏥:{counts['hospital']} 🛒:{counts['shop']} 📮:{counts['post']} 🌳:{counts['park']}</p></div>""", unsafe_allow_html=True)
                st.table(df[["施設名", "種別", "距離"]])
            st.map(data={'lat': [lat], 'lon': [lon]})
        else:
            st.warning("位置情報を取得してください")
