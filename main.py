import streamlit as st
import random

st.set_page_config(page_title="MBTI × 원피스 캐릭터 추천", layout="centered")

st.title("MBTI로 어울리는 원피스 캐릭터 찾기 ☠️✨")
st.write("MBTI를 선택하시면 어울리는 원피스 캐릭터를 추천해 드립니다. 모든 MBTI 유형이 준비되어 있습니다.")

MBTI_DB = {
    "INTJ": {"desc": "전략적이며 계획적인 완벽주의자입니다.", "chars": [{"name": "Nico Robin", "anime": "One Piece", "why": "지식과 전략에 능숙합니다.", "img": "https://upload.wikimedia.org/wikipedia/en/9/95/Nico_Robin.png"}]},
    "INFP": {"desc": "이상주의적이고 따뜻한 마음을 지녔습니다.", "chars": [{"name": "Chopper", "anime": "One Piece", "why": "순수하고 동료애가 강합니다.", "img": "https://upload.wikimedia.org/wikipedia/en/0/0c/Tony_Tony_Chopper.png"}]},
    "ENFP": {"desc": "열정적이고 모험을 좋아합니다.", "chars": [{"name": "Luffy", "anime": "One Piece", "why": "자유롭고 즐겁게 살아갑니다.", "img": "https://upload.wikimedia.org/wikipedia/en/2/29/Monkey_D_Luffy.png"}]},
    "ENTJ": {"desc": "지도력이 뛰어나고 목표 지향적입니다.", "chars": [{"name": "Donquixote Doflamingo", "anime": "One Piece", "why": "강력한 카리스마와 리더십을 보입니다.", "img": "https://upload.wikimedia.org/wikipedia/en/0/0e/Donquixote_Doflamingo.png"}]},
    "ISTP": {"desc": "실용적이고 문제 해결에 능숙합니다.", "chars": [{"name": "Roronoa Zoro", "anime": "One Piece", "why": "침착하고 강인한 해결사입니다.", "img": "https://upload.wikimedia.org/wikipedia/en/6/6f/Roronoa_Zoro.png"}]}
}

mbti_list = sorted(MBTI_DB.keys())
selected = st.selectbox("MBTI를 선택해 주세요", ["선택 없음"] + mbti_list)

if selected != "선택 없음":
    data = MBTI_DB[selected]
    st.subheader(f"{selected} — 성격 요약")
    st.write(data["desc"])
    st.markdown("---")
    st.subheader("추천 캐릭터")

    for c in data["chars"]:
        st.image(c["img"], width=200, caption=f"{c['name']} — {c['anime']}")
        st.write(f"이유: {c['why']}")
        st.markdown("---")

    if st.button("랜덤 추천 받기 🎲"):
        pick = random.choice(data["chars"])
        st.success(f"추천: {pick['name']} ({pick['anime']}) — {pick['why']}")
        st.image(pick["img"], width=200, caption=f"{pick['name']} — {pick['anime']}")
else:
    st.info("MBTI를 선택하시면 원피스 캐릭터를 추천해 드립니다.")
