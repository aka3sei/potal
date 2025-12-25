import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: アニメーションの強制適用と中央揃え
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    
    .stApp { display: flex; justify-content: center; }
    
    /* 入力欄とボタンの幅を280pxに固定 */
    [data-testid="stVerticalBlock"] > div {
        width: 280px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    /* 巨大ボタンと強力な押し込みアニメーション */
    div.stButton > button {
        width: 100% !important;
        height: 75px !important;
        border-radius: 15px !important;
        font-size: 30px !important;
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
        display: block !important;
        margin: 0 auto 10px auto !important;
        /* アニメーション設定 */
        transition: transform 0.05s ease-in-out !important;
    }

    /* 【修正】より確実に反応するアニメーション設定 */
    div.stButton > button:active {
        transform: scale(0.90) !important;       /* 10%縮小して深く沈ませる */
        background-color: #1a365d !important;    /* 押した瞬間だけ色を濃い紺に */
        color: #ffffff !important;               /* 文字を白く */
        border: none !important;
    }

    /* 特殊ボタン（削除） */
    div.stButton > button[kind="secondary"] {
        background-color: #e2e8f0 !important;
        height: 60px !important;
        font-size: 20px !important;
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
    
    # パスワード入力欄（即ログイン判定用）
    password = st.text_input("アクセスパスワードを入力", value=st.session_state['temp_password'], type="password")

    # 即ログインのロジック
    if len(password) == 4:
        if password == "1234":
            st.session_state['authenticated'] = True
            st.rerun()
        else:
            st.error("パスコードが違います")
            st.session_state['temp_password'] = ""
            st.rerun()

    # 1〜5までのボタン
    nums = ["1", "2", "3", "4", "5"]
    for num in nums:
        if st.button(num, key=f"num_{num}"):
            st.session_state['temp_password'] += num
            st.rerun()

    # 一文字消すボタン
    if st.button("⬅︎ 削除", key="del_key", type="secondary"):
        st.session_state['temp_password'] = st.session_state['temp_password'][:-1]
        st.rerun()

# --- ログイン後 ---
else:
    st.markdown('<h2 style="text-align:center;">📱 業務アプリ一覧</h2>', unsafe_allow_html=True)
    # ここにご提示いただいたリンクを配置
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
