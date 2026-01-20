import streamlit as st
from dataclasses import dataclass
from typing import List, Dict

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="MBTI 진로 추천 ✨🚀",
    page_icon="🧭",
    layout="wide"
)

# -----------------------------
# Fancy CSS
# -----------------------------
CUSTOM_CSS = """
<style>
/* Base background */
.stApp {
  background: radial-gradient(circle at 10% 10%, rgba(255, 0, 150, 0.18), transparent 35%),
              radial-gradient(circle at 90% 20%, rgba(0, 200, 255, 0.18), transparent 40%),
              radial-gradient(circle at 20% 90%, rgba(0, 255, 150, 0.14), transparent 45%),
              linear-gradient(135deg, #0b1020 0%, #0f1a3a 35%, #1a0f3a 70%, #0b1020 100%);
  color: #EAF0FF;
}

/* Make headers pop */
h1, h2, h3, h4 {
  letter-spacing: 0.3px;
}

/* Glass card */
.card {
  background: rgba(255, 255, 255, 0.10);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 18px;
  padding: 18px 18px 14px 18px;
  box-shadow: 0 12px 40px rgba(0,0,0,0.35);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}

/* Badge */
.badge {
  display: inline-block;
  padding: 6px 10px;
  margin-right: 8px;
  margin-bottom: 8px;
  border-radius: 999px;
  background: linear-gradient(90deg, rgba(255,255,255,0.20), rgba(255,255,255,0.08));
  border: 1px solid rgba(255,255,255,0.18);
  font-size: 0.92rem;
}

/* Gradient title */
.title {
  font-size: 3rem;
  font-weight: 900;
  background: linear-gradient(90deg, #ff4fd8, #7c4dff, #20e3ff, #49ffa6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 0.2rem;
}

.subtitle {
  opacity: 0.95;
  font-size: 1.1rem;
}

/* Button cosmetics */
div.stButton > button {
  border-radius: 14px !important;
  padding: 0.9rem 1.1rem !important;
  font-weight: 800 !important;
  border: 1px solid rgba(255,255,255,0.20) !important;
  background: linear-gradient(90deg, rgba(255,79,216,0.95), rgba(124,77,255,0.95), rgba(32,227,255,0.95)) !important;
  color: #0b1020 !important;
  box-shadow: 0 12px 30px rgba(0,0,0,0.35) !important;
}

div.stButton > button:hover {
  transform: translateY(-1px);
  filter: brightness(1.05);
}

/* Selectbox */
div[data-baseweb="select"] > div {
  border-radius: 14px;
  background: rgba(255,255,255,0.08) !important;
  border: 1px solid rgba(255,255,255,0.18) !important;
}

/* Info callout */
.callout {
  border-left: 6px solid rgba(73,255,166,0.9);
  background: rgba(73,255,166,0.10);
  padding: 12px 14px;
  border-radius: 14px;
}

/* Footer */
.footer {
  opacity: 0.75;
  font-size: 0.9rem;
  margin-top: 20px;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# -----------------------------
# Data Model
# -----------------------------
@dataclass
class CareerPack:
    emoji: str
    jobs: List[str]
    strengths: List[str]
    caution: List[str]
    roadmap: List[str]
    keywords: List[str]

# -----------------------------
# MBTI Career Data (교육용 예시)
# 실제 서비스라면: 설문/관심분야/역량 등 추가 입력을 권장
# -----------------------------
MBTI_DATA: Dict[str, CareerPack] = {
    "INTJ": CareerPack(
        emoji="🧠🗺️",
        jobs=["데이터 사이언티스트", "전략기획/PM", "R&D 엔지니어", "리서처", "퀀트 분석가"],
        strengths=["논리적 사고", "장기 전략 수립", "문제 구조화", "독립적 몰입"],
        caution=["완벽주의로 인한 속도 저하", "소통 톤이 차갑게 느껴질 수 있음"],
        roadmap=["문제 정의 → 가설 세우기", "데이터/리서치 역량 강화", "포트폴리오(프로젝트) 2~3개 제작", "발표/스토리텔링 연습"],
        keywords=["전략", "분석", "시스템", "최적화"]
    ),
    "INTP": CareerPack(
        emoji="🔬🧩",
        jobs=["소프트웨어 엔지니어", "AI/ML 엔지니어", "연구원", "보안/아키텍트", "기술 컨설턴트"],
        strengths=["호기심", "개념화 능력", "창의적 문제 해결", "깊이 있는 탐구"],
        caution=["마무리/일정 관리 어려움", "실행보다 탐구에 오래 머무름"],
        roadmap=["핵심 분야 1개(예: 백엔드/ML) 선택", "기초 이론 + 실습 병행", "작은 제품을 끝까지 출시", "커뮤니티/오픈소스 참여"],
        keywords=["탐구", "이론", "구현", "실험"]
    ),
    "ENTJ": CareerPack(
        emoji="👑📈",
        jobs=["사업개발", "프로덕트 매니저", "경영/전략 컨설턴트", "세일즈 리더", "운영 총괄"],
        strengths=["리더십", "의사결정", "목표 달성", "조직/자원 운영"],
        caution=["속도 우선으로 공감이 부족해 보일 수 있음", "과도한 통제"],
        roadmap=["리더십/커뮤니케이션 스킬업", "KPI 설계/데이터 기반 운영", "실전 프로젝트(동아리/인턴)", "협상/세일즈 기본기"],
        keywords=["리더십", "성과", "전략", "운영"]
    ),
    "ENTP": CareerPack(
        emoji="⚡🎤",
        jobs=["창업가", "마케팅/브랜딩", "기획자", "콘텐츠 크리에이터", "신사업 PM"],
        strengths=["아이디어 폭발", "설득/커뮤니케이션", "변화 적응", "네트워킹"],
        caution=["디테일/루틴 관리 취약", "한 번에 너무 많은 프로젝트"],
        roadmap=["아이디어를 MVP로 만들기", "실험(AB 테스트) 습관화", "브랜딩/카피라이팅", "주 1회 회고로 우선순위 재정렬"],
        keywords=["아이디어", "실험", "확장", "설득"]
    ),
    "INFJ": CareerPack(
        emoji="🌙🕊️",
        jobs=["상담사", "교육기획자", "HRD/인재개발", "콘텐츠 에디터", "사회혁신/NGO"],
        strengths=["공감", "가치 지향", "통찰", "깊은 관계 형성"],
        caution=["감정 소진", "갈등 회피로 의사표현 지연"],
        roadmap=["상담/교육 관련 기초학습", "관찰·기록(저널링)", "프로그램 설계 프로젝트", "번아웃 방지 루틴(경계 설정)"],
        keywords=["공감", "성장", "가치", "교육"]
    ),
    "INFP": CareerPack(
        emoji="🎨🌿",
        jobs=["작가/에디터", "UX 라이터", "디자이너", "브랜딩", "심리/코칭 분야"],
        strengths=["창의성", "의미/가치 추구", "진정성", "풍부한 상상력"],
        caution=["현실적 제약에 쉽게 지침", "완성보다 영감에 의존"],
        roadmap=["매일 30분 창작 루틴", "작은 결과물 공개(블로그/포폴)", "피드백 수용 훈련", "수익화 모델(프리랜스/제품) 이해"],
        keywords=["창작", "스토리", "감성", "브랜드"]
    ),
    "ENFJ": CareerPack(
        emoji="🌟🤝",
        jobs=["교사/강사", "HR/리쿠르터", "커뮤니티 매니저", "CS/고객성공", "조직문화 담당"],
        strengths=["사람을 성장시키는 능력", "팀 빌딩", "동기부여", "커뮤니케이션"],
        caution=["타인 기대에 과몰입", "자기 시간 부족"],
        roadmap=["퍼실리테이션/코칭 기법 학습", "발표/강의 경험 쌓기", "커뮤니티 운영 프로젝트", "자기 경계 설정"],
        keywords=["코칭", "커뮤니티", "성장", "협업"]
    ),
    "ENFP": CareerPack(
        emoji="🎉🔥",
        jobs=["마케터", "콘텐츠/미디어", "서비스 기획", "브랜드 매니저", "교육/워크숍 진행"],
        strengths=["에너지", "사람/아이디어 연결", "스토리텔링", "도전정신"],
        caution=["집중력 분산", "루틴/마감 스트레스"],
        roadmap=["주력 분야 1개 고정", "캠페인/콘텐츠 포트폴리오", "마감 관리(주간 계획)", "대중 앞 발표 경험"],
        keywords=["스토리", "확산", "관계", "도전"]
    ),
    "ISTJ": CareerPack(
        emoji="🧱📋",
        jobs=["회계/재무", "품질관리(QA)", "공공/행정", "데이터 관리", "프로세스 운영"],
        strengths=["성실함", "정확성", "규정/절차 준수", "꾸준함"],
        caution=["변화에 대한 스트레스", "유연성 부족으로 비칠 수 있음"],
        roadmap=["업무 프로세스 이해", "엑셀/SQL 등 실무 도구", "자격증/기초회계", "개선 제안(Kaizen) 습관"],
        keywords=["정확", "신뢰", "프로세스", "운영"]
    ),
    "ISFJ": CareerPack(
        emoji="🧸💗",
        jobs=["간호/보건", "초등/특수 교육", "HR 운영", "고객지원", "행정/사무"],
        strengths=["배려", "책임감", "지원/케어 역량", "꼼꼼함"],
        caution=["자기주장 약화", "과도한 책임감으로 피로"],
        roadmap=["서비스 마인드 + 실무 스킬", "문서/업무 자동화", "의사소통(거절/요청) 훈련", "에너지 관리"],
        keywords=["돌봄", "지원", "안정", "책임"]
    ),
    "ESTJ": CareerPack(
        emoji="🧭🏗️",
        jobs=["운영 관리자", "프로젝트 매니저", "영업관리", "생산관리", "공공조직 리더"],
        strengths=["조직화", "실행력", "규칙 설계", "성과 관리"],
        caution=["강한 표현으로 갈등", "유연성 부족"],
        roadmap=["프로젝트 관리(일정/리스크)", "리더십/피드백 훈련", "성과지표 설계", "협업 툴 숙련"],
        keywords=["실행", "관리", "성과", "운영"]
    ),
    "ESFJ": CareerPack(
        emoji="🍰🎈",
        jobs=["인사/교육", "고객경험(CX)", "이벤트/행사 기획", "영업", "서비스 매니저"],
        strengths=["관계 형성", "팀 케어", "현장 감각", "협업"],
        caution=["평가/갈등에 민감", "과잉 배려"],
        roadmap=["커뮤니케이션 스킬", "고객 여정 이해", "행사/운영 프로젝트", "데이터로 설득하는 법"],
        keywords=["관계", "서비스", "현장", "협업"]
    ),
    "ISTP": CareerPack(
        emoji="🛠️🏍️",
        jobs=["개발자", "메카트로닉스/설비", "데이터 엔지니어", "영상/편집", "현장 기술직"],
        strengths=["문제 해결", "도구 활용", "침착함", "즉흥 대응"],
        caution=["장기 계획/문서화 부족", "감정 표현이 적음"],
        roadmap=["핵심 기술 스택 선택", "실전 제작(장비/코드)", "문서화 습관(노션)", "커리어 방향성 점검(분기)"],
        keywords=["기술", "현장", "실전", "효율"]
    ),
    "ISFP": CareerPack(
        emoji="🌸🎧",
        jobs=["디자이너", "사진/영상", "패션/뷰티", "공예/메이커", "UX/UI"],
        strengths=["미적 감각", "섬세함", "감성 표현", "사용자 공감"],
        caution=["자기PR 어려움", "마감 스트레스"],
        roadmap=["포트폴리오 중심 학습", "작품 공개/피드백 루프", "클라이언트 커뮤니케이션", "수익화(프리랜스/상품) 이해"],
        keywords=["감각", "표현", "사용자", "디자인"]
    ),
    "ESTP": CareerPack(
        emoji="🏄‍♂️💥",
        jobs=["영업", "트레이더/세일즈", "이벤트/현장 기획", "퍼포먼스 마케팅", "스포츠/코칭"],
        strengths=["행동력", "현장 적응", "대담함", "순발력"],
        caution=["충동적 의사결정", "장기 프로젝트 지루함"],
        roadmap=["실전 경험(현장/세일즈)", "데이터 기반 의사결정", "리스크 관리", "장기 목표를 짧은 스프린트로 쪼개기"],
        keywords=["현장", "속도", "도전", "성과"]
    ),
    "ESFP": CareerPack(
        emoji="🎭💃",
        jobs=["방송/미디어", "연예/공연", "세일즈", "호스피탈리티", "크리에이터"],
        strengths=["표현력", "분위기 메이커", "대인 친화", "현장 감각"],
        caution=["계획/재무 관리 약함", "과도한 일정으로 번아웃"],
        roadmap=["무대/카메라 경험", "브랜딩(SNS)", "기초 재무/계약 상식", "루틴(수면/운동) 고정"],
        keywords=["표현", "무대", "관계", "분위기"]
    ),
}

ALL_TYPES = list(MBTI_DATA.keys())

# -----------------------------
# Header
# -----------------------------
st.markdown('<div class="title">MBTI 진로 추천 ✨🧭🚀</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">MBTI를 선택하면, 성향에 맞는 <b>직업 추천</b>과 <b>학습 로드맵</b>, <b>주의 포인트</b>까지 한 번에 제안해드립니다. 🌈📚</div>',
    unsafe_allow_html=True
)

st.write("")
left, right = st.columns([1.2, 1.0], gap="large")

# -----------------------------
# Sidebar / Controls
# -----------------------------
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("1) MBTI 선택 🎯")
    mbti = st.selectbox("당신의 MBTI는 무엇인가요? 🧩", ALL_TYPES, index=ALL_TYPES.index("INTJ"))

    st.subheader("2) 관심 분야 필터(옵션) 🧠✨")
    fields = st.multiselect(
        "관심 분야를 골라보세요 (추천을 조금 더 날카롭게!) 🔎",
        ["IT/개발 💻", "데이터/AI 🤖", "기획/PM 📌", "마케팅/브랜딩 📣", "교육/상담 🧑‍🏫", "디자인/콘텐츠 🎨", "공공/행정 🏛️", "현장/기술 🛠️"],
        default=[]
    )

    st.subheader("3) 추천 스타일 ⚙️")
    top_k = st.slider("추천 직업 개수 🎁", min_value=3, max_value=8, value=5)
    show_roadmap = st.toggle("학습 로드맵 보기 🧭", value=True)
    show_caution = st.toggle("주의 포인트 보기 ⚠️", value=True)

    run = st.button("✨ 추천 결과 보기!", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Simple field-to-job keyword heuristic (교육용)
# -----------------------------
FIELD_HINTS = {
    "IT/개발 💻": ["개발", "엔지니어", "아키텍트"],
    "데이터/AI 🤖": ["데이터", "AI", "ML", "분석", "퀀트", "리서처"],
    "기획/PM 📌": ["기획", "PM", "프로덕트", "전략", "운영"],
    "마케팅/브랜딩 📣": ["마케팅", "브랜딩", "캠페인", "콘텐츠"],
    "교육/상담 🧑‍🏫": ["상담", "교육", "강사", "HRD", "코칭"],
    "디자인/콘텐츠 🎨": ["디자이너", "영상", "에디터", "크리에이터", "UX"],
    "공공/행정 🏛️": ["공공", "행정", "품질", "QA", "회계"],
    "현장/기술 🛠️": ["현장", "설비", "기술", "메카트로닉스"],
}

def filter_jobs(jobs: List[str], selected_fields: List[str], top_k: int) -> List[str]:
    if not selected_fields:
        return jobs[:top_k]
    hints = []
    for f in selected_fields:
        hints.extend(FIELD_HINTS.get(f, []))
    scored = []
    for j in jobs:
        score = 0
        for h in hints:
            if h in j:
                score += 2
        scored.append((score, j))
    scored.sort(key=lambda x: (-x[0], x[1]))
    # If everything scores 0, just return default top_k
    if scored and scored[0][0] == 0:
        return jobs[:top_k]
    return [j for _, j in scored][:top_k]

# -----------------------------
# Result area
# -----------------------------
with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("추천 결과 🌈✨")

    if not run:
        st.markdown(
            '<div class="callout">왼쪽에서 MBTI를 선택하고 <b>“추천 결과 보기”</b> 버튼을 눌러주세요! 🧭💫</div>',
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        pack = MBTI_DATA[mbti]
        st.markdown(f"### {mbti} {pack.emoji} 타입 분석 리포트 📄✨")

        # Badges
        badges = [
            f"성향 키워드: {' · '.join(pack.keywords)} 🏷️",
            f"추천 직업 {top_k}개 🎁",
            "진로 탐색 모드 ON 🚀"
        ]
        st.markdown("".join([f'<span class="badge">{b}</span>' for b in badges]), unsafe_allow_html=True)

        # Jobs
        st.markdown("#### 💼 추천 직업 리스트")
        jobs_filtered = filter_jobs(pack.jobs, fields, top_k)
        for i, job in enumerate(jobs_filtered, 1):
            st.markdown(f"**{i}. {job}** ✨")

        # Strengths
        st.markdown("#### 🌟 강점 포인트")
        st.write(" · ".join([f"{s}" for s in pack.strengths]) + " ✅")

        # Roadmap
        if show_roadmap:
            st.markdown("#### 🧭 추천 학습 로드맵 (진로 준비 루트)")
            for step_i, step in enumerate(pack.roadmap, 1):
                st.markdown(f"{step_i}) {step} 📌")

        # Caution
        if show_caution:
            st.markdown("#### ⚠️ 주의 포인트 (성장 팁)")
            for c in pack.caution:
                st.markdown(f"- {c} 🧯")

        # Mini activity
        st.markdown("#### 📝 오늘의 진로 미션 (10분 컷)")
        st.info(
            "1) 관심 직업 1개를 고르고 🔎\n"
            "2) 그 직업의 ‘하루 업무’를 3줄로 정리하고 ✍️\n"
            "3) 필요한 역량 3가지를 체크해보세요 ✅✅✅"
        )

        st.markdown('<div class="footer">💡 교육용 참고: MBTI는 성향 탐색 도구이며, 진로 결정은 관심/역량/가치관/환경 요인을 함께 고려하는 것이 가장 좋습니다. 🌱</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Expandable: All types overview
# -----------------------------
with st.expander("🌌 전체 MBTI 직업 추천 맵 한눈에 보기 (16 타입)"):
    cols = st.columns(4, gap="medium")
    for idx, t in enumerate(ALL_TYPES):
        pack = MBTI_DATA[t]
        with cols[idx % 4]:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(f"### {t} {pack.emoji}")
            st.write("추천 직업 예시:")
            st.write(" • " + "\n • ".join(pack.jobs[:4]))
            st.markdown('</div>', unsafe_allow_html=True)
