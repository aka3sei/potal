import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 中央揃え・強力な押し込みアニメーション・幅広デザイン
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    
    .stApp { display: flex; justify-content: center; }
    
    /* 入力欄とボタンの幅を280pxに固定して中央寄せ */
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
        font-size: 32px !important;
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
        display: block !important;
        margin: 0 auto 10px auto !important;
        transition: transform 0.05s ease !important;
    }

    /* 【押し込みアニメーション】押した瞬間に深く沈み、色を反転 */
    div.stButton > button:active {
        transform: scale(0.85) !important;
        background-color: #1a365d !important;
        color: #ffffff !important;
    }

    /* 削除ボタン専用のデザイン */
    div.stButton > button[kind="secondary"] {
        background-color: #e2e8f0 !important;
        height: 60px !important;
        font-size: 20px !important;
    }

    /* アプリ一覧ボタンのデザイン */
    a[data-testid="stLinkButton"] {
        width: 100% !important; height: 70px !important;
        border-radius: 15px !important; font-size: 1.1rem !important;
        font-weight: bold !important; background-color: #ffffff !important;
        color: #1a365d !important; border: 2px solid #e2e8f0 !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        text-decoration: none !important; margin-bottom: 15px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
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
    st.markdown('<h2 style="text-align:center;">🔒 営業支援システム</h2>', unsafe_allow_html=True)
    
    # パスワード入力欄（表示用）
    st.text_input("アクセスパスワードを入力", value=st.session_state['temp_password'], type="password")

    # 【重要】即時ログインロジック：4桁目に達した瞬間に判定
    if len(st.session_state['temp_password']) >= 4:
        if st.session_state['temp_password'] == "1234":
            st.session_state['authenticated'] = True
            st.session_state['temp_password'] = "" # 次回のためにクリア
            st.rerun()
        else:
            st.error("パスコードが違います")
            st.session_state['temp_password'] = "" # 間違えたら即リセット
            st.rerun()

    # 数字ボタン (1-0すべて配置)
    for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        if st.button(num, key=f"num_{num}"):
            st.session_state['temp_password'] += num
            st.rerun()

    # 削除ボタン
    if st.button("⬅︎ 一文字削除", key="del_key", type="secondary"):
        st.session_state['temp_password'] = st.session_state['temp_password'][:-1]
        st.rerun()

# --- 2. ログイン後：アプリ一覧 ---
else:
    st.markdown('<h2 style="text-align:center;">📱 業務アプリ一覧</h2>', unsafe_allow_html=True)
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
