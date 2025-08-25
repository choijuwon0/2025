import streamlit as st

st.set_page_config(page_title="건강 체크 프로그램", page_icon="🩺", layout="wide")

# CSS로 배경 및 카드 스타일 변경
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #a8edea, #fed6e3);
        background-attachment: fixed;
    }
    .title {
        font-size: 42px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.2);
    }
    .card {
        padding: 20px;
        border-radius: 20px;
        background: rgba(255,255,255,0.6);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        backdrop-filter: blur(10px);
        margin-bottom: 25px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.25);
    }
    .sleep { border-left: 10px solid #9b59b6; }
    .meal { border-left: 10px solid #e67e22; }
    .exercise { border-left: 10px solid #2ecc71; }
    .water { border-left: 10px solid #3498db; }
    .stress { border-left: 10px solid #e74c3c; }
    </style>
""", unsafe_allow_html=True)

# 제목
st.markdown("<div class='title'>🩺 건강 체크 프로그램</div>", unsafe_allow_html=True)

# 카드 예시
with st.container():
    st.markdown("<div class='card sleep'>", unsafe_allow_html=True)
    st.subheader("🛏️ 수면 상태")
    st.write("7~9시간이 이상적입니다.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card water'>", unsafe_allow_html=True)
    st.subheader("💧 수분 섭취")
    st.write("하루 2000~2500ml (여성), 2500~3000ml (남성)")
    st.markdown("</div>", unsafe_allow_html=True)
