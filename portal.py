import streamlit as st

st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# セッション状態の初期化
if 'input_pass' not in st.session_state:
    st.session_state['input_pass'] = ""
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# パスワード判定ロジック
if len(st.session_state['input_pass']) == 4:
    if st.session_state['input_pass'] == "1234":
        st.session_state['logged_in'] = True
        st.session_state['input_pass'] = ""
    else:
        st.error("パスコードが正しくありません")
        st.session_state['input_pass'] = ""
    st.rerun()

# デザイン設定
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    
    /* テンキーを強制的に3列にするグリッド設定 */
    .keypad-grid {
        display: grid !important;
        grid-template-columns: repeat(3, 1fr) !important; /* 絶対に3列 */
        gap: 15px !important;
        max-width: 300px !important;
        margin: 0 auto !important;
        padding: 10px !important;
    }

    /* Streamlitのボタンをこのグリッドに適合させる */
    div.stButton > button {
        width: 100% !important;
        aspect-ratio: 1 / 1 !important; /* 正方形 */
        border-radius: 15px !important;
        font-size: 24px !important;
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
        transition: transform 0.1s !important;
    }

    /* 反応アニメーション */
    div.stButton > button:active {
        transform: scale(0.9) !important;
        background-color: #cbd5e0 !important;
    }
    
    .main-title { text-align: center; font-weight: bold; color: #1a365d; }
    .pass-display { text-align: center; font-size: 40px; letter-spacing: 15px; height: 60px; }
    </style>
""", unsafe_allow_html=True)

if not st.session_state['logged_in']:
    st.markdown('<p class="main-title">パスコードを入力</p>', unsafe_allow_html=True)
    
    display_dots = "●" * len(st.session_state['input_pass'])
    st.markdown(f'<div class="pass-display">{display_dots}</div>', unsafe_allow_html=True)

    # --- HTMLのdivで囲んで強制的に3列にする ---
    st.markdown('<div class="keypad-grid">', unsafe_allow_html=True)
    
    # 1から9までのボタン
    for i in range(1, 10):
        if st.button(str(i), key=f"btn_{i}"):
            st.session_state['input_pass'] += str(i)
            st.rerun()
            
    # 下段のボタン
    if st.button("CLR", key="btn_clr"):
        st.session_state['input_pass'] = ""
        st.rerun()
    if st.button("0", key="btn_0"):
        st.session_state['input_pass'] += "0"
        st.rerun()
    if st.button("⬅︎", key="btn_del"):
        st.session_state['input_pass'] = st.session_state['input_pass'][:-1]
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

else:
    # ログイン後画面
    st.markdown('<h3 style="text-align:center;">📱 業務アプリ一覧</h3>', unsafe_allow_html=True)
    st.link_button("🏙️ 暮らしの立地スコア診断", "https://bbmns2pc89m86nxhkvqnet.streamlit.app/", use_container_width=True)
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/", use_container_width=True)
    
    st.write("---")
    if st.button("ログアウト", type="secondary"):
        st.session_state['logged_in'] = False
        st.rerun()
