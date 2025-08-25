import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
import time

# 페이지 기본 설정 (제목, 아이콘, 레이아웃)
st.set_page_config(page_title="건강 체크 프로그램", page_icon="🩺", layout="wide")

# CSS 스타일 적용 (배경, 카드 디자인, 강조 색상 등)
st.markdown("""
    <style>
    body {
        background: linear-gradient(120deg, #fdfbfb, #ebedee);
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 25px;
        transition: transform 0.3s ease;
    }
    .card:hover {
        transform: scale(1.01);
    }
    .highlight-red { color: #e74c3c; font-weight: bold; }
    .highlight-green { color: #27ae60; font-weight: bold; }
    .highlight-blue { color: #2980b9; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 타이틀 출력
st.markdown("<div class='title'>🩺 건강 체크 프로그램</div>", unsafe_allow_html=True)

# ---------------- 기본 정보 입력 ----------------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 👤 기본 정보")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("나이", min_value=1, max_value=120, value=25)  # 나이 입력
    with col2:
        gender = st.selectbox("성별", ["남성", "여성"])  # 성별 선택
    st.markdown("</div>", unsafe_allow_html=True)

# 성별에 따라 권장 수분 섭취량 다르게 설정
if gender == "남성":
    water_min, water_max = 2500, 3000
    water_text = "2500~3000ml (≈ 5~6컵, 2.5~3L)"
else:
    water_min, water_max = 2000, 2500
    water_text = "2000~2500ml (≈ 4~5컵, 2~2.5L)"

# ---------------- 생활 습관 입력 ----------------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 📝 생활 습관 입력")
    col1, col2 = st.columns(2)
    with col1:
        sleep_start = st.time_input("🛏️ 잠든 시간", value=datetime.strptime("23:00", "%H:%M").time())  # 수면 시작 시간
        meal_regular = st.selectbox("🍚 식사 규칙성", ["항상 규칙적", "가끔 불규칙", "매우 불규칙"])  # 식사 패턴
        stress = st.slider("😥 스트레스 (0=없음, 10=심함)", 0, 10, 5)  # 스트레스 정도
    with col2:
        sleep_end = st.time_input("⏰ 일어난 시간", value=datetime.strptime("07:00", "%H:%M").time())  # 기상 시간
        exercise = st.selectbox("🏃 운동 횟수(주)", ["0회", "1~2회", "3회 이상"])  # 주간 운동 횟수
        water_ml = st.number_input("💧 하루 물 섭취량 (ml)", min_value=0, max_value=10000, value=2000, step=100)  # 하루 물 섭취량
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- 수면 시간 계산 ----------------
sleep_duration = None
if sleep_start and sleep_end:
    start_dt = datetime.combine(datetime.today(), sleep_start)
    end_dt = datetime.combine(datetime.today(), sleep_end)
    if end_dt <= start_dt:
        end_dt += timedelta(days=1)  # 자정 이후 기상 고려
    sleep_duration = (end_dt - start_dt).seconds / 3600  # 수면 시간(시간 단위) 계산

# ---------------- 버튼 클릭 시 건강 상태 평가 ----------------
if st.button("📊 건강 상태 체크하기", use_container_width=True):
    score = 0  # 점수 초기화
    
    # 수면 평가
    if sleep_duration is not None:
        if 7 <= sleep_duration <= 9: score += 2
        elif 5 <= sleep_duration < 7 or 9 < sleep_duration <= 10: score += 1
    
    # 식사 평가
    if meal_regular == "항상 규칙적": score += 2
    elif meal_regular == "가끔 불규칙": score += 1
    
    # 운동 평가
    if exercise == "3회 이상": score += 2
    elif exercise == "1~2회": score += 1
    
    # 수분 섭취 평가
    if water_min <= water_ml <= water_max: score += 2
    elif (water_min - 500) <= water_ml < water_min or water_max < water_ml <= (water_max + 500): score += 1
    
    # 스트레스 평가
    if stress <= 3: score += 2
    elif stress <= 6: score += 1

    # ---------------- 건강 상태 결과 ----------------
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📊 건강 상태 결과")

    # 프로그래스바 애니메이션 효과
    progress = st.progress(0)
    for i in range(int(score * 10)):
        time.sleep(0.02)
        progress.progress(i / 100)

    # 점수에 따른 결과 메시지
    if score >= 8:
        st.success("✅ 건강 상태가 매우 좋습니다! 🎉 현재 생활습관을 유지하세요.")
    elif score >= 5:
        st.warning("⚠️ 보통입니다. 생활습관을 조금 더 관리하세요.")
    else:
        st.error("🚨 건강에 주의가 필요합니다! 생활 습관을 개선하세요.")
    st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- 표준 수치와 비교 ----------------
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📋 표준 정상 수치와 비교")
    water_cups = water_ml / 500  # 물을 컵 단위로 환산
    water_l = water_ml / 1000    # 물을 리터 단위로 환산
    data = {
        "항목": ["수면 🛏️", "식사 🍚", "운동 🏃", "수분 💧", "스트레스 😥"],
        "내 상태": [
            f"{sleep_duration:.1f} 시간" if sleep_duration else "입력 없음",  # 실제 입력값
            meal_regular,
            exercise,
            f"{water_ml} ml (≈ {water_cups:.1f}컵, {water_l:.1f}L)",
            str(stress)
        ],
        "표준 정상 범위": [
            "7~9시간",
            "항상 규칙적",
            "주 3회 이상",
            water_text,
            "0~3 (낮을수록 좋음)"
        ]
    }
    st.table(pd.DataFrame(data))  # 비교 표 출력
    st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- 개선 방안 & 기대 효과 ----------------
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("💡 개선 방안 & 기대 효과")
    if sleep_duration and sleep_duration < 7:
        st.markdown("- 🛏️ <span class='highlight-red'>수면 부족</span>: 최소 7시간 이상 자도록 노력하세요.", unsafe_allow_html=True)
        st.caption("❌ 집중력 저하, 면역력 약화 → ✅ 집중력↑, 기분 안정, 회복력 증가")
    if meal_regular != "항상 규칙적":
        st.markdown("- 🍚 <span class='highlight-red'>불규칙한 식사</span>: 식사 시간을 일정하게 하세요.", unsafe_allow_html=True)
        st.caption("❌ 위장 장애, 혈당 변동 → ✅ 혈당 안정, 소화 개선, 에너지 유지")
    if exercise == "0회":
        st.markdown("- 🏃 <span class='highlight-red'>운동 부족</span>: 주 2~3회 운동을 추천합니다.", unsafe_allow_html=True)
        st.caption("❌ 근육 감소, 혈액순환 저하 → ✅ 체중 관리, 심혈관 건강, 활력 증가")
    if water_ml < water_min:
        st.markdown(f"- 💧 <span class='highlight-red'>수분 부족</span>: 하루 {water_text} 섭취!", unsafe_allow_html=True)
        st.caption("❌ 피부 건조, 피로감 → ✅ 체온 조절, 노폐물 배출, 집중력 개선")
    if stress > 6:
        st.markdown("- 😥 <span class='highlight-red'>스트레스 과다</span>: 명상, 산책, 취미 활동을 해보세요.", unsafe_allow_html=True)
        st.caption("❌ 불면, 소화 불량 → ✅ 수면 질↑, 불안 완화, 집중력↑")
    st.markdown("</div>", unsafe_allow_html=True)
