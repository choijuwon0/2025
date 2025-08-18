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
        "3~4컵 (1.5~2L)",
        "0~3 (낮을수록 좋음)"
    ]
}
df = pd.DataFrame(data)
st.table(df)

# 개선 방안 & 몸의 변화
st.subheader("💡 개선 방안 & 기대 효과")

if sleep_duration and sleep_duration < 7:
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

if water < 3:
    st.write("- **수분 부족**: 하루 3~4컵(1.5~2L) 물을 섭취하세요. (1컵=500ml)")
    st.caption("❌ 현재: 갈증, 두통, 피부 건조, 신장 기능 저하")
    st.caption("✅ 개선 효과: 체온 조절, 혈액순환 개선, 노폐물 배출")

if stress > 6:
    st.write("- **스트레스 과다**: 명상, 산책, 취미 활동을 시도하세요.")
    st.caption("❌ 현재: 소화 불량, 불면증, 호르몬 불균형")
    st.caption("✅ 개선 효과: 코르티솔 ↓, 수면 질 ↑, 불안 완화")
