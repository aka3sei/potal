import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .main-title { font-size: 24px; font-weight: bold; text-align: center; color: #1a365d; margin-bottom: 30px; }
    
    div.stButton > button, a[data-testid="stLinkButton"] {
        width: 100% !important;
        height: 70px !important;
        border-radius: 15px !important;
        font-size: 1.1rem !important;
        font-weight: bold !important;
        background-color: #ffffff !important;
        color: #1a365d !important;
        border: 2px solid #e2e8f0 !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
        margin-bottom: 12px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-decoration: none !important;
    }
    </style>
""", unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.markdown('<div class="main-title">🔒 営業支援システム</div>', unsafe_allow_html=True)
    password = st.text_input("アクセスパスワードを入力", type="password", key="pw_input")
    if st.button("ログイン", use_container_width=True):
        if password == "1234":
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.error("パスワードが正しくありません")
else:
    st.markdown('<div class="main-title">📱 業務アプリ一覧</div>', unsafe_allow_html=True)
    
    # ここに「最寄り駅」があることを確認してください
    st.link_button("🏙️ 暮らしの立地スコア診断", "https://bbmns2pc89m86nxhkvqnet.streamlit.app/")
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/")
    st.link_button("🏢 マンション予想AI", "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/")
    st.link_button("🛠️ 内装リフォーム見積", "https://reform-xblfcovcvgk83yhwkypqbu.streamlit.app/")
    st.link_button("💰 ローン診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")
    st.link_button("📈 営業進捗管理", "https://my-sales-app-aog993sltv8vseasajfwvr.streamlit.app/")

    st.write("---")
    if st.button("🚪 ログアウトして画面をロック"):
        st.session_state['logged_in'] = False
        st.rerun()
