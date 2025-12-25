import streamlit as st

st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: テンキーの3列死守と全中央揃え
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .block-container { padding: 1rem 1rem !important; }

    /* 1. タイトルとパス表示の中央揃え */
    .main-title { font-size: 20px; font-weight: bold; text-align: center; color: #1a365d; margin-top: 10px; }
    .pass-display { font-size: 40px; text-align: center; letter-spacing: 15px; color: #1a365d; margin: 10px 0; height: 55px; }

    /* 2. テンキーをスマホでも強制的に3列・中央にする */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        justify-content: center !important;
        gap: 8px !important;
        width: 100% !important;
        max-width: 300px !important;
        margin: 0 auto 8px auto !important;
    }
    [data-testid="column"] { flex: 1 !important; min-width: 0 !important; }

    /* 3. テンキーボタンのデザイン（数字ど真ん中） */
    div.stButton > button[kind="primary"] {
        width: 100% !important;
        aspect-ratio: 1.2 / 1 !important;
        border-radius: 10px !important;
        font-size: 24px !important;
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        padding: 0 !important;
    }
    div.stButton > button[kind="primary"] p { margin: 0 !important; line-height: 1 !important; }
    div.stButton > button[kind="primary"]:active { transform: scale(0.92) !important; background-color: #cbd5e0 !important; }

    /* 4. ログイン後の業務アプリリスト（大きく押しやすく） */
    a[data-testid="stLinkButton"] {
        width: 100% !important; height: 65px !important;
        border-radius: 12px !important; font-size: 1.05rem !important;
        font-weight: bold !important; background-color: #ffffff !important;
        color: #1a365d !important; border: 2px solid #e2e8f0 !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        text-decoration: none !important; margin-bottom: 10px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05) !important;
    }
    
    /* ログアウトボタン */
    div.stButton > button[kind="secondary"] {
        width: auto !important; padding: 4px 12px !important; font-size: 14px !important;
        border-radius: 4px !important; background-color: #f8fafc !important;
        color: #4a5568 !important; border: 1px solid #cbd5e0 !important;
        display: block !important; margin-left: auto !important;
    }
    </style>
""", unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'input_pass' not in st.session_state:
    st.session_state['input_pass'] = ""

# --- パスコード画面 ---
if not st.session_state['logged_in']:
    st.markdown('<div class="main-title">パスコードを入力</div>', unsafe_allow_html=True)
    
    if len(st.session_state['input_pass']) == 4:
        if st.session_state['input_pass'] == "1234":
            st.session_state['logged_in'] = True
            st.session_state['input_pass'] = ""
            st.rerun()
        else:
            st.error("パスコードが違います")
            st.session_state['input_pass'] = ""
            st.rerun()

    display_pass = "●" * len(st.session_state['input_pass'])
    st.markdown(f'<div class="pass-display">{display_pass}</div>', unsafe_allow_html=True)

    rows = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["CLR", "0", "⬅︎"]]
    for i, row in enumerate(rows):
        cols = st.columns(3)
        for j, val in enumerate(row):
            with cols[j]:
                if st.button(val, key=f"btn_{i}_{j}", type="primary"):
                    if val == "CLR": st.session_state['input_pass'] = ""
                    elif val == "⬅︎": st.session_state['input_pass'] = st.session_state['input_pass'][:-1]
                    else: st.session_state['input_pass'] += val
                    st.rerun()

# --- ログイン後：全アプリ一覧 ---
else:
    st.markdown('<div class="main-title">📱 業務アプリ一覧</div>', unsafe_allow_html=True)
    st.write("") # 少し余白
    
    # 登録されている全アプリのリンク
    st.link_button("🏙️ 暮らしの立地スコア診断", "https://bbmns2pc89m86nxhkvqnet.streamlit.app/")
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/")
    st.link_button("🏢 マンション予想AI", "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/")
    st.link_button("🛠️ 内装リフォーム見積", "https://reform-xblfcovcvgk83yhwkypqbu.streamlit.app/")
    st.link_button("💰 ローン診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")
    st.link_button("📈 営業進捗管理", "https://my-sales-app-aog993sltv8vseasajfwvr.streamlit.app/")

    st.write("---")
    if st.button("ログアウト", key="logout_btn", type="secondary"):
        st.session_state['logged_in'] = False
        st.session_state['input_pass'] = ""
        st.rerun()
