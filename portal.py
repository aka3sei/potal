import streamlit as st

st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# iPhone風テンキーのデザイン
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .main-title { font-size: 24px; font-weight: bold; text-align: center; color: #1a365d; margin-top: 20px; }
    .pass-display { 
        font-size: 40px; text-align: center; letter-spacing: 15px; 
        color: #1a365d; margin: 20px 0; height: 50px;
    }
    /* テンキーボタンのデザイン */
    div.stButton > button {
        width: 70px !important; height: 70px !important;
        border-radius: 50% !important; /* 丸ボタン */
        font-size: 24px !important; font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: none !important; margin: 10px auto !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
    }
    /* 業務アプリボタン（ログイン後）のデザイン */
    a[data-testid="stLinkButton"] {
        width: 100% !important; height: 70px !important;
        border-radius: 15px !important; font-size: 1.1rem !important;
        font-weight: bold !important; background-color: #ffffff !important;
        color: #1a365d !important; border: 2px solid #e2e8f0 !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        text-decoration: none !important; margin-bottom: 12px !important;
    }
    </style>
""", unsafe_allow_html=True)

# セッション状態の初期化
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'input_pass' not in st.session_state:
    st.session_state['input_pass'] = ""

# --- 画面分岐 ---
if not st.session_state['logged_in']:
    st.markdown('<div class="main-title">ENTER PASSCODE</div>', unsafe_allow_html=True)
    
    # 入力状況を「●」で表示
    display_pass = "●" * len(st.session_state['input_pass'])
    st.markdown(f'<div class="pass-display">{display_pass}</div>', unsafe_allow_html=True)

    # テンキーの配置 (3x4形式)
    keys = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["Clear", "0", "OK"]
    ]

    for row in keys:
        cols = st.columns([1, 1, 1, 1, 1]) # 左右に余白を作って中央寄せ
        with cols[1]:
            if st.button(row[0]):
                if row[0] == "Clear": st.session_state['input_pass'] = ""
                else: st.session_state['input_pass'] += row[0]
                st.rerun()
        with cols[2]:
            if st.button(row[1]):
                st.session_state['input_pass'] += row[1]
                st.rerun()
        with cols[3]:
            if st.button(row[2]):
                if row[2] == "OK":
                    if st.session_state['input_pass'] == "1234":
                        st.session_state['logged_in'] = True
                        st.rerun()
                    else:
                        st.error("パスワードが違います")
                        st.session_state['input_pass'] = ""
                        st.rerun()
                else:
                    st.session_state['input_pass'] += row[2]
                    st.rerun()

else:
    # 【ログイン後のアプリリスト画面】
    st.markdown('<div class="main-title">📱 業務アプリ一覧</div>', unsafe_allow_html=True)
    
    st.link_button("🏙️ 暮らしの立地スコア診断", "https://bbmns2pc89m86nxhkvqnet.streamlit.app/")
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/")
    st.link_button("🏢 マンション予想AI", "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/")
    st.link_button("🛠️ 内装リフォーム見積", "https://reform-xblfcovcvgk83yhwkypqbu.streamlit.app/")
    st.link_button("💰 ローン診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")
    st.link_button("📈 営業進捗管理", "https://my-sales-app-aog993sltv8vseasajfwvr.streamlit.app/")

    st.write("---")
    if st.button("🚪 ログアウトして画面をロック", use_container_width=True):
        st.session_state['logged_in'] = False
        st.session_state['input_pass'] = ""
        st.rerun()
