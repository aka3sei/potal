import streamlit as st

st.set_page_config(page_title="不動産営業支援ポータル", layout="centered")

# CSS: 徹底的に中央へ追い込む設定
st.markdown("""
    <style>
    /* ヘッダーと余計な余白をカット */
    header[data-testid="stHeader"] { visibility: hidden; }
    .block-container { padding: 1rem 1rem !important; }

    /* 1. タイトルとパス表示をど真ん中に固定 */
    .centered-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        text-align: center;
    }
    .main-title { font-size: 20px; font-weight: bold; color: #1a365d; margin-bottom: 5px; }
    .pass-display { font-size: 40px; letter-spacing: 12px; color: #1a365d; height: 60px; }

    /* 2. テンキーを「スマホでも絶対3列」かつ「中央」にする */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        justify-content: center !important;
        gap: 8px !important;
        width: 100% !important;
        max-width: 320px !important; /* ボタンが広がりすぎないように制限 */
        margin: 0 auto !important;
    }
    [data-testid="column"] {
        flex: 1 !important;
        min-width: 0 !important;
    }

    /* 3. ボタン自体のデザインと「数字のど真ん中」配置 */
    div.stButton > button[kind="primary"] {
        width: 100% !important;
        aspect-ratio: 1 / 1 !important; /* 正方形に近づける */
        border-radius: 12px !important;
        font-size: 24px !important;
        font-weight: bold !important;
        background-color: #f0f2f6 !important;
        color: #1a365d !important;
        border: 1px solid #d1d5db !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* ボタン内の余白（Pタグ）を殺して中央を出す */
    div.stButton > button[kind="primary"] p {
        margin: 0 !important;
        line-height: 1 !important;
        display: block !important;
    }
    
    /* 押し込んだ時の沈む動き */
    div.stButton > button[kind="primary"]:active {
        transform: scale(0.90) !important;
        background-color: #e2e8f0 !important;
    }

    /* ログイン後のリストデザイン */
    a[data-testid="stLinkButton"] {
        width: 100% !important; height: 60px !important;
        border-radius: 12px !important; font-size: 1.1rem !important;
        font-weight: bold !important; background-color: #ffffff !important;
        color: #1a365d !important; border: 2px solid #e2e8f0 !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        text-decoration: none !important; margin-bottom: 8px !important;
    }

    /* ログアウトボタン（右下・シンプル） */
    div.stButton > button[kind="secondary"] {
        width: auto !important; height: auto !important;
        padding: 5px 12px !important; font-size: 13px !important;
        border-radius: 4px !important; background-color: #f8fafc !important;
        color: #666 !important; border: 1px solid #ddd !important;
        display: block !important; margin-left: auto !important;
    }
    </style>
""", unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'input_pass' not in st.session_state:
    st.session_state['input_pass'] = ""

# --- パスコード画面 ---
if not st.session_state['logged_in']:
    # まとめて中央寄せ用のラッパー
    st.markdown('<div class="centered-wrapper">', unsafe_allow_html=True)
    st.markdown('<div class="main-title">パスコードを入力</div>', unsafe_allow_html=True)
    
    # 判定ロジック
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
    st.markdown('</div>', unsafe_allow_html=True) # Wrapper閉じ

    # テンキー
    rows = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["CLR", "0", "⬅︎"]]
    for i, row in enumerate(rows):
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
    st.markdown('<div class="centered-wrapper"><div class="main-title">📱 業務アプリ一覧</div></div>', unsafe_allow_html=True)
    st.link_button("🏙️ 暮らしの立地スコア診断", "https://bbmns2pc89m86nxhkvqnet.streamlit.app/")
    st.link_button("🚉 最寄り駅・周辺検索", "https://moyori-6e5qmrnhwfjieq9wfdtcee.streamlit.app/")
    st.link_button("🏢 マンション予想AI", "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/")
    st.link_button("🛠️ 内装リフォーム見積", "https://reform-xblfcovcvgk83yhwkypqbu.streamlit.app/")
    st.link_button("💰 ローン診断", "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/")
    st.link_button("📈 営業進捗管理", "https://my-sales-app-aog993sltv8vseasajfwvr.streamlit.app/")

    st.write("---")
    if st.button("ログアウト", key="logout_btn", type="secondary"):
        st.session_state['logged_in'] = False
        st.session_state['input_pass'] = ""
        st.rerun()
