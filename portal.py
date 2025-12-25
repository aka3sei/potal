import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 横幅280pxで入力欄とボタンを完全に一致させ、中央に固定する
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    
    /* 1. 【中央揃えと幅の固定】入力欄とボタンを包むエリアを280pxに固定 */
    .stTextInput, .stButton {
        width: 280px !important;
        margin: 0 auto !important;
    }

    /* 2. 【入力欄】幅100%（＝280px） */
    div[data-testid="stTextInput"] > div {
        width: 100% !important;
    }

    /* 3. 【巨大ボタン】幅100%（＝280px）で高さを出し、中央に配置 */
    div.stButton > button {
        width: 100% !important;  /* 親要素280pxいっぱいに広げる */
        height: 70px !important; /* ボタンの高さを強調 */
        border-radius: 10px !important;
        font-size: 30px !important; /* 数字を巨大に */
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
        display: block !important;
        margin: 0 auto !important;
    }

    /* ログイン後のリストデザイン（崩さないよう維持） */
    a[data-testid="stLinkButton"] {
        width: 100% !important; height: 65px !important;
        border-radius: 12px !important; font-size: 1.1rem !important;
        font-weight: bold !important; background-color: #ffffff !important;
        color: #1a365d !important; border: 2px solid #e2e8f0 !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        text-decoration: none !important; margin-bottom: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# セッション状態
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if 'temp_password' not in st.session_state:
    st.session_state['temp_password'] = ""

# --- 1. パスワード認証画面 ---
if not st.session_state['authenticated']:
    st.markdown('<h2 style="text-align:center;">🔒 営業支援システム</h2>', unsafe_allow_html=True)
    
    # 中央に配置された280pxの入力欄
    password = st.text_input("アクセスパスワードを入力", value=st.session_state['temp_password'], type="password")

    # 入力欄と全く同じ幅の「1」ボタン
    if st.button("1", key="num_1"):
        st.session_state['temp_password'] += "1"
        st.rerun()

    st.write("") 
    
    # ログインボタン
    if st.button("ログイン", key="login_exec"):
        if password == "1234":
            st.session_state['authenticated'] = True
            st.rerun()
        else:
            st.error("パスワードが正しくありません")
            st.session_state['temp_password'] = ""

# --- 2. 業務アプリ一覧画面 ---
else:
    st.markdown('<h2 style="text-align:center;">📱 業務アプリ一覧</h2>', unsafe_allow_html=True)
    st.link_button("🏙️ 暮らしのスコア診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/")
    st.link_button("🏢 マンション予想AI", "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/")
    st.link_button("📈 営業進捗管理", "https://my-sales-app-aog993sltv8vseasajfwvr.streamlit.app/")
    st.link_button("💰 ローン診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")

    st.write("---")
    if st.button("ログアウト", key="logout"):
        st.session_state['authenticated'] = False
        st.session_state['temp_password'] = ""
        st.rerun()
