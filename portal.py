import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 入力欄の2重枠解消のみに集中
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .block-container { padding-top: 1.5rem !important; }
    
    /* コンテンツ幅固定 */
    [data-testid="stVerticalBlock"] > div {
        width: 280px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    /* タイトルの余白 */
    .title-text {
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        color: #1a365d;
        margin-bottom: 10px !important;
    }

    /* 【ここを修正】入力欄の2重枠を解消 */
    /* 1. 外側の枠線を完全に消す */
    div[data-testid="stTextInput"] > div {
        border: none !important;
        background-color: transparent !important;
        box-shadow: none !important;
        padding: 0 !important;
    }
    
    /* 2. 内側の入力エリアのみにボタンと合わせたデザインを適用 */
    div[data-testid="stTextInput"] input {
        height: 75px !important;
        font-size: 36px !important;
        text-align: center !important;
        border-radius: 18px !important;
        background-color: #f1f5f9 !important;
        border: 2px solid #cbd5e1 !important; /* ここが唯一の枠線になります */
        color: #1a365d !important;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.05) !important;
        outline: none !important;
    }

    /* --- 以下、変更なし --- */
    div.stButton > button {
        width: 100% !important;
        height: 75px !important; 
        border-radius: 18px !important;
        font-size: 34px !important; 
        font-weight: bold !important;
        background-color: #ffffff !important;
        color: #1a365d !important;
        border: 1px solid #cbd5e1 !important;
        display: block !important;
        margin: 0 auto 10px auto !important; 
        transition: transform 0.05s ease !important;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.08) !important;
    }

    div.stButton > button:active {
        transform: scale(0.92) !important;
        background-color: #1a365d !important;
        color: #ffffff !important;
    }

    div.stButton > button[kind="secondary"] {
        background-color: #f1f5f9 !important;
        height: 60px !important;
        font-size: 18px !important;
    }
    </style>
""", unsafe_allow_html=True)

# セッション状態
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if 'temp_password' not in st.session_state:
    st.session_state['temp_password'] = ""

# --- 1. パスコード画面 ---
if not st.session_state['authenticated']:
    st.markdown('<div class="title-text">🔒 営業支援システム</div>', unsafe_allow_html=True)
    
    if len(st.session_state['temp_password']) >= 4:
        if st.session_state['temp_password'] == "1234":
            st.session_state['authenticated'] = True
            st.session_state['temp_password'] = ""
            st.rerun()
        else:
            st.error("パスコードが違います")
            st.session_state['temp_password'] = ""
            st.rerun()

    st.text_input("pass_input", value=st.session_state['temp_password'], type="password", label_visibility="collapsed")

    for num in ["1", "2", "3", "4", "5"]:
        if st.button(num, key=f"num_{num}"):
            st.session_state['temp_password'] += num
            st.rerun()

    if st.button("⬅︎ 一文字削除", key="del_key", type="secondary"):
        st.session_state['temp_password'] = st.session_state['temp_password'][:-1]
        st.rerun()

# --- 2. ログイン後：アプリ一覧 ---
else:
    st.markdown('<div class="title-text">📱 業務アプリ一覧</div>', unsafe_allow_html=True)
    st.write("")
    st.link_button("🏙️ 暮らしのスコア診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/")
    st.link_button("🏢 マンション予想AI", "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/")
    st.link_button("📈 営業進捗管理", "https://my-sales-app-aog993sltv8vseasajfwvr.streamlit.app/")
    st.link_button("💰 ローン診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")

    st.write("---")
    if st.button("ログアウト", key="logout_btn", type="secondary"):
        st.session_state['authenticated'] = False
        st.rerun()
