import streamlit as st

st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 強制的に横並びを維持する
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    
    /* 各行（3つのボタンの塊）をスマホでも横並びに固定 */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 10px !important;
        justify-content: center !important;
        max-width: 300px !important;
        margin: 0 auto 10px auto !important;
    }
    
    [data-testid="column"] {
        flex: 1 !important;
        min-width: 0 !important;
    }

    /* ボタンのデザイン：中央揃えとアニメーション */
    div.stButton > button[kind="primary"] {
        width: 100% !important;
        aspect-ratio: 1.2 / 1 !important;
        border-radius: 10px !important;
        font-size: 24px !important;
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    /* 押し込んだ時の沈む動き */
    div.stButton > button[kind="primary"]:active {
        transform: scale(0.90) !important;
        background-color: #cbd5e0 !important;
    }
    </style>
""", unsafe_allow_html=True)

if 'input_pass' not in st.session_state:
    st.session_state['input_pass'] = ""
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.markdown('<p style="text-align:center; font-weight:bold;">パスコードを入力</p>', unsafe_allow_html=True)
    
    # パスワード判定
    if len(st.session_state['input_pass']) == 4:
        if st.session_state['input_pass'] == "1234":
            st.session_state['logged_in'] = True
            st.session_state['input_pass'] = ""
            st.rerun()
        else:
            st.error("不正なコードです")
            st.session_state['input_pass'] = ""
            st.rerun()

    display_dots = "●" * len(st.session_state['input_pass'])
    st.markdown(f'<h1 style="text-align:center; letter-spacing:15px;">{display_dots}</h1>', unsafe_allow_html=True)

    # --- ここがポイント：1行（3つ）ずつ独立して配置 ---
    
    # 第1セット：1-2-3
    row1 = st.columns(3)
    with row1[0]:
        if st.button("1", key="b1", type="primary"): st.session_state['input_pass'] += "1"; st.rerun()
    with row1[1]:
        if st.button("2", key="b2", type="primary"): st.session_state['input_pass'] += "2"; st.rerun()
    with row1[2]:
        if st.button("3", key="b3", type="primary"): st.session_state['input_pass'] += "3"; st.rerun()

    # 第2セット：4-5-6
    row2 = st.columns(3)
    with row2[0]:
        if st.button("4", key="b4", type="primary"): st.session_state['input_pass'] += "4"; st.rerun()
    with row2[1]:
        if st.button("5", key="b5", type="primary"): st.session_state['input_pass'] += "5"; st.rerun()
    with row2[2]:
        if st.button("6", key="b6", type="primary"): st.session_state['input_pass'] += "6"; st.rerun()

    # 第3セット：7-8-9
    row3 = st.columns(3)
    with row3[0]:
        if st.button("7", key="b7", type="primary"): st.session_state['input_pass'] += "7"; st.rerun()
    with row3[1]:
        if st.button("8", key="b8", type="primary"): st.session_state['input_pass'] += "8"; st.rerun()
    with row3[2]:
        if st.button("9", key="b9", type="primary"): st.session_state['input_pass'] += "9"; st.rerun()

    # 第4セット：CLR-0-削除
    row4 = st.columns(3)
    with row4[0]:
        if st.button("CLR", key="b_clr", type="primary"): st.session_state['input_pass'] = ""; st.rerun()
    with row4[1]:
        if st.button("0", key="b0", type="primary"): st.session_state['input_pass'] += "0"; st.rerun()
    with row4[2]:
        if st.button("⬅︎", key="b_del", type="primary"): st.session_state['input_pass'] = st.session_state['input_pass'][:-1]; st.rerun()

else:
    st.success("ログイン済み")
    if st.button("ログアウト"):
        st.session_state['logged_in'] = False
        st.rerun()
