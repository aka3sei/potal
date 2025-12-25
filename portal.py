import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: バランスの再構築
st.markdown("""
    <style>
    /* ヘッダー・余白の最小化 */
    header[data-testid="stHeader"] { visibility: hidden; }
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
    }
    
    /* コンテンツ幅固定と中央寄せ */
    [data-testid="stVerticalBlock"] > div {
        width: 280px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    /* タイトル */
    .title-text {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        color: #1a365d;
        margin-bottom: 10px !important;
    }

    /* 【修正】入力表示スペースの高さを広げる */
    div[data-testid="stTextInput"] {
        margin-bottom: 25px !important; /* ボタンとの間隔を広げてゆとりを持たせる */
    }
    div[data-testid="stTextInput"] input {
        height: 60px !important; /* 入力枠自体の高さを出して視認性アップ */
        font-size: 24px !important;
        text-align: center !important;
        border-radius: 12px !important;
    }

    /* 【修正】数字ボタン：高さを少し低く（85px → 72px） */
    div.stButton > button {
        width: 100% !important;
        height: 72px !important; 
        border-radius: 15px !important;
        font-size: 32px !important; 
        font-weight: bold !important;
        background-color: #f8fafc !important;
        color: #1a365d !important;
        border: 1px solid #cbd5e1 !important;
        display: block !important;
        margin: 0 auto 10px auto !important;
        transition: transform 0.05s ease !important;
    }

    /* 押し込みアニメーション */
    div.stButton > button:active {
        transform: scale(0.90) !important;
        background-color: #1a365d !important;
        color: #ffffff !important;
    }

    /* 修正ボタン */
    div.stButton > button[kind="secondary"] {
        background-color: #f1f5f9 !important;
        height: 60px !important;
        font-size: 18px !important;
    }

    /* ログイン後のリストボタン */
    a[data-testid="stLinkButton"] {
        width: 100% !important; height: 70px !important;
        border-radius: 15px !important; font-size: 1.1rem !important;
        font-weight: bold !important; background-color: #ffffff !important;
        color: #1a365d !important; border: 2px solid #f1f5f9 !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        text-decoration: none !important; margin-bottom: 15px !important;
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
    
    # 即時ログイン判定
    if len(st.session_state['temp_password']) >= 4:
        if st.session_state['temp_password'] == "1234":
            st.session_state['authenticated'] = True
            st.session_state['temp_password'] = ""
            st.rerun()
        else:
            st.error("パスコードが違います")
            st.session_state['temp_password'] = ""
            st.rerun()

    # 入力表示エリア（高さを出した設定）
    st.text_input("password_field", value=st.session_state['temp_password'], type="password", label_visibility="collapsed")

    # 数字ボタン (1-5, 0)
    for num in ["1", "2", "3", "4", "5", "0"]:
        if st.button(num, key=f"num_{num}"):
            st.session_state['temp_password'] += num
            st.rerun()

    # 修正ボタン
    if st.button("⬅︎ 修正", key="del_key", type="secondary"):
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
