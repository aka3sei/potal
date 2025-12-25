import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 階層を無視して強制的に中央へ寄せる
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    
    /* 1. 全てのブロックを強制的に中央へ */
    div[data-testid="stVerticalBlock"] > div {
        width: 100% !important;
        display: flex !important;
        justify-content: center !important;
    }

    /* 2. 入力欄と2列ボタンのコンテナ幅を280pxに固定 */
    div[data-testid="stTextInput"], 
    div[data-testid="stHorizontalBlock"] {
        width: 280px !important;
        flex-shrink: 0 !important;
    }

    /* 3. 2列並びを維持 */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        gap: 10px !important;
    }
    div[data-testid="column"] {
        flex: 1 !important;
    }

    /* 4. ワイドボタンのデザイン */
    div.stButton > button[kind="primary"] {
        width: 100% !important;
        height: 70px !important;
        border-radius: 10px !important;
        font-size: 28px !important;
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
    }

    /* 5. ログイン・リスト・特殊ボタンも中央揃えと幅を統一 */
    div.stButton > button[kind="secondary"],
    a[data-testid="stLinkButton"] {
        width: 280px !important;
        margin: 0 auto !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }

    a[data-testid="stLinkButton"] {
        height: 65px !important;
        border-radius: 12px !important;
        font-size: 1.1rem !important;
        font-weight: bold !important;
        background-color: #ffffff !important;
        color: #1a365d !important;
        border: 2px solid #e2e8f0 !important;
        text-decoration: none !important;
        margin-bottom: 10px !important;
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
    st.markdown('<h2 style="text-align:center;">🔒 営業支援システム</h2>', unsafe_allow_html=True)
    
    # 中央寄せされた入力欄
    password = st.text_input("アクセスパスワードを入力", value=st.session_state['temp_password'], type="password")

    # 2列ずつのワイドボタン
    rows = [["1", "2"], ["3", "4"], ["5", "6"], ["7", "8"], ["9", "0"], ["CLR", "⬅︎"]]
    
    for row in rows:
        cols = st.columns(2)
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
    if st.button("ログイン", key="login_exec", type="secondary"):
        if password == "1234":
            st.session_state['authenticated'] = True
            st.rerun()
        else:
            st.error("パスワードが正しくありません")
            st.session_state['temp_password'] = ""

# --- 2. 業務アプリ一覧画面 ---
else:
    st.markdown('<h2 style="text-align:center;">📱 業務アプリ一覧</h2>', unsafe_allow_html=True)
    
    st.link_button("🏙️ 暮らしのスコア診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/")
    st.link_button("🏢 マンション予想AI", "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/")
    st.link_button("📈 営業進捗管理", "https://my-sales-app-aog993sltv8vseasajfwvr.streamlit.app/")
    st.link_button("💰 ローン診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")

    st.write("---")
    if st.button("ログアウト", key="logout", type="secondary"):
        st.session_state['authenticated'] = False
        st.session_state['temp_password'] = ""
        st.rerun()
