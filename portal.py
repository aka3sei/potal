import streamlit as st

st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 限界まで横幅を詰め、強制的に3列を維持する
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .block-container { padding: 1rem 0.5rem !important; }

    /* 1. タイトルとパス表示 */
    .main-title { font-size: 18px; font-weight: bold; text-align: center; color: #1a365d; margin-bottom: 0px; }
    .pass-display { font-size: 30px; text-align: center; letter-spacing: 10px; color: #1a365d; height: 40px; margin-top: 5px; }

    /* 2. 【最重要】横幅をさらに230pxまで絞り、絶対に3列にする */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        justify-content: center !important;
        gap: 4px !important;            /* 隙間を極限まで狭く(4px) */
        width: 100% !important;
        max-width: 230px !important;    /* 250pxから230pxへさらに縮小 */
        margin: 0 auto 4px auto !important;
    }
    
    [data-testid="column"] {
        flex: 1 !important;
        min-width: 0 !important;
    }

    /* 3. ボタン：スリム化と中央配置 */
    div.stButton > button[kind="primary"] {
        width: 100% !important;
        height: 50px !important;         /* 高さを固定してスリムに */
        border-radius: 8px !important;
        font-size: 18px !important;      /* 数字も少し小さく */
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 0 !important;
    }

    /* 文字の位置を微調整 */
    div.stButton > button[kind="primary"] p {
        margin: 0 !important;
        line-height: 1 !important;
    }
    
    /* 押し込んだ時の動き */
    div.stButton > button[kind="primary"]:active {
        transform: scale(0.92) !important;
    }

    /* ログアウトボタン */
    div.stButton > button[kind="secondary"] {
        width: auto !important;
        padding: 2px 8px !important;
        font-size: 11px !important;
        margin-left: auto !important;
    }
    </style>
""", unsafe_allow_html=True)

# セッション管理
if 'input_pass' not in st.session_state:
    st.session_state['input_pass'] = ""
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.markdown('<div class="main-title">パスコードを入力</div>', unsafe_allow_html=True)
    
    # 判定
    if len(st.session_state['input_pass']) == 4:
        if st.session_state['input_pass'] == "1234":
            st.session_state['logged_in'] = True
            st.session_state['input_pass'] = ""
            st.rerun()
        else:
            st.error("パスコードが違います")
            st.session_state['input_pass'] = ""
            st.rerun()

    display_dots = "●" * len(st.session_state['input_pass'])
    st.markdown(f'<div class="pass-display">{display_dots}</div>', unsafe_allow_html=True)

    def create_row(keys):
        cols = st.columns(3)
        for i, key in enumerate(keys):
            with cols[i]:
                # すべてに type="primary" を指定して一貫性を持たせる
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
    if st.button("ログアウト", key="logout_btn", type="secondary"):
        st.session_state['logged_in'] = False
        st.rerun()
