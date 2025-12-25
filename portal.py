import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 枠のサイズと中央揃えを死守
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .main-title { font-size: 24px; font-weight: bold; text-align: center; color: #1a365d; margin-bottom: 20px; }
    
    /* 入力欄とボタンの「箱」を280pxに固定して中央寄せを絶対維持 */
    div[data-testid="column"], 
    div[data-testid="stVerticalBlock"] > div:has(div[data-testid="stTextInput"]),
    div[data-testid="stVerticalBlock"] > div:has(button) {
        max-width: 280px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    /* 入力欄のデザイン */
    div[data-testid="stTextInput"] {
        width: 100% !important;
        margin-bottom: 10px !important;
    }

    /* 【幅広ボタン】入力枠と同じ幅（100%）に固定 */
    div.stButton > button[kind="primary"] {
        width: 100% !important;   /* 親要素280pxいっぱいに広げる */
        height: 65px !important;  /* 高さを出してさらに押しやすく */
        border-radius: 10px !important;
        font-size: 28px !important; /* 数字を大きく強調 */
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
        margin-bottom: 5px !important;
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

    /* ログイン・CLR・削除ボタンなどの特殊ボタン */
    div.stButton > button[kind="secondary"] {
        width: 100% !important;
        height: 50px !important;
        margin-top: 5px !important;
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
    
    # 280px幅の入力欄
    password = st.text_input("アクセスパスワードを入力", value=st.session_state['temp_password'], type="password")

    # 1〜9, 0 の幅広ボタンを縦に並べる
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for num in nums:
        if st.button(num, key=f"n_{num}", type="primary"):
            st.session_state['temp_password'] += num
            st.rerun()

    # CLR（クリア）と削除を横並びにする場合はここも中央揃えを維持
    col_sub1, col_sub2 = st.columns(2)
    with col_sub1:
        if st.button("CLR", key="clr", type="secondary"):
            st.session_state['temp_password'] = ""
            st.rerun()
    with col_sub2:
        if st.button("⬅︎", key="del", type="secondary"):
            st.session_state['temp_password'] = st.session_state['temp_password'][:-1]
            st.rerun()

    # ログインボタン
    if st.button("ログイン", key="login_exec", type="secondary"):
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
    if st.button("ログアウト", key="logout"):
        st.session_state['authenticated'] = False
        st.session_state['temp_password'] = ""
        st.rerun()
