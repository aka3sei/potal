import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSSでボタンを大きく、アプリ風に整える
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .main-title { font-size: 24px; font-weight: bold; text-align: center; color: #1a365d; margin-bottom: 30px; }
    /* ボタンのデザインを統一 */
    div.stButton > button, a[data-testid="stLinkButton"] {
        width: 100% !important;
        height: 80px !important;
        border-radius: 15px !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        background-color: #ffffff !important;
        color: #1a365d !important;
        border: 2px solid #e2e8f0 !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
        margin-bottom: 10px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-decoration: none !important;
    }
    div.stButton > button:active {
        background-color: #edf2f7 !important;
        transform: scale(0.98);
    }
    </style>
""", unsafe_allow_html=True)

# 1. パスワード認証の変数名を 'auth' に統一
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.markdown('<div class="main-title">🔒 営業支援システム</div>', unsafe_allow_html=True)
    password = st.text_input("アクセスパスワードを入力", type="password")
    if st.button("ログイン"):
        if password == "1234":
            st.session_state['auth'] = True
            st.rerun()
        else:
            st.error("パスワードが正しくありません")
else:
    # 2. アプリリスト
    st.markdown('<div class="main-title">📱 業務アプリ一覧</div>', unsafe_allow_html=True)
    
    # 指定の順番に並び替え
    st.link_button("🏙️ 暮らしの立地スコア診断", "https://bbmns2pc89m86nxhkvqnet.streamlit.app/")
    st.link_button("🏢 マンション予想AI", "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/")
    st.link_button("💰 ローン診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")
    st.link_button("📈 営業進捗管理", "https://my-sales-app-aog993sltv8vseasajfwvr.streamlit.app/")

    st.write("---")
    # ログアウトボタンで 'auth' を False に戻す
    if st.button("ログアウト", type="secondary"):
        st.session_state['auth'] = False
        st.rerun()
