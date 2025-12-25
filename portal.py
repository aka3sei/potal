import streamlit as st

# ページ設定
st.set_page_config(page_title="不動産営業支援ポータル", layout="centered", initial_sidebar_state="collapsed")

# CSSでアプリっぽいデザインに調整
st.markdown("""
    <style>
    header[data-testid="stHeader"] { visibility: hidden; }
    .main-title { font-size: 24px; font-weight: bold; text-align: center; color: #1a365d; margin-bottom: 30px; }
    .app-card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin-bottom: 15px;
        transition: 0.3s;
    }
    .app-link {
        text-decoration: none;
        color: #1e293b;
        font-weight: bold;
        display: block;
    }
    </style>
""", unsafe_allow_html=True)

# 1. パスワード認証（ロック画面）
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    st.markdown('<div class="main-title">🔒 営業支援システム</div>', unsafe_allow_html=True)
    password = st.text_input("アクセスパスワードを入力", type="password")
    if st.button("ログイン", use_container_width=True):
        if password == "1234":  # ← 好きなパスワードに変更してください
            st.session_state['authenticated'] = True
            st.rerun()
        else:
            st.error("パスワードが正しくありません")
else:
    # 2. アプリリスト（2枚目の画面）
    st.markdown('<div class="main-title">📱 業務アプリ一覧</div>', unsafe_allow_html=True)
    
    # 各アプリのリンク設定
    apps = [
        {"name": "🏙️ 暮らしのスコア診断", "url": "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/"},
        {"name": "🏢 マンション予想AI", "url": "https://tokyo-mansion-ai-ds4tk2ddjdvxhdnbdcpghz.streamlit.app/"},
        {"name": "📈 営業進捗管理", "url": "https://my-sales-app-aog993sltv8vseasajfwvr.streamlit.app/"},
        {"name": "💰 ローン診断", "url": "https://kqhrxuaoh5vmuguuuyfbzg.streamlit.app/"}
    ]

    for app in apps:
        st.markdown(f"""
            <a href="{app['url']}" target="_self" class="app-link">
                <div class="app-card">
                    {app['name']}
                </div>
            </a>
        """, unsafe_allow_html=True)

    st.write("") # スペースを空ける
    if st.button("ログアウト", use_container_width=True):
        st.session_state['authenticated'] = False

        st.rerun()
