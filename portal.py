import streamlit as st

st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# デザイン調整
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .main-title { font-size: 22px; font-weight: bold; text-align: center; color: #1a365d; margin-top: 30px; }
    .pass-display { 
        font-size: 40px; text-align: center; letter-spacing: 15px; 
        color: #1a365d; margin: 30px 0; height: 50px;
    }
    div.stButton > button {
        width: 75px !important; height: 75px !important;
        border-radius: 50% !important;
        font-size: 26px !important; font-weight: 500 !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: none !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        margin: 0 auto !important;
    }
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

# セッション状態
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'input_pass' not in st.session_state:
    st.session_state['input_pass'] = ""

# --- 画面分岐 ---
if not st.session_state['logged_in']:
    st.markdown('<div class="main-title">パスコードを入力</div>', unsafe_allow_html=True)
    
    # 4文字入力されたら自動判定
    if len(st.session_state['input_pass']) == 4:
        if st.session_state['input_pass'] == "1234":
            st.session_state['logged_in'] = True
            st.session_state['input_pass'] = "" # クリアしておく
            st.rerun()
        else:
            st.error("パスコードが正しくありません")
            st.session_state['input_pass'] = "" # 間違えたらクリア
            # 少し待たせる（エラーを見せるため）

    display_pass = "●" * len(st.session_state['input_pass'])
    st.markdown(f'<div class="pass-display">{display_pass}</div>', unsafe_allow_html=True)

    # ボタン配置
    def create_key_row(k1, k2, k3):
        cols = st.columns([1, 1, 1, 1, 1])
        with cols[1]:
            if st.button(k1):
                if k1 == "Clear": st.session_state['input_pass'] = ""
                else: st.session_state['input_pass'] += k1
                st.rerun()
        with cols[2]:
            if st.button(k2):
                st.session_state['input_pass'] += k2
                st.rerun()
        with cols[3]:
            if st.button(k3):
                # 削除ボタン（BackSpace）の役割も持たせられますが、一旦数字として配置
                st.session_state['input_pass'] += k3
                st.rerun()

    create_key_row("1", "2", "3")
    create_key_row("4", "5", "6")
    create_key_row("7", "8", "9")
    
    # 0段目（Clear, 0, BackSpace的な配置）
    cols_last = st.columns([1, 1, 1, 1, 1])
    with cols_last[1]:
        if st.button("CLR"): # クリア
            st.session_state['input_pass'] = ""
            st.rerun()
    with cols_last[2]:
        if st.button("0"):
            st.session_state['input_pass'] += "0"
            st.rerun()
    with cols_last[3]:
        if st.button("⬅︎"): # 1文字消す
            st.session_state['input_pass'] = st.session_state['input_pass'][:-1]
            st.rerun()

else:
    # ログイン後の画面
    st.markdown('<div class="main-title">📱 業務アプリ一覧</div>', unsafe_allow_html=True)
    
    st.link_button("🏙️ 暮らしの立地スコア診断", "https://bbmns2pc89m86nxhkvqnet.streamlit.app/")
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/")
    st.link_button("🏢 マンション予想AI", "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/")
    st.link_button("🛠️ 内装リフォーム見積", "https://reform-xblfcovcvgk83yhwkypqbu.streamlit.app/")
    st.link_button("💰 ローン診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")
    st.link_button("📈 営業進捗管理", "https://my-sales-app-aog993sltv8vseasajfwvr.streamlit.app/")

    st.write("---")
    if st.button("🚪 ログアウト", use_container_width=True):
        st.session_state['logged_in'] = False
        st.session_state['input_pass'] = ""
        st.rerun()
