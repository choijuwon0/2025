import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

st.title("🩺 건강 체크 프로그램")

st.header("1. 생활습관 입력")

# 기본 정보 입력
st.markdown("### 👤 기본 정보")
age = st.number_input("나이", min_value=1, max_value=120, value=25)
gender = st.selectbox("성별", ["남성", "여성"])

# 성별에 따른 권장 수분 섭취량
if gender == "남성":
    water_min, water_max = 2500, 3000  # 권장 2500ml
    water_text = "2500ml (≈ 5컵, 2.5L)"
else:
    water_min, water_max = 2000, 2500  # 권장 2000ml
    water_text = "2000ml (≈ 4컵, 2.0L)"

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
water_ml = st.number_input("하루 물 섭취량 (ml)", min_value=0, max_value=10000, value=2000, step=100)
water_cups = water_ml / 500
water_l = water_ml / 1000

st.markdown("### 😥 스트레스")
stress = st.slider("스트레스 정도 (0=전혀 없음, 10=매우 심함)", 0, 10, 5)


# 결과 버튼
if st.button("건강 상태 체크하기"):
    score = 0
    
    # 수면 점수
    if sleep_duration is not None:
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

    # 물 섭취 (성별 기준 적용)
    if water_min <= water_ml <= water_max:
        score += 2
    elif (water_min - 500) <= water_ml < water_min or water_max < water_ml <= (water_max + 500):
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
            f"{sleep_duration:.1f} 시간" if sleep_duration is not None else "입력 없음",
            meal_regular,
            exercise,
            f"{water_ml} ml (≈ {water_cups:.1f}컵, {water_l:.1f}L)",
            str(stress)
        ],
        "표준 정상 범위": [
            "7~9시간",
            "항상 규칙적",
            "주 3회 이상",
            water_text,   # 성별에 따라 달라짐
            "0~3 (낮을수록 좋음)"
        ]
    }
    df = pd.DataFrame(data)
    st.table(df)

    # 개선 방안 & 몸의 변화
    st.subheader("💡 개선 방안 & 기대 효과")

    if sleep_duration is not None and sleep_duration < 7:
        st.write("- **수면 부족**: 7시간 이상 자도록 노력하세요.")
        st.caption("❌ 현재: 집중력 저하, 피로 누적, 면역력 약화")
        st.caption("✅ 개선 효과: 집중력 ↑, 면역력 강화, 기분 안정")

    if meal_regular != "항상 규칙적":
        st.write("- **불규칙한 식사**: 규칙적으로 식사하세요.")
        st.caption("❌ 현재: 위장 장애, 혈당 변동, 폭식 위험")
        st.caption("✅ 개선 효과: 혈당 안정, 위산 억제, 소화 개선")

    if exercise == "0회":
        st.write("- **운동 부족**: 주 2~3회 운동하세요.")
        st.caption("❌ 현재: 근육 감소, 체지방 증가, 혈액순환 저하")
        st.caption("✅ 개선 효과: 기초대사량 ↑, 체중 관리, 심혈관 건강")

    if water_ml < water_min:
        st.write(f"- **수분 부족**: 하루 {water_text} 물을 섭취하세요.")
        st.caption("❌ 현재: 갈증, 두통, 피부 건조, 신장 기능 저하")
        st.caption("✅ 개선 효과: 체온 조절, 혈액순환 개선, 노폐물 배출")

    if stress > 6:
        st.write("- **스트레스 과다**: 명상, 산책, 취미 활동을 시도하세요.")
        st.caption("❌ 현재: 소화 불량, 불면증, 호르몬 불균형")
        st.caption("✅ 개선 효과: 코르티솔 ↓, 수면 질 ↑, 불안 완화")
