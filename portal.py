import streamlit as st

st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# デザイン設定（2列に最適化）
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .block-container { padding: 1.5rem 1rem !important; }

    .main-title { font-size: 22px; font-weight: bold; text-align: center; color: #1a365d; margin-bottom: 10px; }
    .pass-display { font-size: 40px; text-align: center; letter-spacing: 15px; color: #1a365d; height: 60px; }

    /* 【2列レイアウト強制設定】 */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        justify-content: center !important;
        gap: 15px !important;
        max-width: 320px !important; /* 2列が綺麗に収まる幅 */
        margin: 0 auto 15px auto !important;
    }
    
    [data-testid="column"] {
        flex: 1 !important;
        min-width: 0 !important;
    }

    /* 【巨大ボタンデザイン】 */
    div.stButton > button[kind="primary"] {
        width: 100% !important;
        height: 80px !important;         /* 高さを出して押しやすく */
        border-radius: 15px !important;
        font-size: 32px !important;      /* 数字をかなり大きく */
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 0 !important;
    }

    /* ボタン内の数字を中央に固定 */
    div.stButton > button[kind="primary"] p {
        margin: 0 !important;
        line-height: 1 !important;
    }
    
    /* 押し込んだ時の沈む動き */
    div.stButton > button[kind="primary"]:active {
        transform: scale(0.92) !important;
        background-color: #cbd5e0 !important;
    }

    /* ログアウトボタン（以前のスタイル） */
    div.stButton > button[kind="secondary"] {
        width: auto !important;
        padding: 5px 15px !important;
        font-size: 14px !important;
        border-radius: 4px !important;
        margin-left: auto !important;
        display: block !important;
    }
    </style>
""", unsafe_allow_html=True)

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

    # 2列ずつの配列に再構成
    rows = [["1", "2"], ["3", "4"], ["5", "6"], ["7", "8"], ["9", "0"], ["CLR", "⬅︎"]]

    for i, row in enumerate(rows):
        cols = st.columns(2) # 2列に変更
        for j, val in enumerate(row):
            with cols[j]:
                if st.button(val, key=f"btn_{val}", type="primary"):
                    if val == "CLR": st.session_state['input_pass'] = ""
                    elif val == "⬅︎": st.session_state['input_pass'] = st.session_state['input_pass'][:-1]
                    else: st.session_state['input_pass'] += val
                    st.rerun()

else:
    st.markdown('<h3 style="text-align:center;">📱 業務アプリ一覧</h3>', unsafe_allow_html=True)
    st.link_button("🏙️ 暮らしの立地スコア診断", "https://bbmns2pc89m86nxhkvqnet.streamlit.app/", use_container_width=True)
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/", use_container_width=True)
    
    st.write("---")
    if st.button("ログアウト", key="logout_btn", type="secondary"):
        st.session_state['logged_in'] = False
        st.rerun()
