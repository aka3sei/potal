import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 枠のサイズと中央寄せを強制
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .main-title { font-size: 24px; font-weight: bold; text-align: center; color: #1a365d; margin-bottom: 20px; }
    
    /* 入力欄とボタンを包む「親要素」を280pxにして中央に置く */
    [data-testid="stVerticalBlock"] > div:has(div[data-testid="stTextInput"]),
    [data-testid="stVerticalBlock"] > div:has(button) {
        max-width: 280px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }

    /* 入力欄のデザイン */
    div[data-testid="stTextInput"] {
        width: 100% !important;
        margin-bottom: 15px !important;
    }

    /* ボタンのデザイン：入力枠と同じ幅（100%）に強制 */
    div.stButton > button {
        width: 100% !important;   /* これで親要素の280pxいっぱいに広がる */
        height: 60px !important;
        border-radius: 8px !important;
        font-size: 24px !important;
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
    }

    /* ボタン内の数字の位置微調整 */
    div.stButton > button p {
        margin: 0 !important;
        line-height: 1 !important;
    }

    /* アプリ一覧ボタン（ログイン後） */
    a[data-testid="stLinkButton"] {
        width: 100% !important; height: 65px !important;
        border-radius: 12px !important; font-size: 1.1rem !important;
        font-weight: bold !important; background-color: #ffffff !important;
        color: #1a365d !important; border: 2px solid #e2e8f0 !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        text-decoration: none !important; margin-bottom: 10px !important;
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
    
    # 280pxに固定された入力欄
    password = st.text_input("アクセスパスワードを入力", value=st.session_state['temp_password'], type="password")

    # 全く同じ280px幅の「1」ボタン
    if st.button("1", key="num_1"):
        st.session_state['temp_password'] += "1"
        st.rerun()

    st.write("") 
    
    # ログインボタン
    if st.button("ログイン"):
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
    if st.button("ログアウト"):
        st.session_state['authenticated'] = False
        st.session_state['temp_password'] = ""
        st.rerun()
