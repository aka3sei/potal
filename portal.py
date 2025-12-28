import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS設定: デザインの維持
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .block-container { padding-top: 1.0rem !important; }
    
    /* 入力エリア全体の幅調整 */
    [data-testid="stVerticalBlock"] > div {
        width: 300px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    /* パスワード入力欄（幅を半分にする） */
    div[data-testid="stTextInput"] {
        width: 150px !important; 
        margin: 0 auto 20px auto !important; 
    }
    div[data-testid="stTextInput"] input {
        text-align: center;
        font-size: 20px;
    }

    .title-text {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        color: #1a365d;
        margin-bottom: 20px !important;
    }

    /* テンキー風ボタンのスタイル */
    div.stButton > button {
        width: 100% !important;
        height: 60px !important; 
        border-radius: 12px !important;
        font-size: 24px !important; 
        font-weight: bold !important;
        background-color: #ffffff !important;
        color: #1a365d !important;
        border: 1px solid #cbd5e1 !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05) !important;
    }

    div.stButton > button:active {
        transform: scale(0.92) !important;
        background-color: #1a365d !important;
        color: #ffffff !important;
    }

    /* 削除ボタン（記号）用の色調整 */
    div[data-testid="column"]:last-child button {
        background-color: #f1f5f9 !important;
        font-size: 20px !important;
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
    
    # 認証ロジック
    if len(st.session_state['temp_password']) >= 4:
        if st.session_state['temp_password'] == "1234":
            st.session_state['authenticated'] = True
            st.session_state['temp_password'] = ""
            st.rerun()
        else:
            st.error("Error")
            st.session_state['temp_password'] = ""
            st.rerun()

    # パスワード入力欄（幅半分・中央寄せ）
    st.text_input("pass", value=st.session_state['temp_password'], type="password", label_visibility="collapsed")

    # 1 2 3 4 5 と 削除(⌫) を横に並べる
    # スマホ画面を考慮し、3つずつの2段構成が最も押しやすいため調整
    col_group1 = st.columns(3)
    with col_group1[0]:
        if st.button("1"):
            st.session_state['temp_password'] += "1"
            st.rerun()
    with col_group1[1]:
        if st.button("2"):
            st.session_state['temp_password'] += "2"
            st.rerun()
    with col_group1[2]:
        if st.button("3"):
            st.session_state['temp_password'] += "3"
            st.rerun()

    col_group2 = st.columns(3)
    with col_group2[0]:
        if st.button("4"):
            st.session_state['temp_password'] += "4"
            st.rerun()
    with col_group2[1]:
        if st.button("5"):
            st.session_state['temp_password'] += "5"
            st.rerun()
    with col_group2[2]:
        if st.button("⌫"):
            st.session_state['temp_password'] = st.session_state['temp_password'][:-1]
            st.rerun()

# --- 2. ログイン後：アプリ一覧 ---
else:
    st.markdown('<div class="title-text">📱 業務アプリ一覧</div>', unsafe_allow_html=True)
    
    # 最新のURLリンク集
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/")
    st.link_button("🏙️ 立地スコア", "https://bbmns2pc89m86nxhkvqnet.streamlit.app/")
    st.link_button("🛡️ ハザードマップ", "https://hazardmap-ej92obhxl7cfrntxy7xtqj.streamlit.app/")
    st.link_button("🏫 東京 教育環境完全ガイド", "https://qmkp7yf2na9mcxrggjayft.streamlit.app/")
    st.link_button("🏢 マンション予想AI", "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/") 
    st.link_button("⚖️ 賃貸 VS 購入", "https://taxfee-pfwmbwlcuvsftgfpxzpbgh.streamlit.app/")
    st.link_button("💰 ローン診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")
    st.link_button("🏠 内装リフォーム", "https://reform-xblfcovcvgk83yhwkypqbu.streamlit.app/")
    st.link_button("📈 営業進捗管理", "https://my-sales-app-aog993sltv8vseasajfwvr.streamlit.app/")
    

    st.write("---")
    if st.button("ログアウト", key="logout_btn"):
        st.session_state['authenticated'] = False
        st.rerun()


