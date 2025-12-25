import streamlit as st

st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: アニメーションの追加とボタンデザインの微調整
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .main-title { font-size: 22px; font-weight: bold; text-align: center; color: #1a365d; margin-top: 30px; }
    
    /* パスコード表示エリア */
    .pass-display { 
        font-size: 40px; text-align: center; letter-spacing: 15px; 
        color: #1a365d; margin: 30px 0; height: 50px;
    }

    /* テンキーボタン：クリック時に少し凹むアニメーションを追加 */
    div.stButton > button {
        width: 75px !important; height: 75px !important;
        border-radius: 50% !important;
        font-size: 26px !important; font-weight: 500 !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: none !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        margin: 0 auto !important;
        transition: transform 0.1s, background-color 0.1s; /* 反応速度 */
    }
    /* 触れたとき・押したときの反応 */
    div.stButton > button:active {
        transform: scale(0.90) !important; /* ギュッと小さくなる */
        background-color: #cbd5e0 !important; /* 少し暗くなる */
    }

    /* 業務アプリリンクのデザイン */
    a[data-testid="stLinkButton"] {
        width: 100% !important; height: 70px !important;
        border-radius: 15px !important; font-size: 1.1rem !important;
        font-weight: bold !important; background-color: #ffffff !important;
        color: #1a365d !important; border: 2px solid #e2e8f0 !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        text-decoration: none !important; margin-bottom: 12px !important;
    }

    /* ログアウトボタン（以前のスタイル：丸くない標準ボタン） */
    .logout-btn > div > button {
        height: auto !important;
        width: auto !important;
        border-radius: 5px !important;
        font-size: 14px !important;
        padding: 5px 20px !important;
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
    
    # 4文字入力されたら自動判定
    if len(st.session_state['input_pass']) == 4:
        if st.session_state['input_pass'] == "1234":
            st.session_state['logged_in'] = True
            st.session_state['input_pass'] = "" 
            st.rerun()
        else:
            st.error("パスコードが正しくありません")
            st.session_state['input_pass'] = ""
            st.rerun()

    display_pass = "●" * len(st.session_state['input_pass'])
    st.markdown(f'<div class="pass-display">{display_pass}</div>', unsafe_allow_html=True)

    # テンキー配列
    def create_key_row(k1, k2, k3):
        cols = st.columns([1, 1, 1, 1, 1])
        with cols[1]:
            if st.button(k1):
                st.session_state['input_pass'] += k1
                st.rerun()
        with cols[2]:
            if st.button(k2):
                st.session_state['input_pass'] += k2
                st.rerun()
        with cols[3]:
            if st.button(k3):
                st.session_state['input_pass'] += k3
                st.rerun()

    create_key_row("1", "2", "3")
