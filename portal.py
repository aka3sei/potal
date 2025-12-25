import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 余計な余白を排除し、中央揃えを絶対化する
st.markdown("""
    <style>
    /* ヘッダー非表示 */
    header[data-testid="stHeader"] { visibility: hidden; }
    
    /* 1. 全ての親要素を中央寄せにする */
    .stApp {
        display: flex;
        justify-content: center;
    }
    
    /* 2. 入力欄とボタンの幅を280pxに固定し、中央に強制配置 */
    [data-testid="stVerticalBlock"] > div {
        width: 280px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    /* 3. 入力欄自体の幅と中央寄せ */
    div[data-testid="stTextInput"] {
        width: 100% !important;
        margin: 0 auto !important;
    }

    /* 4. 【重要】「1」のボタンを幅いっぱい（280px）にし、高さを出す */
    div.stButton > button {
        width: 100% !important;   /* 親要素280pxに対して100% */
        height: 80px !important;   /* 押しやすい高さ */
        border-radius: 12px !important;
        font-size: 32px !important; /* 数字を大きく */
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
        display: block !important;
        margin: 0 auto !important;
    }

    /* ログインボタンなどの二次的ボタンも幅を統一 */
    div.stButton > button[kind="secondary"] {
        width: 100% !important;
        height: 50px !important;
        margin-top: 20px !important;
    }
    </style>
""", unsafe_allow_html=True)

# セッション状態
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if 'temp_password' not in st.session_state:
    st.session_state['temp_password'] = ""

# --- パスコード画面 ---
if not st.session_state['authenticated']:
    st.markdown('<h2 style="text-align:center;">🔒 営業支援システム</h2>', unsafe_allow_html=True)
    
    # 中央に配置された280px幅の入力欄
    password = st.text_input("アクセスパスワードを入力", value=st.session_state['temp_password'], type="password")

    # 全く同じ幅で中央に配置される「1」ボタン
    if st.button("1", key="num_1"):
        st.session_state['temp_password'] += "1"
        st.rerun()

    # ログインボタン
    if st.button("ログイン", key="login_exec", type="secondary"):
        if password == "1234":
            st.session_state['authenticated'] = True
            st.rerun()
        else:
            st.error("パスワードが正しくありません")
            st.session_state['temp_password'] = ""

# --- ログイン後 ---
else:
    st.markdown('<h2 style="text-align:center;">📱 業務アプリ一覧</h2>', unsafe_allow_html=True)
    st.write("認証に成功しました。")
    if st.button("ログアウト", type="secondary"):
        st.session_state['authenticated'] = False
        st.rerun()
