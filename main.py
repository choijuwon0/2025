import streamlit as st
import random
import requests
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="MBTI × 애니캐릭터 추천", layout="centered")

st.title("MBTI로 어울리는 애니메이션 캐릭터 찾기 🧠✨")
st.write("원하는 MBTI를 선택하면 그 성격과 어울리는 애니 캐릭터들을 보여줍니다. 추천은 대중적인 해석과 팬덤에서 자주 연관되는 인물들을 기반으로 합니다.")

# MBTI 데이터: 설명(한국어) + 추천 캐릭터 리스트
MBTI_DB = {
    "INTJ": {
        "desc": "전략적이고 독립적이며 큰 그림을 보는 성향. 계획을 세우고 목표를 향해 침착하게 나아갑니다.",
        "chars": [
            {"name": "루루슈 비 브리타니아", "anime": "Code Geass", "why": "냉철한 전략가, 목표를 위해 계산적으로 움직임."},
            {"name": "라이토 야가미", "anime": "Death Note", "why": "지적이고 목표 지향적이며 목적을 위해 계획을 세움."}
        ]
    },
    "INTP": {
        "desc": "호기심이 많고 독창적인 사고를 즐기는 유형. 이론과 원리를 파고드는 걸 좋아합니다.",
        "chars": [
            {"name": "레이먼드", "anime": "(예시)", "why": "논리적 사고와 관찰력이 뛰어남."},
            {"name": "츠키시마 켄마", "anime": "하이큐!!", "why": "내향적이고 관찰력 좋은 타입."}
        ]
    },
    "ENTJ": {
        "desc": "리더십이 강하고 목표 달성에 집중하는 타입. 조직을 이끄는 데 능숙합니다.",
        "chars": [
            {"name": "에르윈 스미스", "anime": "진격의 거인", "why": "리더십과 전략 수립 능력."},
            {"name": "토키오", "anime": "(예시)", "why": "결단력 있는 지도자형."}
        ]
    },
    "ENFJ": {
        "desc": "타인을 이끄는 카리스마와 공감을 바탕으로 사람들을 잘 챙기는 유형입니다.",
        "chars": [
            {"name": "이즈쿠 미도리야", "anime": "My Hero Academia", "why": "다른 사람을 돕고 이끄는 이상주의자."},
            {"name": "나미", "anime": "원피스", "why": "동료를 위한 헌신과 리더십."}
        ]
    },
    "INFP": {
        "desc": "이상주의적이고 감성적이며 자신만의 가치관을 중요시합니다. 창의성도 풍부합니다.",
        "chars": [
            {"name": "토오루 오카자키", "anime": "(예시)", "why": "내면의 가치와 감성에 충실한 성격."},
            {"name": "카구야 신노미야", "anime": "카구야님은 못말려!", "why": "자신의 감정을 섬세하게 숨김—내향적 낭만주의자."}
        ]
    },
    "ENFP": {
        "desc": "열정적이고 창의적이며 사람 만나는 걸 즐기는 타입. 가능성을 보는 성향이 강합니다.",
        "chars": [
            {"name": "요츠야", "anime": "(예시)", "why": "에너지 넘치고 사람을 끌어당김."},
            {"name": "나츠 도라그닐", "anime": "페어리 테일", "why": "모험심과 강한 열정."}
        ]
    },
    "ISTJ": {
        "desc": "책임감 있고 현실적이며 규칙과 전통을 중시하는 유형입니다.",
        "chars": [
            {"name": "히나츠키 케이스케", "anime": "(예시)", "why": "성실하고 원칙을 중시."},
            {"name": "카카시 하타케", "anime": "나루토", "why": "냉정하고 신뢰할 수 있는 베테랑."}
        ]
    },
    "ISFJ": {
        "desc": "다정하고 헌신적이며 타인을 돌보는 데 에너지를 쓰는 유형입니다.",
        "chars": [
            {"name": "토모에", "anime": "(예시)", "why": "타인을 잘 돌보고 세심함을 보임."}
        ]
    },
    "ISTP": {
        "desc": "실용적이고 문제 해결을 좋아하는 타입. 상황에 유연하게 대처합니다.",
        "chars": [
            {"name": "스나이퍼", "anime": "(예시)", "why": "침착하고 기술적으로 뛰어남."}
        ]
    },
    "ISFP": {
        "desc": "조용하고 관찰력이 뛰어나며 예술적 감각을 가진 타입입니다.",
        "chars": [
            {"name": "치토", "anime": "아리아", "why": "내향적이면서 감성적인 면이 강함."}
        ]
    },
    "ESTP": {
        "desc": "모험을 즐기고 행동력이 빠르며 위험을 감수하는 타입입니다.",
        "chars": [
            {"name": "조로", "anime": "원피스", "why": "행동파이고 도전적인 성향."}
        ]
    },
    "ESFP": {
        "desc": "사교적이고 현재를 즐기며 분위기 메이커 역할을 합니다.",
        "chars": [
            {"name": "우사기 츠키노 (세일러문)", "anime": "세일러문", "why": "밝고 사교적인 성격."}
        ]
    },
    "ESTJ": {
        "desc": "관리능력이 뛰어나고 체계적이며 규칙을 지키는 것을 선호합니다.",
        "chars": [
            {"name": "리바이", "anime": "진격의 거인", "why": "규율과 효율을 중시함."}
        ]
    },
    "INFJ": {
        "desc": "통찰력 있고 깊은 신념을 가진 이상주의자. 다른 사람의 잠재력을 잘 읽습니다.",
        "chars": [
            {"name": "히나타", "anime": "(예시)", "why": "조용하지만 강한 신념과 배려심."}
        ]
    },
    "HUMAN": {
        "desc": "테스트용: 실제 MBTI 중 하나를 선택하세요.",
        "chars": []
    }
}

# MBTI 선택 UI
mbti_list = sorted([k for k in MBTI_DB.keys() if k != "HUMAN"])
selected = st.selectbox("MBTI를 선택하세요", ["선택 없음"] + mbti_list)

if selected and selected != "선택 없음":
    data = MBTI_DB[selected]
    st.subheader(f"{selected} — 성격 요약")
    st.write(data["desc"])

    st.markdown("---")
    st.subheader("추천 애니메이션 캐릭터들")

    chars = data.get("chars", [])
    if not chars:
        st.info("이 MBTI에 대한 추천 캐릭터 데이터가 없습니다. 원하시면 추가해드릴게요.")
    else:
        # 캐릭터 카드 나열
        for c in chars:
            with st.expander(f"{c['name']} — {c.get('anime','(원작)')}", expanded=False):
                st.write(f"**이유:** {c.get('why','')}")

    # 무작위 추천
    if chars:
        if st.button("무작위 추천 받기 🎲"):
            pick = random.choice(chars)
            st.success(f"추천: {pick['name']} ({pick.get('anime')}) — {pick.get('why')}")

    # 결과 다운로드
    def make_text():
        lines = [f"MBTI: {selected}", f"설명: {data['desc']}", "\n추천 캐릭터:"]
        for c in chars:
            lines.append(f"- {c['name']} ({c.get('anime')}): {c.get('why')}")
        return "\n".join(lines)

    st.download_button("추천 결과 다운로드 (.txt)", make_text(), file_name=f"{selected}_recommendation.txt")

else:
    st.info("왼쪽 드롭다운에서 MBTI를 선택하면 추천 캐릭터를 보여줍니다.")

st.markdown("---")
st.caption("원하시면 캐릭터 매핑을 더 추가하거나, 이미지와 링크를 포함하는 등 앱을 확장해드릴게요.")
