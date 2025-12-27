import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS設定: デザインの維持
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .block-container { padding-top: 1.0rem !important; }
    
    [data-testid="stVerticalBlock"] > div {
        width: 280px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    div[data-testid="stTextInput"] {
        width: 320px !important; 
        margin-left: -20px !important;
        margin-bottom: 25px !important; 
    }

    .title-text {
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        color: #1a365d;
        margin-bottom: 20px !important;
    }

    /* リンクボタンのスタイル */
    .stLinkButton a {
        width: 100% !important;
        height: 75px !important; 
        border-radius: 18px !important;
        font-size: 24px !important; /* 文字サイズを微調整 */
        font-weight: bold !important;
        background-color: #ffffff !important;
        color: #1a365d !important;
        border: 1px solid #cbd5e1 !important;
        display: flex !important;
        align-items: center;
        justify-content: center;
        text-decoration: none !important;
        margin-bottom: 10px !important; 
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.08) !important;
    }

    .stLinkButton a:active {
        transform: scale(0.95) !important;
        background-color: #1a365d !important;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

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

    st.text_input("pass", value=st.session_state['temp_password'], type="password", label_visibility="collapsed")

    # 数字ボタンの配置
    cols = st.columns(3)
    for i, num in enumerate(["1", "2", "3", "4", "5"]):
        with cols[i % 3]:
            if st.button(num, key=f"num_{num}"):
                st.session_state['temp_password'] += num
                st.rerun()

    if st.button("⬅︎ 一文字削除", key="del_key"):
        st.session_state['temp_password'] = st.session_state['temp_password'][:-1]
        st.rerun()

# --- 2. ログイン後：アプリ一覧 ---
else:
    st.markdown('<div class="title-text">📱 業務アプリ一覧</div>', unsafe_allow_html=True)
    
    # リンクボタンを確実に表示させる
    st.link_button("🛡️ ハザードマップ", "https://hazardmap-ej92obhxl7cfrntxy7xtqj.streamlit.app/")
    st.link_button("⚖️ 賃貸 VS 購入", "https://taxfee-pfwmbwlcuvsftgfpxzpbgh.streamlit.app/")
    st.link_button("🏠 内装リフォーム", "https://reform-xblfcovcvgk83yhwkypqbu.streamlit.app/")
    st.link_button("🏙️ 立地スコア", "https://bbmns2pc89m86nxhkvqnet.streamlit.app/")
    st.link_button("🚉 周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/")
    st.link_button("🏢 マンション予想AI", "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/")
    st.link_button("📈 営業進捗管理", "https://my-sales-app-aog993sltv8vseasajfwvr.streamlit.app/")
    st.link_button("💰 ローン診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")

    st.write("---")
    if st.button("ログアウト", key="logout_btn"):
        st.session_state['authenticated'] = False
        st.rerun()
