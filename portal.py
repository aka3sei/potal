import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 装飾はせず、位置関係（横幅と下の余白）のみを維持
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    
    /* 上部余白 1.0rem */
    .block-container { padding-top: 1.0rem !important; }
    
    /* コンテンツ全体の基本幅（ボタンの幅） */
    [data-testid="stVerticalBlock"] > div {
        width: 280px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    /* 入力表示枠の横幅設定 */
    div[data-testid="stTextInput"] {
        width: 320px !important; 
        margin-left: -20px !important;
        /* 入力欄と数字1の間の余白 */
        margin-bottom: 25px !important; 
    }

    /* タイトル */
    .title-text {
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        color: #1a365d;
        margin-bottom: 20px !important;
    }

    /* 数字ボタンのデザイン */
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

    /* ボタン押し込み */
    div.stButton > button:active {
        transform: scale(0.92) !important;
        background-color: #1a365d !important;
        color: #ffffff !important;
    }

    /* 修正・ログアウトボタン */
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
    
    # 4桁即時ログイン
    if len(st.session_state['temp_password']) >= 4:
        if st.session_state['temp_password'] == "1234":
            st.session_state['authenticated'] = True
            st.session_state['temp_password'] = ""
            st.rerun()
        else:
            st.error("パスコードが違います")
            st.session_state['temp_password'] = ""
            st.rerun()

    # 入力表示エリア
    st.text_input("pass", value=st.session_state['temp_password'], type="password", label_visibility="collapsed")

    # 1〜5のボタン
    for num in ["1", "2", "3", "4", "5"]:
        if st.button(num, key=f"num_{num}"):
            st.session_state['temp_password'] += num
            st.rerun()

    # 削除ボタン
    if st.button("⬅︎ 一文字削除", key="del_key", type="secondary"):
        st.session_state['temp_password'] = st.session_state['temp_password'][:-1]
        st.rerun()

# --- 2. ログイン後：アプリ一覧 ---
else:
    st.markdown('<div class="title-text">📱 業務アプリ一覧</div>', unsafe_allow_html=True)
    st.write("")
    
    # アプリ一覧（内装アプリを追加）
    st.link_button("🏠 内装リフォームシミュレート", "https://reform-xblfcovcvgk83yhwkypqbu.streamlit.app/")
    st.link_button("🏙️ 暮らしのスコア診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/")
    st.link_button("🏢 マンション予想AI", "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/")
    st.link_button("📈 営業進捗管理", "https://my-sales-app-aog993sltv8vseasajfwvr.streamlit.app/")
    st.link_button("💰 ローン診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")

    st.write("---")
    if st.button("ログアウト", key="logout_btn", type="secondary"):
        st.session_state['authenticated'] = False
        st.rerun()
