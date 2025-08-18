import streamlit as st
from datetime import datetime, timedelta

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
    st.subheader("📊 결과")
    if score >= 8:
        st.success("✅ 건강 상태가 좋습니다! 현재 생활습관을 유지하세요.")
    elif score >= 5:
        st.warning("⚠️ 보통입니다. 생활습관을 조금 더 관리하세요.")
    else:
        st.error("🚨 건강에 주의가 필요합니다! 생활 습관을 개선하세요.")

    st.subheader("💡 개선 방안")
    if sleep_duration and sleep_duration < 7:
        st.write(f"- 수면 시간이 {sleep_duration:.1f}시간으로 부족합니다. 7시간 이상 확보하세요.")
    if meal_regular != "항상 규칙적":
        st.write("- 규칙적인 시간에 식사하도록 노력하세요.")
    if exercise == "0회":
        st.write("- 최소 주 2~3회 가벼운 운동을 권장합니다.")
    if water < 6:
        st.write("- 하루 6~8컵(3L~4L)의 물을 섭취하세요. (1컵=500ml)")
    if stress > 6:
        st.write("- 스트레스 해소를 위해 명상, 산책, 취미 활동을 시도해보세요.")
