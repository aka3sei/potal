import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: スマホの縦並びを禁止し、ボタンを巨大化する
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .main-title { font-size: 24px; font-weight: bold; text-align: center; color: #1a365d; margin-bottom: 20px; }
    
    /* 1. 入力欄を中央に寄せる */
    div[data-testid="stTextInput"] { max-width: 280px; margin: 0 auto !important; }

    /* 2. 【最重要】スマホでも絶対に縦に並べない設定 (2列固定) */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important; /* 強制横並び */
        flex-wrap: nowrap !important;   /* 折り返し禁止 */
        justify-content: center !important;
        gap: 10px !important;           /* ボタン間の隙間 */
        max-width: 280px !important;    /* 枠からはみ出さない幅 */
        margin: 10px auto !important;
    }
    [data-testid="column"] { flex: 1 !important; min-width: 0 !important; }

    /* 3. 巨大数字ボタンのデザイン */
    div.stButton > button[kind="primary"] {
        width: 100% !important;
        height: 70px !important;        /* スマホで押しやすい高さ */
        border-radius: 12px !important;
        font-size: 28px !important;     /* 数字を大きく */
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
    }
    
    /* アプリ一覧ボタンのデザイン */
    a[data-testid="stLinkButton"] {
        width: 100% !important; height: 70px !important;
        border-radius: 15px !important; font-size: 1.1rem !important;
        font-weight: bold !important; background-color: #ffffff !important;
        color: #1a365d !important; border: 2px solid #e2e8f0 !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        text-decoration: none !important; margin-bottom: 12px !important;
    }

    /* ログイン・ログアウトボタン */
    div.stButton > button[kind="secondary"] {
        width: 100% !important; height: 50px !important; margin-top: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# セッション状態の初期化
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if 'temp_password' not in st.session_state:
    st.session_state['temp_password'] = ""

# --- 1. パスワード認証画面 ---
if not st.session_state['authenticated']:
    st.markdown('<div class="main-title">🔒 営業支援システム</div>', unsafe_allow_html=True)
    
    # テキスト入力欄
    password = st.text_input("アクセスパスワードを入力", value=st.session_state['temp_password'], type="password")

    # テンキー配置（2列ずつ確実に配置）
    rows = [["1", "2"], ["3", "4"], ["5", "6"], ["7", "8"], ["9", "0"], ["CLR", "⬅︎"]]
    
    for row in rows:
        cols = st.columns(2) # ここで2列の枠を作る
        for i, val in enumerate(row):
            with cols[i]:
                if st.button(val, key=f"key_{val}", type="primary"):
                    if val == "CLR":
                        st.session_state['temp_password'] = ""
                    elif val == "⬅︎":
                        st.session_state['temp_password'] = st.session_state['temp_password'][:-1]
                    else:
                        st.session_state['temp_password'] += val
                    st.rerun()

    # ログインボタン
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
