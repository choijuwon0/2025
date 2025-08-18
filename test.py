import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

st.title("🩺 건강 체크 프로그램")

st.header("1. 생활습관 입력")

# 수면 시간 입력
st.markdown("### 🛏️ 수면 시간")
sleep_start = st.time_input("잠든 시간", value=datetime.strptime("23:00", "%H:%M").time())
sleep_end = st.time_input("일어난 시간", value=datetime.strptime("07:00", "%H:%M").time())

# 수면 시간 계산
sleep_duration = None
if sleep_start and sleep_end:
    start_dt = datetime.combine(datetime.today(), sleep_start)
    end_dt = datetime.combine(datetime.today(), sleep_end)
    if end_dt <= start_dt:  # 자정 넘어간 경우
        end_dt += timedelta(days=1)
    sleep_duration = (end_dt - start_dt).seconds / 3600

st.markdown("### 🍚 식사")
meal_regular = st.selectbox("식사 시간을 규칙적으로 지키나요?", ["항상 규칙적", "가끔 불규칙", "매우 불규칙"])

st.markdown("### 🏃 운동")
exercise = st.selectbox("주당 운동 횟수", ["0회", "1~2회", "3회 이상"])

st.markdown("### 💧 수분 섭취")
st.caption("👉 1컵 = 500ml 기준")
water = st.number_input("하루 물 섭취량(컵)", min_value=0, max_value=20, value=5)

st.markdown("### 😥 스트레스")
stress = st.slider("스트레스 정도 (0=전혀 없음, 10=매우 심함)", 0, 10, 5)


# 결과 버튼
if st.button("건강 상태 체크하기"):
    score = 0
    
    # 수면 점수
    if sleep_duration:
        if 7 <= sleep_duration <= 9:
            score += 2
        elif 5 <= sleep_duration < 7 or 9 < sleep_duration <= 10:
            score += 1
    
    # 식사
    if meal_regular == "항상 규칙적":
        score += 2
    elif meal_regular == "가끔 불규칙":
        score += 1

    # 운동
    if exercise == "3회 이상":
        score += 2
    elif exercise == "1~2회":
        score += 1

    # 물 섭취
    if 6 <= water <= 8:
        score += 2
    elif 4 <= water < 6 or 8 < water <= 10:
        score += 1

    # 스트레스
    if stress <= 3:
        score += 2
    elif stress <= 6:
        score += 1

    # 결과 출력
    st.subheader("📊 건강 상태 결과")
    if score >= 8:
        st.success("✅ 건강 상태가 좋습니다! 현재 생활습관을 유지하세요.")
    elif score >= 5:
        st.warning("⚠️ 보통입니다. 생활습관을 조금 더 관리하세요.")
    else:
        st.error("🚨 건강에 주의가 필요합니다! 생활 습관을 개선하세요.")

    # 표준 정상 수치 비교표
    st.subheader("📋 표준 정상 수치와 비교")
    data = {
        "항목": ["수면", "식사", "운동", "수분 섭취", "스트레스"],
        "내 상태": [
            f"{sleep_duration:.1f} 시간" if sleep_duration else "입력 없음",
            meal_regular,
            exercise,
            f"{water} 컵 (≈ {water*0.5:.1f} L)",
            str(stress)
        ],
        "표준 정상 범위": [
            "7~9시간",
            "항상 규칙적",
            "주 3회 이상",
            "6~8컵 (3~4L)",
            "0~3 (낮을수록 좋음)"
        ]
    }
    df = pd.DataFrame(data)
    st.table(df)

    # 개선 방안 및 효과
    st.subheader("💡 개선 방안 & 기대 효과")
    if sleep_duration and sleep_duration < 7:
        st.write("- **수면 부족**: 7시간 이상 자도록 노력하세요. 👉 집중력 향상, 면역력 강화")
    if meal_regular != "항상 규칙적":
        st.write("- **불규칙한 식사**: 규칙적으로 식사하세요. 👉 소화기 건강, 혈당 안정")
    if exercise == "0회":
        st.write("- **운동 부족**: 주 2~3회 운동하세요. 👉 체중 관리, 심혈관 건강")
    if water < 6:
        st.write("- **수분 부족**: 하루 6~8컵(3~4L) 물 섭취하세요. 👉 피로 감소, 피부 개선")
    if stress > 6:
        st.write("- **스트레스 과다**: 명상, 산책, 취미 활동을 시도하세요. 👉 정신 건강, 수면 질 개선")
