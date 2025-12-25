import streamlit as st

st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 全機種で横並びを維持しつつ、幅をスリムに調整
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .block-container { padding: 1.5rem 1rem !important; }

    /* 1. タイトルと入力表示 */
    .main-title { font-size: 18px; font-weight: bold; text-align: center; color: #1a365d; margin-bottom: 5px; }
    .pass-display { font-size: 36px; text-align: center; letter-spacing: 12px; color: #1a365d; height: 50px; }

    /* 2. キーパッド全体の幅をスマホに合わせる (ここが肝) */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        justify-content: center !important;
        gap: 6px !important;            /* 間隔を狭くした(10px -> 6px) */
        width: 100% !important;
        max-width: 280px !important;    /* 全体幅をさらに絞った(320px -> 280px) */
        margin: 0 auto 6px auto !important;
    }
    
    [data-testid="column"] {
        flex: 1 !important;
        min-width: 0 !important;
    }

    /* 3. ボタン自体のサイズとデザイン */
    div.stButton > button[kind="primary"] {
        width: 100% !important;
        aspect-ratio: 1.1 / 1 !important; /* 少しだけ横長にして高さを抑えた */
        border-radius: 8px !important;
        font-size: 22px !important;      /* 文字も少しスリムに */
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 0 !important;
    }

    /* 数字の中央寄せ徹底 */
    div.stButton > button[kind="primary"] p {
        margin: 0 !important;
        line-height: 1 !important;
    }
    
    /* 押し込んだ時の沈む動き */
    div.stButton > button[kind="primary"]:active {
        transform: scale(0.92) !important;
        background-color: #cbd5e0 !important;
    }

    /* ログアウトボタン */
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

# セッション管理
if 'input_pass' not in st.session_state:
    st.session_state['input_pass'] = ""
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

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

    display_dots = "●" * len(st.session_state['input_pass'])
    st.markdown(f'<div class="pass-display">{display_dots}</div>', unsafe_allow_html=True)

    # 行作成関数
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
    st.markdown('<h3 style="text-align:center;">📱 業務アプリ一覧</h3>', unsafe_allow_html=True)
    st.link_button("🏙️ 暮らしの立地スコア診断", "https://bbmns2pc89m86nxhkvqnet.streamlit.app/", use_container_width=True)
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/", use_container_width=True)
    st.link_button("🏢 マンション予想AI", "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/", use_container_width=True)

    st.write("---")
    if st.button("ログアウト", type="secondary"):
        st.session_state['logged_in'] = False
        st.rerun()
