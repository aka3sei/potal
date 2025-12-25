import streamlit as st
from streamlit_js_eval import get_geolocation
from geopy.distance import geodesic
import requests
import pandas as pd

# 1. ページ構成の基本設定
st.set_page_config(page_title="営業支援ポータル", layout="centered")

# デザイン（CSS）
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .main-title { font-size: 24px; font-weight: bold; text-align: center; color: #1a365d; margin-bottom: 20px; }
    /* メニューボタンのデザイン */
    div.stButton > button {
        width: 100%; height: 70px; border-radius: 15px;
        font-size: 1.1rem !important; font-weight: bold !important;
        background-color: #ffffff !important; color: #1a365d !important;
        border: 2px solid #e2e8f0 !important; margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 共通：状態管理 ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if 'page' not in st.session_state:
    st.session_state['page'] = 'menu'

# --- アプリ機能1：暮らしのスコア診断 ---
def score_app():
    st.button("🔙 ポータルに戻る", on_click=lambda: st.session_state.update({"page": "menu"}))
    st.title("🏙️ 暮らしのスコア診断")
    
    loc = get_geolocation()
    if loc:
        lat, lon = loc['coords']['latitude'], loc['coords']['longitude']
        st.success(f"現在地を取得しました: {lat}, {lon}")
        # ここに以前作成した「暮らしのスコア」のロジックを配置します
        # ... (データ取得・計算処理) ...
        st.write("※スコア診断機能がこの中で動作します")
    else:
        st.info("位置情報を取得中です...")

# --- アプリ機能2：マンション予想（枠組み） ---
def mansion_app():
    st.button("🔙 ポータルに戻る", on_click=lambda: st.session_state.update({"page": "menu"}))
    st.title("🏢 マンション予想AI")
    st.write("物件情報を入力してください。")
    # ここにマンション予想アプリのコードを移植します

# --- アプリ機能3：営業進捗（枠組み） ---
def sales_app():
    st.button("🔙 ポータルに戻る", on_click=lambda: st.session_state.update({"page": "menu"}))
    st.title("📈 営業進捗管理")
    st.write("本日の進捗を入力します。")

# --- メインロジック ---
if not st.session_state['authenticated']:
    # 1枚目：ロック画面
    st.markdown('<div class="main-title">🔒 営業支援システム</div>', unsafe_allow_html=True)
    password = st.text_input("パスワード", type="password")
    if st.button("ログイン"):
        if password == "1234":
            st.session_state['authenticated'] = True
            st.rerun()
        else:
            st.error("不一致")
else:
    # 2枚目：アプリ選択 or 各アプリ画面
    if st.session_state['page'] == 'menu':
        st.markdown('<div class="main-title">📱 業務アプリ一覧</div>', unsafe_allow_html=True)
        
        # URLへ飛ばすのではなく、session_stateを書き換えて同じ画面内で切り替える
        if st.button("🏙️ 暮らしのスコア診断"):
            st.session_state['page'] = 'score'
            st.rerun()
            
        if st.button("🏢 マンション予想AI"):
            st.session_state['page'] = 'mansion'
            st.rerun()

        if st.button("📈 営業進捗管理"):
            st.session_state['page'] = 'sales'
            st.rerun()

        st.write("---")
        if st.button("ログアウト", type="secondary"):
            st.session_state['authenticated'] = False
            st.rerun()
            
    elif st.session_state['page'] == 'score':
        score_app()
    elif st.session_state['page'] == 'mansion':
        mansion_app()
    elif st.session_state['page'] == 'sales':
        sales_app()
