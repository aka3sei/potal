import streamlit as st

st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: ボタンをさらに小さくし、3列を絶対死守する
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .block-container { padding: 1rem 0.5rem !important; }

    /* 1. タイトル周りをコンパクトに */
    .main-title { font-size: 18px; font-weight: bold; text-align: center; color: #1a365d; margin-bottom: 0px; }
    .pass-display { font-size: 28px; text-align: center; letter-spacing: 8px; color: #1a365d; height: 35px; margin: 5px 0; }

    /* 2. 【究極修正】横幅を210pxまで絞り、隙間も最小(2px)に */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        justify-content: center !important;
        gap: 2px !important;            /* 隙間をほぼゼロに */
        width: 100% !important;
        max-width: 210px !important;    /* 230pxからさらに絞り込み */
        margin: 0 auto 4px auto !important;
    }
    
    [data-testid="column"] {
        flex: 1 !important;
        min-width: 0 !important;
        padding: 0 !important;         /* カラム自体の余白を消去 */
    }

    /* 3. ボタン：さらに小さく、スリムに */
    div.stButton > button[kind="primary"] {
        width: 100% !important;
        height: 45px !important;         /* 高さをさらに抑える */
        border-radius: 6px !important;
        font-size: 16px !important;      /* 数字も小さめに */
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 0 !important;
        min-width: 0 !important;
    }

    /* 数字のズレを徹底修正 */
    div.stButton > button[kind="primary"] div p {
        margin: 0 !important;
        line-height: 1 !important;
    }
    
    /* 押し込んだ時の動き */
    div.stButton > button[kind="primary"]:active {
        transform: scale(0.9) !important;
    }

    /* ログアウトボタン（影響を受けないよう隔離） */
    div.stButton > button[kind="secondary"] {
        width: auto !important;
        height: auto !important;
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

# パスコード入力画面
if not st.session_state['logged_in']:
    st.markdown('<div class="main-title">パスコードを入力</div>', unsafe_allow_html=True)
    
    # 4文字で自動判定
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

    # 行ごとに作成（3列を強制）
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
    # ログイン後のメイン画面
    st.markdown('<h3 style="text-align:center;">📱 業務アプリ一覧</h3>', unsafe_allow_html=True)
    st.link_button("🏙️ 暮らしの立地スコア診断", "https://bbmns2pc89m86nxhkvqnet.streamlit.app/", use_container_width=True)
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/", use_container_width=True)
    
    st.write("---")
    # ログアウトボタン（以前のスタイルを維持）
    if st.button("ログアウト", key="logout_btn", type="secondary"):
        st.session_state['logged_in'] = False
        st.rerun()
