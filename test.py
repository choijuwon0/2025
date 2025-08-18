import streamlit as st

st.title("🩺 건강 체크 프로그램")

st.header("1. 생활습관 입력")

sleep_hours = st.number_input("어제 수면 시간(시간)", min_value=0, max_value=24, value=7)
meal_regular = st.selectbox("식사 시간을 규칙적으로 지키나요?", ["항상 규칙적", "가끔 불규칙", "매우 불규칙"])
exercise = st.selectbox("주당 운동 횟수", ["0회", "1~2회", "3회 이상"])
water = st.number_input("하루 물 섭취량(컵)", min_value=0, max_value=20, value=5)
stress = st.slider("스트레스 정도", 0, 10, 5)

if st.button("건강 상태 체크하기"):
    score = 0
    
    # 수면
    if 7 <= sleep_hours <= 9:
        score += 2
    elif 5 <= sleep_hours < 7 or 9 < sleep_hours <= 10:
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

    # 결과
    st.subheader("📊 결과")
    if score >= 8:
        st.success("✅ 건강 상태가 좋습니다! 현재 생활습관을 유지하세요.")
    elif score >= 5:
        st.warning("⚠️ 보통입니다. 생활습관을 조금 더 관리하세요.")
    else:
        st.error("🚨 건강에 주의가 필요합니다! 생활 습관을 개선하세요.")

    st.subheader("💡 개선 방안")
    if sleep_hours < 7:
        st.write("- 수면을 7시간 이상 확보하세요.")
    if meal_regular != "항상 규칙적":
        st.write("- 규칙적인 시간에 식사하도록 노력하세요.")
    if exercise == "0회":
        st.write("- 최소 주 2~3회 가벼운 운동을 권장합니다.")
    if water < 6:
        st.write("- 하루 6~8컵의 물을 섭취하세요.")
    if stress > 6:
        st.write("- 스트레스를 줄일 수 있는 명상이나 산책을 해보세요.")

