import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 上部余白の極小化、中央揃え、巨大ボタン
st.markdown("""
    <style>
    /* ヘッダーと余白を徹底排除 */
    header[data-testid="stHeader"] { visibility: hidden; }
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 0rem !important;
    }
    
    /* コンテンツ全体を中央寄せ、幅固定 */
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
        margin-bottom: 5px !important;
    }

    /* ボタンデザイン：高さをさらに出し、押しやすさを追求 */
    div.stButton > button {
        width: 100% !important;
        height: 85px !important; /* 高さを85pxにアップ */
        border-radius: 18px !important;
        font-size: 36px !important; /* 数字をさらに巨大に */
        font-weight: bold !important;
        background-color: #f8fafc !important;
        color: #1a365d !important;
        border: 1px solid #cbd5e1 !important;
        display: block !important;
        margin: 0 auto 12px auto !important;
        transition: transform 0.05s ease !important;
    }

    /* 押し込みアニメーション：深く沈み、色が反転 */
    div.stButton > button:active {
        transform: scale(0.88) !important;
        background-color: #1a365d !important;
        color: #ffffff !important;
        border: none !important;
    }

    /* 削除ボタン：数字ボタンと差別化 */
    div.stButton > button[kind="secondary"] {
        background-color: #f1f5f9 !important;
        height: 65px !important;
        font-size: 20px !important;
        color: #64748b !important;
    }

    /* アプリ一覧リンクボタン */
    a[data-testid="stLinkButton"] {
        width: 100% !important; height: 75px !important;
        border-radius: 15px !important; font-size: 1.15rem !important;
        font-weight: bold !important; background-color: #ffffff !important;
        color: #1a365d !important; border: 2px solid #f1f5f9 !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        text-decoration: none !important; margin-bottom: 15px !important;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1) !important;
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
    
    # 4桁即時ログイン判定
    if len(st.session_state['temp_password']) >= 4:
        if st.session_state['temp_password'] == "1234":
            st.session_state['authenticated'] = True
            st.session_state['temp_password'] = ""
            st.rerun()
        else:
            st.error("パスコードが違います")
            st.session_state['temp_password'] = ""
            st.rerun()

    # 入力表示（ラベルなしでスッキリ）
    st.text_input("pass", value=st.session_state['temp_password'], type="password", label_visibility="collapsed")

    # 厳選された数字ボタン (1-5, 0)
    for num in ["1", "2", "3", "4", "5", "0"]:
        if st.button(num, key=f"num_{num}"):
            st.session_state['temp_password'] += num
            st.rerun()

    # 削除ボタン
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
