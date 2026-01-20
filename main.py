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
        roadmap=["핵심 분야 1개(예: 백엔드/ML) 선택",]()
