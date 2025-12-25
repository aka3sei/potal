import streamlit as st

st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 全機種で横並びを強制し、デザインを整える
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    
    /* 1. タイトルと入力表示を中央へ */
    .main-title { text-align: center; font-weight: bold; color: #1a365d; margin-bottom: 5px; }
    .pass-display { text-align: center; font-size: 40px; letter-spacing: 15px; height: 60px; color: #1a365d; }

    /* 2. 【最重要】スマホでもPCでも横並びを強制する */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important; /* 横に並べる */
        flex-wrap: nowrap !important;   /* 折り返しを禁止 */
        justify-content: center !important;
        gap: 10px !important;           /* ボタン間の隙間 */
        max-width: 320px !important;    /* キーパッドの幅を固定 */
        margin: 0 auto 10px auto !important;
    }
    
    /* カラムの幅を3等分に固定 */
    [data-testid="column"] {
        flex: 1 !important;
        min-width: 0 !important;
    }

    /* 3. ボタンのデザイン：中央揃え・角丸四角・アニメーション */
    div.stButton > button[kind="primary"] {
        width: 100% !important;
        aspect-ratio: 1.2 / 1 !important;
        border-radius: 12px !important;
        font-size: 24px !important;
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: transform 0.1s;
    }

    /* 数字をど真ん中に固定 */
    div.stButton > button[kind="primary"] p {
        margin: 0 !important;
        line-height: 1 !important;
    }
    
    /* 反応アニメーション：沈む動き */
    div.stButton > button[kind="primary"]:active {
        transform: scale(0.92) !important;
        background-color: #cbd5e0 !important;
    }

    /* ログアウトボタン（以前のスタイル） */
    div.stButton > button[kind="secondary"] {
        width: auto !important;
        height: auto !important;
        padding: 5px 15px !important;
        font-size: 14px !important;
        border-radius: 4px !important;
        display: block !important;
        margin-left: auto !important;
    }
    </style>
""", unsafe_allow_html=True)

# セッション状態
if 'input_pass' not in st.session_state:
    st.session_state['input_pass'] = ""
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# パスコード判定
if not st.session_state['logged_in']:
    if len(st.session_state['input_pass']) == 4:
        if st.session_state['input_pass'] == "1234":
            st.session_state['logged_in'] = True
            st.session_state['input_pass'] = ""
            st.rerun()
        else:
            st.error("パスコードが違います")
            st.session_state['input_pass'] = ""
            st.rerun()

    st.markdown('<p class="main-title">パスコードを入力</p>', unsafe_allow_html=True)
    display_dots = "●" * len(st.session_state['input_pass'])
    st.markdown(f'<div class="pass-display">{display_dots}</div>', unsafe_allow_html=True)

    # --- 1行ずつ st.columns(3) を作ることで強制的に3列にする ---
    def create_row(keys):
        cols = st.columns(3)
        for i, key in enumerate(keys):
            with cols[i]:
                if st.button(key, key=f"btn_{key}", type="primary"):
                    if key == "CLR": st.session_state['input_pass'] = ""
                    elif key == "⬅︎": st.session_state['input_pass'] = st.session_state['input_pass'][:-1]
                    else: st.session_state['input_pass'] += key
                    st.rerun()

    create_row(["1", "2", "3"])
    create_row(["4", "5", "6"])
    create_row(["7", "8", "9"])
    create_row(["CLR", "0", "⬅︎"])

else:
    # ログイン後画面
    st.markdown('<h3 style="text-align:center;">📱 業務アプリ一覧</h3>', unsafe_allow_html=True)
    st.link_button("🏙️ 暮らしの立地スコア診断", "https://bbmns2pc89m86nxhkvqnet.streamlit.app/", use_container_width=True)
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/", use_container_width=True)
    
    st.write("---")
    if st.button("ログアウト", type="secondary"):
        st.session_state['logged_in'] = False
        st.rerun()
