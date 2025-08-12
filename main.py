import streamlit as st
import random

st.set_page_config(page_title="MBTI × 하루 운세", layout="centered")

st.markdown("""
<h1 style='text-align: center; color: #FF69B4;'>🌟 MBTI로 보는 오늘의 하루 운세 🔮 🌟</h1>
<p style='text-align: center; font-size: 18px;'>MBTI를 선택하시면 <strong>당신만을 위한 화려한 하루 운세</strong>를 알려드립니다!</p>
""", unsafe_allow_html=True)

MBTI_UNSE = {
    "INTJ": "💼 계획했던 일이 순조롭게 진행됩니다. 세부 사항까지 신경 쓰면 좋은 성과가 있습니다.",
    "INFP": "💖 따뜻한 하루가 펼쳐집니다. 주변 사람과의 관계에서 기분 좋은 일이 생깁니다.",
    "ENFP": "✨ 새로운 기회와 만남이 찾아옵니다. 열린 마음으로 맞이하세요.",
    "ENTJ": "👑 리더십을 발휘할 순간이 옵니다. 결단력이 빛나는 하루가 될 것입니다.",
    "ISTP": "🛠 문제 해결 능력이 돋보입니다. 침착하게 대응하면 좋은 결과를 얻습니다.",
    "ISFJ": "🤝 누군가를 도우면 그 복이 곧 돌아옵니다.",
    "ESFP": "🎉 활기차고 즐거운 하루입니다. 긍정적인 에너지를 마음껏 나누세요.",
    "ESTJ": "📈 목표에 집중하면 성과를 거둘 수 있는 날입니다.",
    "ENTP": "💡 창의적인 아이디어가 빛을 발합니다. 자유롭게 표현하세요.",
    "INFJ": "🔮 깊은 통찰력이 발휘되는 하루입니다. 중요한 결정을 내리기 좋습니다.",
    "ISFP": "🎨 감성이 풍부해집니다. 예술적 영감을 받기 좋은 날입니다.",
    "ESTP": "🚀 도전이 행운을 부릅니다. 새로운 시도를 해보세요.",
    "ESFJ": "💬 협력이 순조롭습니다. 서로 도움을 주고받으며 발전합니다.",
    "ISTJ": "🏆 성실함이 보상받는 하루입니다. 꾸준함이 빛납니다."
}

mbti_list = sorted(MBTI_UNSE.keys())
selected = st.selectbox("💎 MBTI를 선택해 주세요 💎", ["선택 없음"] + mbti_list)

if selected != "선택 없음":
    st.markdown(f"<h2 style='color: #FFD700;'>{selected} — 오늘의 하루 운세</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:18px;'>{MBTI_UNSE[selected]}</p>", unsafe_allow_html=True)
    if st.button("🌠 랜덤 하루 조언 받기 🎲"):
        advice_list = [
            "🌈 긍정적인 마음이 좋은 기운을 부릅니다.",
            "💎 작은 친절이 큰 행운이 됩니다.",
            "🔥 오늘은 과감한 결정을 해보세요.",
            "🌿 휴식을 취하며 에너지를 회복하세요.",
            "💌 좋은 사람과의 대화가 큰 영감을 줍니다."
        ]
        st.success(random.choice(advice_list))
else:
    st.info("MBTI를 선택하시면 오늘의 하루 운세를 알려드립니다.")
