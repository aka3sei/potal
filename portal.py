import streamlit as st

st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# デザイン（アニメーション・丸ボタン）
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .main-title { font-size: 22px; font-weight: bold; text-align: center; color: #1a365d; margin-top: 20px; }
    .pass-display { 
        font-size: 40px; text-align: center; letter-spacing: 15px; 
        color: #1a365d; margin: 15px 0; height: 50px;
    }
    /* 丸ボタンのスタイル */
    div.stButton > button {
        width: 70px !important; height: 70px !important;
        border-radius: 50% !important;
        font-size: 24px !important; font-weight: 500 !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: none !important;
        margin: 0 auto !important;
        transition: transform 0.1s;
    }
    div.stButton > button:active {
        transform: scale(0.85) !important;
        background-color: #cbd5e0 !important;
    }
    /* ログイン後のリスト */
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

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'input_pass' not in st.session_state:
    st.session_state['input_pass'] = ""

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

    # テンキー配列（確実に4行作る）
    rows = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["CLR", "0", "⬅︎"]
    ]

    # ボタンを1行ずつ確実に描画
    for i, row in enumerate(rows):
        c1, c2, c3, c4, c5 = st.columns([1, 1, 1, 1, 1])
        # 各ボタンに一意のkey（例: btn_0_1）を付けてエラーを回避
        with c2:
            if st.button(row[0], key=f"btn_{i}_0"):
                if row[0] == "CLR": st.session_state['input_pass'] = ""
                else: st.session_state['input_pass'] += row[0]
                st.rerun()
        with c3:
            if st.button(row[1], key=f"btn_{i}_1"):
                st.session_state['input_pass'] += row[1]
                st.rerun()
        with c4:
            if st.button(row[2], key=f"btn_{i}_2"):
                if row[2] == "⬅︎": st.session_state['input_pass'] = st.session_state['input_pass'][:-1]
                else: st.session_state['input_pass'] += row[2]
                st.rerun()

else:
    # ログイン後
    st.markdown('<div class="main-title">📱 業務アプリ一覧</div>', unsafe_allow_html=True)
    
    st.link_button("🏙️ 暮らしの立地スコア診断", "https://bbmns2pc89m86nxhkvqnet.streamlit.app/")
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/")
    st.link_button("🏢 マンション予想AI", "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/")
    st.link_button("🛠️ 内装リフォーム見積", "https://reform-xblfcovcvgk83yhwkypqbu.streamlit.app/")
    st.link_button("💰 ローン診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")
    st.link_button("📈 営業進捗管理", "https://my-sales-app-aog993sltv8vseasajfwvr.streamlit.app/")

    st.write("---")
    if st.button("ログアウト", type="secondary"):
        st.session_state['logged_in'] = False
        st.session_state['input_pass'] = ""
        st.rerun()
