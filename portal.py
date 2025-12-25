import streamlit as st
from streamlit_js_eval import get_geolocation
from geopy.distance import geodesic
import requests
import pandas as pd

# 1. ページ設定
st.set_page_config(page_title="営業支援ポータル", layout="centered")

# --- CSS設定（デザイン） ---
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .main-title { font-size: 24px; font-weight: bold; text-align: center; color: #1a365d; margin-bottom: 30px; }
    /* メニューボタンのデザイン */
    div.stButton > button {
        width: 100%; height: 80px; border-radius: 15px;
        font-size: 1.2rem !important; font-weight: bold !important;
        background-color: #ffffff !important; color: #1a365d !important;
        border: 2px solid #e2e8f0 !important; box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
        margin-bottom: 15px;
    }
    .score-box { background-color: #f0f4f8; padding: 20px; border-radius: 20px; text-align: center; border: 2px solid #1a365d; }
    .score-number { font-size: 3.5rem; font-weight: bold; color: #1a365d; line-height: 1; }
    </style>
""", unsafe_allow_html=True)

# --- 状態管理 (Session State) ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'page' not in st.session_state: st.session_state.page = "menu"

# --- 機能：暮らしのスコア診断 (合体) ---
def run_score_app():
    if st.button("🔙 ポータルに戻る"):
        st.session_state.page = "menu"
        st.rerun()
    
    st.subheader("🏙️ 暮らしの立地スコア")
    loc = get_geolocation()
    if loc:
        lat, lon = loc['coords']['latitude'], loc['coords']['longitude']
        # --- データ取得ロジック ---
        overpass_url = "https://overpass-api.de/api/interpreter"
        query = f"""[out:json][timeout:30];(
          node["amenity"~"school|kindergarten|hospital|clinic|post_office|bank"](around:1200,{lat},{lon});
          node["shop"~"supermarket|convenience|drugstore"](around:1200,{lat},{lon});
          node["leisure"="park"](around:1200,{lat},{lon});
          way["amenity"~"school|kindergarten|hospital|clinic|post_office|bank"](around:1200,{lat},{lon});
          way["shop"~"supermarket|convenience|drugstore"](around:1200,{lat},{lon});
          way["leisure"="park"](around:1200,{lat},{lon});
        );out center;"""
        try:
            res = requests.get(overpass_url, params={'data': query}, timeout=15)
            data = res.json()
            facilities = []
            for el in data.get('elements', []):
                tags = el.get('tags', {})
                name = tags.get('name') or tags.get('brand') or "施設"
                f_lat = el.get('lat') or el.get('center', {}).get('lat')
                f_lon = el.get('lon') or el.get('center', {}).get('lon')
                dist = geodesic((lat, lon), (f_lat, f_lon)).meters
                if dist > 1200: continue
                
                amenity = tags.get('amenity', '')
                if amenity in ['post_office', 'bank']: cat, cid = "📮 郵便局", "post"
                elif tags.get('leisure') == 'park': cat, cid = "🌳 公園", "park"
                elif amenity in ['school', 'kindergarten']: cat, cid = "🏫 学校", "school"
                elif amenity in ['hospital', 'clinic']: cat, cid = "🏥 病院", "hospital"
                elif tags.get('shop') in ['supermarket', 'convenience']: cat, cid = "🛒 買物", "shop"
                else: continue
                
                facilities.append({"施設名": name, "種別": cat, "距離": f"約{int(dist)}m", "cid": cid})
            
            df = pd.DataFrame(facilities).drop_duplicates(subset="施設名")
            if not df.empty:
                score = min(55 + (len(df) * 0.8), 99)
                st.markdown(f'<div class="score-box"><p style="margin:0;">実測スコア</p><p class="score-number">{int(score)}</p></div>', unsafe_allow_html=True)
                st.table(df[["施設名", "種別", "距離"]])
            st.map(data={'lat': [lat], 'lon': [lon]})
        except:
            st.error("データ取得に失敗しました。")
    else:
        st.info("⌛ 位置情報を取得中です...")

# --- メインロジック ---
if not st.session_state.auth:
    st.markdown('<div class="main-title">🔒 営業支援システム</div>', unsafe_allow_html=True)
    pw = st.text_input("パスワード", type="password")
    if st.button("ログイン"):
        if pw == "1234":
            st.session_state.auth = True
            st.rerun()
        else: st.error("不一致")
else:
    if st.session_state.page == "menu":
        st.markdown('<div class="main-title">📱 業務アプリ一覧</div>', unsafe_allow_html=True)
        if st.button("🏙️ 暮らしのスコア診断"):
            st.session_state.page = "score"
            st.rerun()
        
        # 他のアプリ用ボタン（まだ合体していないので案内のみ）
        if st.button("🏢 マンション予想AI (準備中)"): st.warning("コード合体が必要です")
        if st.button("📈 営業進捗管理 (準備中)"): st.warning("コード合体が必要です")
        
        st.write("---")
        if st.button("ログアウト"):
            st.session_state.auth = False
            st.rerun()

    elif st.session_state.page == "score":
        run_score_app()
