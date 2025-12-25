import streamlit as st

st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: スマホでも強制的に横に並べ、数字をど真ん中に置く
st.markdown("""
    <style>
    /* 余計な余白をカット */
    header[data-testid="stHeader"] { visibility: hidden; }
    .block-container { padding-top: 2rem !important; }

    /* 1. タイトルとパス表示の中央揃え */
    .main-title { font-size: 20px; font-weight: bold; text-align: center; color: #1a365d; margin-bottom: 5px; }
    .pass-display { font-size: 40px; text-align: center; letter-spacing: 15px; color: #1a365d; height: 60px; }

    /* 2. 【最重要】スマホでも横3列を強制するFlexbox設定 */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important; /* 横に並べる */
        flex-wrap: nowrap !important;   /* 折り返し禁止 */
        justify-content: center !important;
        gap: 8px !important;            /* ボタン間の隙間 */
        width: 100% !important;
        max-width: 320px !important;    /* 画面中央に寄せるための幅制限 */
        margin: 0 auto !important;
    }
    
    /* 各カラムが均等な幅になるように固定 */
    [data-testid="column"] {
        flex: 1 !important;
        min-width: 0 !important;
    }

    /* 3. ボタン自体のデザイン（四角で中央配置） */
    div.stButton > button[kind="primary"] {
        width: 100% !important;
        aspect-ratio: 1.2 / 1 !important; /* 押しやすい長方形 */
        border-radius: 8px !important;
        font-size: 24px !important;
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 0 !important;
    }
    
    /* ボタンの中の数字をミリ単位で中央に */
    div.stButton > button[kind="primary"] p {
        margin: 0 !important;
        line-height: 1 !important;
    }

    /* クリック時の沈むアニメーション */
    div.stButton > button[kind="primary"]:active {
        transform: scale(0.92) !important;
        background-color: #e2e8f0 !important;
    }

    /* ログアウトボタン（シンプル版） */
    div.stButton > button[kind="secondary"] {
        width: auto !important;
        padding: 4px 12px !important;
        font-size: 13px !important;
        border-radius: 4px !important;
        display: block !important;
        margin-left: auto !important;
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

    # テンキー配列（3列×4行）
    rows = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["CLR", "0", "⬅︎"]]
    
    for i, row in enumerate(rows):
        # ここで3つのカラムを作成
        cols = st.columns(3)
        for j, val in enumerate(row):
            with cols[j]:
                if st.button(val, key=f"btn_{i}_{j}", type="primary"):
                    if val == "CLR": st.session_state['input_pass'] = ""
                    elif val == "⬅︎": st.session_state['input_pass'] = st.session_state['input_pass'][:-1]
                    else: st.session_state['input_pass'] += val
                    st.rerun()

# --- ログイン後 ---
else:
    st.markdown('<h3 style="text-align:center;">📱 業務アプリ一覧</h3>', unsafe_allow_html=True)
    st.link_button("🏙️ 暮らしの立地スコア診断", "https://bbmns2pc89m86nxhkvqnet.streamlit.app/", use_container_width=True)
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/", use_container_width=True)
    st.link_button("🏢 マンション予想AI", "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/", use_container_width=True)
    
    st.write("---")
    if st.button("ログアウト", key="logout_btn", type="secondary"):
        st.session_state['logged_in'] = False
        st.session_state['input_pass'] = ""
        st.rerun()
