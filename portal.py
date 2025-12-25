import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 上部余白の削除と中央揃え・アニメーション
st.markdown("""
    <style>
    /* ヘッダーと余計な余白を徹底的に削る */
    header[data-testid="stHeader"] { visibility: hidden; }
    .block-container {
        padding-top: 1rem !important; /* 標準の半分以下に設定 */
        padding-bottom: 0rem !important;
    }
    
    /* コンテンツ全体をさらに上に引き上げる */
    [data-testid="stVerticalBlock"] {
        gap: 0px !important;
        margin-top: -20px !important;
    }

    .stApp { display: flex; justify-content: center; }
    
    /* 入力欄とボタンの幅を280pxに固定 */
    [data-testid="stVerticalBlock"] > div {
        width: 280px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    /* タイトルの余白微調整 */
    .title-text {
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        color: #1a365d;
        margin-bottom: 10px !important;
        margin-top: 0px !important;
    }

    /* 巨大ボタンと強力な押し込みアニメーション */
    div.stButton > button {
        width: 100% !important;
        height: 72px !important;
        border-radius: 15px !important;
        font-size: 32px !important;
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
        display: block !important;
        margin: 0 auto 8px auto !important;
        transition: transform 0.05s ease !important;
    }

    /* 押し込みアニメーション */
    div.stButton > button:active {
        transform: scale(0.85) !important;
        background-color: #1a365d !important;
        color: #ffffff !important;
    }

    /* 削除ボタン専用 */
    div.stButton > button[kind="secondary"] {
        background-color: #e2e8f0 !important;
        height: 55px !important;
        font-size: 18px !important;
    }

    /* ログイン後のリストボタン */
    a[data-testid="stLinkButton"] {
        width: 100% !important; height: 65px !important;
        border-radius: 15px !important; font-size: 1.1rem !important;
        font-weight: bold !important; background-color: #ffffff !important;
        color: #1a365d !important; border: 2px solid #e2e8f0 !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        text-decoration: none !important; margin-bottom: 12px !important;
    }
    </style>
""", unsafe_allow_html=True)

# セッション状態の管理
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if 'temp_password' not in st.session_state:
    st.session_state['temp_password'] = ""

# --- 1. パスコード画面 ---
if not st.session_state['authenticated']:
    st.markdown('<div class="title-text">🔒 営業支援システム</div>', unsafe_allow_html=True)
    
    # パスワード入力欄
    st.text_input("アクセスパスワードを入力", value=st.session_state['temp_password'], type="password", label_visibility="collapsed")

    # 即時ログインロジック (4桁で即遷移)
    if len(st.session_state['temp_password']) >= 4:
        if st.session_state['temp_password'] == "1234":
            st.session_state['authenticated'] = True
            st.session_state['temp_password'] = ""
            st.rerun()
        else:
            st.error("パスコードが違います")
            st.session_state['temp_password'] = ""
            st.rerun()

    # 数字ボタン
    for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        if st.button(num, key=f"num_{num}"):
            st.session_state['temp_password'] += num
            st.rerun()

    if st.button("⬅︎ 一文字削除", key="del_key", type="secondary"):
        st.session_state['temp_password'] = st.session_state['temp_password'][:-1]
        st.rerun()

# --- 2. ログイン後：アプリ一覧 ---
else:
    st.markdown('<div class="title-text">📱 業務アプリ一覧</div>', unsafe_allow_html=True)
    
    st.link_button("🏙️ 暮らしのスコア診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/")
    st.link_button("🏢 マンション予想AI", "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/")
    st.link_button("📈 営業進捗管理", "https://my-sales-app-aog993sltv8vseasajfwvr.streamlit.app/")
    st.link_button("💰 ローン診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")

    st.write("---")
    if st.button("ログアウト", key="logout_btn", type="secondary"):
        st.session_state['authenticated'] = False
        st.rerun()
