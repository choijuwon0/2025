import streamlit as st
import random

st.set_page_config(page_title="MBTI × 원피스 캐릭터 추천", layout="centered")

st.title("MBTI로 어울리는 원피스 캐릭터 찾기 ☠️✨")
st.write("MBTI를 선택하시면 원피스의 캐릭터와 해당 성격이 어울리는 이유를 보여드립니다.")

MBTI_DB = {
    "INTJ": {"desc": "전략적이며 계획적인 완벽주의자입니다.", "chars": [{"name": "Nico Robin", "anime": "One Piece", "why": "지식과 전략에 능숙합니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/3/3f/Nico_Robin_Anime_Infobox.png"}]},
    "INTP": {"desc": "분석적이며 탐구심이 많은 유형입니다.", "chars": [{"name": "Franky", "anime": "One Piece", "why": "창의적이고 기술에 대한 호기심이 큽니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/d/de/Franky_Anime_Infobox.png"}]},
    "ENTJ": {"desc": "리더십이 강하고 효율적인 전략가입니다.", "chars": [{"name": "Sakazuki (Akainu)", "anime": "One Piece", "why": "결단력과 규율이 뛰어납니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/7/7f/Sakazuki_Anime_Infobox.png"}]},
    "ENTP": {"desc": "도전적이고 창의적인 성향입니다.", "chars": [{"name": "Usopp", "anime": "One Piece", "why": "재치 있고 상황에 기민하게 대처합니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/c/c7/Usopp_Anime_Pre_Timeskip_Infobox.png"}]},
    "INFJ": {"desc": "통찰력 있고 깊은 신념을 가진 이상주의자입니다.", "chars": [{"name": "Jinbe", "anime": "One Piece", "why": "신념과 명예를 중시하며 타인을 돕습니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/5/5b/Jinbe_Anime_Infobox.png"}]},
    "INFP": {"desc": "이상주의적이며 가치관을 중시합니다.", "chars": [{"name": "Chopper", "anime": "One Piece", "why": "순수하고 동료애가 강합니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/7/7b/Tony_Tony_Chopper_Anime_Pre_Timeskip_Infobox.png"}]},
    "ENFJ": {"desc": "타인을 이끄는 카리스마 있는 리더입니다.", "chars": [{"name": "Monkey D. Luffy", "anime": "One Piece", "why": "동료를 이끄는 강한 리더십을 가졌습니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/6/6f/Monkey_D._Luffy_Anime_Pre_Timeskip_Infobox.png"}]},
    "ENFP": {"desc": "열정적이고 사교적인 모험가입니다.", "chars": [{"name": "Portgas D. Ace", "anime": "One Piece", "why": "자유롭고 열정적인 성격입니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/4/4b/Portgas_D._Ace_Anime_Infobox.png"}]},
    "ISTJ": {"desc": "책임감 있고 신뢰할 수 있는 유형입니다.", "chars": [{"name": "Fujitora", "anime": "One Piece", "why": "원칙과 정의를 지킵니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/b/b5/Issho_Anime_Infobox.png"}]},
    "ISFJ": {"desc": "헌신적이고 배려심이 깊은 유형입니다.", "chars": [{"name": "Chopper", "anime": "One Piece", "why": "다른 이의 안녕을 먼저 생각합니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/7/7b/Tony_Tony_Chopper_Anime_Pre_Timeskip_Infobox.png"}]},
    "ESTJ": {"desc": "체계적이고 결단력 있는 관리자입니다.", "chars": [{"name": "Smoker", "anime": "One Piece", "why": "질서와 규율을 중시합니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/0/0a/Smoker_Anime_Infobox.png"}]},
    "ESFJ": {"desc": "사람을 돕고 관계를 중시합니다.", "chars": [{"name": "Vivi Nefertari", "anime": "One Piece", "why": "배려심과 리더십이 돋보입니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/6/68/Nefertari_Vivi_Anime_Infobox.png"}]},
    "ISTP": {"desc": "유연하고 실용적인 문제 해결사입니다.", "chars": [{"name": "Zoro", "anime": "One Piece", "why": "침착하고 상황 판단이 빠릅니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/3/3d/Roronoa_Zoro_Anime_Pre_Timeskip_Infobox.png"}]},
    "ISFP": {"desc": "온화하며 예술적인 감각이 뛰어납니다.", "chars": [{"name": "Brook", "anime": "One Piece", "why": "유머러스하고 음악을 사랑합니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/0/0a/Brook_Anime_Infobox.png"}]},
    "ESTP": {"desc": "모험심 많고 행동력이 빠릅니다.", "chars": [{"name": "Sanji", "anime": "One Piece", "why": "결단력 있고 상황 대처가 빠릅니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/3/33/Sanji_Anime_Pre_Timeskip_Infobox.png"}]},
    "ESFP": {"desc": "에너지 넘치고 사교적인 분위기 메이커입니다.", "chars": [{"name": "Nami", "anime": "One Piece", "why": "밝고 사교적인 성격입니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/0/05/Nami_Anime_Pre_Timeskip_Infobox.png"}]}
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
        st.image(c["img"], width=200)
        st.write(f"**{c['name']}** — {c['anime']}")
        st.write(f"이유: {c['why']}")
        st.markdown("---")

    if st.button("무작위 추천 받기 🎲"):
        pick = random.choice(data["chars"])
        st.success(f"추천: {pick['name']} ({pick['anime']}) — {pick['why']}")
        st.image(pick["img"], width=200)

else:
    st.info("MBTI를 선택하시면 원피스 캐릭터를 추천해 드립니다.")
