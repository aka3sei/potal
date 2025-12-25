import streamlit as st

st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 全体のデザインとアニメーション
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .main-title { font-size: 22px; font-weight: bold; text-align: center; color: #1a365d; margin-top: 30px; }
    
    .pass-display { 
        font-size: 40px; text-align: center; letter-spacing: 15px; 
        color: #1a365d; margin: 20px 0; height: 50px;
    }

    /* テンキーボタン：全ボタン共通 */
    div.stButton > button {
        width: 75px !important; height: 75px !important;
        border-radius: 50% !important;
        font-size: 26px !important; font-weight: 500 !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: none !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        margin: 0 auto !important;
        transition: transform 0.1s;
    }
    
    /* タップ時のアニメーション */
    div.stButton > button:active {
        transform: scale(0.85) !important;
        background-color: #cbd5e0 !important;
    }

    /* CLRと矢印ボタンの文字サイズ調整 */
    div.stButton > button p {
        font-size: 18px !important;
    }

    /* アプリリンクボタン */
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
    st.markdown('<div class="main-title">パスコードを入力</div>', unsafe_allow_html=True)
    
    # 4文字自動判定
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

    # テンキー表示用の関数
    def num_button(label, is_action=False):
        if st.button(label):
            if label == "CLR":
                st.session_state['input_pass'] = ""
            elif label == "⬅︎":
                st.session_state['input_pass'] = st.session_state['input_pass'][:-1]
            else:
                st.session_state['input_pass'] += label
            st.rerun()

    # 1-2-3から0までを配置
    rows = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["CLR", "0", "⬅︎"]
    ]

    for row in rows:
        c1, c2, c3, c4, c5 = st.columns([1, 1, 1, 1, 1])
        with c2: num_button(row[0])
        with c3: num_button(row[1])
        with c4: num_button(row[2])

else:
    # ログイン後
    st.markdown('<div class="main-title">📱 業務アプリ一覧</div>', unsafe_allow_html=True)
    
    st.link_button("🏙️ 暮らしの立地スコア診断", "https://bbmns2pc89m86nxhkvqnet.streamlit.app/")
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9
