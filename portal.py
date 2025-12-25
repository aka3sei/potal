import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 中央揃え・幅広デザイン・押し込みアニメーション
st.markdown("""
    <style>
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

    /* 4. 【幅広ボタン】アニメーション付き */
    div.stButton > button {
        width: 100% !important;
        height: 70px !important;
        border-radius: 12px !important;
        font-size: 28px !important;
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
        display: block !important;
        margin: 0 auto 8px auto !important;
        transition: all 0.1s ease !important; /* なめらかな変化 */
    }

    /* 【重要】押し込みアニメーション (Active状態) */
    div.stButton > button:active {
        transform: scale(0.95) !important;      /* 95%の大きさに縮小（沈む） */
        background-color: #cbd5e0 !important;   /* 少し暗い色にして影を表現 */
        border: 2px solid #a0aec0 !important;   /* 枠線を強調 */
        box-shadow: inset 0 3px 5px rgba(0,0,0,0.1) !important; /* 内側に影を付けて凹みを表現 */
    }

    /* 5. ログイン・特殊ボタンのデザイン */
    div.stButton > button[kind="secondary"] {
        background-color: #e2e8f0 !important;
        height: 60px !important;
        font-size: 20px !important;
        margin-top: 10px !important;
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

    # 1〜5までの幅広ボタン
    nums = ["1", "2", "3", "4", "5"]
    for num in nums:
        if st.button(num, key=f"num_{num}"):
            st.session_state['temp_password'] += num
            st.rerun()

    # 一文字消すボタン
    if st.button("⬅︎ (一文字消す)", key="del_key", type="secondary"):
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

# --- ログイン後 ---
else:
    st.markdown('<h2 style="text-align:center;">📱 業務アプリ一覧</h2>', unsafe_allow_html=True)
    st.write("認証に成功しました。")
    if st.button("ログアウト", type="secondary"):
        st.session_state['authenticated'] = False
        st.rerun()
