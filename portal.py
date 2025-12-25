import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 入力枠とボタンのサイズを完全に一致させる
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .main-title { font-size: 24px; font-weight: bold; text-align: center; color: #1a365d; margin-bottom: 20px; }
    
    /* 入力欄とボタンの横幅を280pxに固定して中央寄せ */
    div[data-testid="stTextInput"], div.stButton {
        max-width: 280px;
        margin: 0 auto !important;
    }

    /* 入力欄の下の余白を調整 */
    div[data-testid="stTextInput"] {
        margin-bottom: 15px !important;
    }

    /* ボタンのデザイン：入力枠と同じ幅・丸み・高さを設定 */
    div.stButton > button[kind="primary"] {
        width: 100% !important;   /* 親要素（280px）に対して100% */
        height: 60px !important;
        border-radius: 8px !important;
        font-size: 24px !important;
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
    }

    /* ログイン後のリストボタン */
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
    st.markdown('<div class="main-title">🔒 営業支援システム</div>', unsafe_allow_html=True)
    
    # 入力欄
    password = st.text_input("アクセスパスワードを入力", value=st.session_state['temp_password'], type="password")

    # 入力欄と全く同じサイズの「1」ボタン
    if st.button("1", key="num_1", type="primary"):
        st.session_state['temp_password'] += "1"
        st.rerun()

    st.write("") # スペース
    
    # ログイン実行ボタン
    if st.button("ログイン", type="secondary"):
        if password == "1234":
            st.session_state['authenticated'] = True
            st.rerun()
        else:
            st.error("パスワードが正しくありません")
            st.session_state['temp_password'] = ""

# --- 2. 業務アプリ一覧画面 ---
else:
    st.markdown('<div class="main-title">📱 業務アプリ一覧</div>', unsafe_allow_html=True)
    st.link_button("🏙️ 暮らしのスコア診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/")
    st.link_button("🏢 マンション予想AI", "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/")
    st.link_button("📈 営業進捗管理", "https://my-sales-app-aog993sltv8vseasajfwvr.streamlit.app/")
    st.link_button("💰 ローン診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")

    st.write("---")
    if st.button("ログアウト", type="secondary"):
        st.session_state['authenticated'] = False
        st.session_state['temp_password'] = ""
        st.rerun()
