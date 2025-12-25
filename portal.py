import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 入力欄の微調整に集中
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .block-container {
        padding-top: 2rem !important;
    }
    
    /* 全体を280pxで中央固定 */
    [data-testid="stVerticalBlock"] > div {
        width: 280px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    .title-text {
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        color: #1a365d;
        margin-bottom: 20px !important;
    }

    /* 【再調整】入力表示スペース：ボタンと質感を合わせる */
    div[data-testid="stTextInput"] {
        margin-bottom: 35px !important;
    }
    div[data-testid="stTextInput"] input {
        height: 75px !important; /* ボタンと同じ高さに設定 */
        font-size: 36px !important;
        text-align: center !important;
        border-radius: 18px !important;
        background-color: #f1f5f9 !important; /* ボタンより少しだけトーンを落として「入力欄」であることを示す */
        border: 2px solid #cbd5e1 !important; /* 枠線を少し強調して「枠」感を出す */
        color: #1a365d !important;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.05) !important; /* 内側に影を入れ、凹んでいる表現 */
    }

    /* 数字ボタン：1〜5のみ */
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
        margin: 0 auto 12px auto !important; 
        transition: transform 0.05s ease !important;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1) !important;
    }

    /* 押し込みアニメーション */
    div.stButton > button:active {
        transform: scale(0.92) !important;
        background-color: #1a365d !important;
        color: #ffffff !important;
    }

    /* 削除ボタン */
    div.stButton > button[kind="secondary"] {
        background-color: #f1f5f9 !important;
        height: 60px !important;
        font-size: 18px !important;
        margin-top: 15px !important;
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

    # パスワード入力表示（label_visibility="collapsed"で余計な余白を消去）
    st.text_input("pw", value=st.session_state['temp_password'], type="password", label_visibility="collapsed")

    # 1〜5までのボタン
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
    
    st.link_button("🏙️ 暮らしのスコア診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/")
    st.link_button("🏢 マンション予想AI", "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/")
    st.link_button("📈 営業進捗管理", "https://my-sales-app-aog993sltv8vseasajfwvr.streamlit.app/")
    st.link_button("💰 ローン診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")

    st.write("---")
    if st.button("ログアウト", key="logout_btn", type="secondary"):
        st.session_state['authenticated'] = False
        st.rerun()
