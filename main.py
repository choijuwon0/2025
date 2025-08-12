import streamlit as st
import random

st.set_page_config(page_title="MBTI × 넷플릭스 애니 캐릭터 추천", layout="centered")

st.title("MBTI로 어울리는 넷플릭스 애니메이션 캐릭터 찾기 🎬✨")
st.write("MBTI를 선택하시면 넷플릭스에서 보실 수 있는 애니메이션 캐릭터와 해당 성격이 어울리는 이유를 보여드립니다.")

MBTI_DB = {
    "ISFJ": {
        "desc": "헌신적이고 세심한 돌봄과 안정성을 중시하는 유형입니다.",
        "chars": [
            {"name": "Retsuko", "anime": "Aggretsuko", "why": "부드럽고 책임감 있는 성격입니다.", "img": "https://upload.wikimedia.org/wikipedia/en/thumb/8/89/Retsuko.png/220px-Retsuko.png"},
            {"name": "Chopper", "anime": "One Piece", "why": "다른 이의 건강과 안녕을 먼저 생각합니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/7/7b/Tony_Tony_Chopper_Anime_Pre_Timeskip_Infobox.png"}
        ]
    },
    "ISTP": {
        "desc": "행동 중심이며 문제 해결에 유연하게 대응하는 실용주의자입니다.",
        "chars": [
            {"name": "Zoro", "anime": "One Piece", "why": "침착하고 상황에 빠르게 적응합니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/3/3d/Roronoa_Zoro_Anime_Pre_Timeskip_Infobox.png"}
        ]
    },
    "ENFJ": {
        "desc": "매력적이고 타인을 이끄는 리더 유형입니다.",
        "chars": [
            {"name": "Luffy", "anime": "One Piece", "why": "강한 리더십과 긍정적인 영향력을 발휘합니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/6/6f/Monkey_D._Luffy_Anime_Pre_Timeskip_Infobox.png"}
        ]
    },
    "ESFP": {
        "desc": "사교적이고 에너지 넘치며 순간을 즐기는 타입입니다.",
        "chars": [
            {"name": "Nami", "anime": "One Piece", "why": "직관적이며 주변을 밝히는 존재입니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/0/05/Nami_Anime_Pre_Timeskip_Infobox.png"},
            {"name": "Shanks", "anime": "One Piece", "why": "자유분방하고 낙천적인 성격입니다.", "img": "https://static.wikia.nocookie.net/onepiece/images/a/a9/Shanks_Anime_Infobox.png"}
        ]
    },
    "INTP": {
        "desc": "논리적이고 분석적인 사고를 즐기는 유형입니다.",
        "chars": [
            {"name": "Fenneko", "anime": "Aggretsuko", "why": "관찰력이 뛰어나고 분석적입니다.", "img": "https://static.wikia.nocookie.net/aggretsuko/images/0/0f/Fenneko.png"}
        ]
    },
    "ENTJ": {
        "desc": "결단력 있고 효율적인 리더 유형입니다.",
        "chars": [
            {"name": "Washimi", "anime": "Aggretsuko", "why": "지혜롭고 리더십이 뛰어납니다.", "img": "https://static.wikia.nocookie.net/aggretsuko/images/0/09/Washimi.png"}
        ]
    }
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
        st.image(c["img"], width=150)
        st.write(f"**{c['name']}** — {c['anime']}")
        st.write(f"이유: {c['why']}")
        st.markdown("---")

    if st.button("무작위 추천 받기 🎲"):
        pick = random.choice(data["chars"])
        st.success(f"추천: {pick['name']} ({pick['anime']}) — {pick['why']}")
        st.image(pick["img"], width=200)

else:
    st.info("MBTI를 선택하시면 넷플릭스 애니 캐릭터를 추천해 드립니다.")
