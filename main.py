import streamlit as st
from dataclasses import dataclass
from typing import List, Dict, Tuple
from datetime import date

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="오늘의 마음 추천 🌿",
    page_icon="🫧",
    layout="wide",
)

# -----------------------------
# Minimal Modern CSS
# -----------------------------
CSS = """
<style>
.stApp {
  background: linear-gradient(135deg, #0B1220 0%, #0E1A2E 55%, #0B1220 100%);
  color: rgba(255,255,255,0.92);
}

h1, h2, h3 {
  letter-spacing: 0.2px;
}

.small-muted {
  opacity: 0.78;
  font-size: 0.95rem;
}

.card {
  background: rgba(255,255,255,0.07);
  border: 1px solid rgba(255,255,255,0.14);
  border-radius: 18px;
  padding: 18px;
  box-shadow: 0 14px 42px rgba(0,0,0,0.35);
  backdrop-filter: blur(10px);
}

.pill {
  display: inline-block;
  padding: 6px 10px;
  border-radius: 999px;
  border: 1px solid rgba(255,255,255,0.14);
  background: rgba(255,255,255,0.06);
  font-size: 0.92rem;
  margin-right: 8px;
  margin-bottom: 8px;
}

.hr {
  height: 1px;
  background: rgba(255,255,255,0.12);
  margin: 14px 0;
  border-radius: 999px;
}

div.stButton > button {
  border-radius: 14px !important;
  padding: 0.85rem 1.1rem !important;
  font-weight: 800 !important;
  border: 1px solid rgba(255,255,255,0.18) !important;
  background: rgba(255,255,255,0.10) !important;
  color: rgba(255,255,255,0.92) !important;
}

div.stButton > button:hover {
  background: rgba(255,255,255,0.16) !important;
  transform: translateY(-1px);
}

div[data-baseweb="select"] > div {
  border-radius: 14px;
  background: rgba(255,255,255,0.06) !important;
  border: 1px solid rgba(255,255,255,0.14) !important;
}

.metric {
  font-size: 2.2rem;
  font-weight: 900;
  line-height: 1.0;
}

.metric-label {
  opacity: 0.8;
  margin-top: 6px;
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# -----------------------------
# Models
# -----------------------------
@dataclass
class Activity:
    title: str
    emoji: str
    duration: str
    intensity: str  # Low / Medium / High
    tags: List[str]
    why: str
    steps: List[str]

# -----------------------------
# Activity Library (추천 데이터)
# -----------------------------
ACTIVITIES: List[Activity] = [
    Activity(
        title="5분 호흡 리셋",
        emoji="🫁🫧",
        duration="5분",
        intensity="Low",
        tags=["불안", "스트레스", "집중"],
        why="호흡을 길게 정리하면 신체 각성이 내려가며 마음이 안정되는 데 도움이 됩니다.",
        steps=["어깨 힘 빼기 🧘", "4초 들이마시기 ⬆️", "6초 내쉬기 ⬇️", "10회 반복 🔁"]
    ),
    Activity(
        title="햇빛 산책",
        emoji="🚶‍♀️🌤️",
        duration="15~25분",
        intensity="Low",
        tags=["우울", "무기력", "리듬"],
        why="가벼운 걷기와 자연광 노출은 컨디션 회복과 기분 전환에 유리합니다.",
        steps=["신발 신고 밖으로 👟", "속도는 편하게 🙂", "주변 3가지만 관찰 👀", "돌아와 물 한 컵 💧"]
    ),
    Activity(
        title="감정 정리 저널",
        emoji="📓✍️",
        duration="10분",
        intensity="Low",
        tags=["복잡", "걱정", "정리"],
        why="생각을 글로 꺼내면 머릿속 소음이 줄고 다음 행동을 정하기 쉬워집니다.",
        steps=["지금 감정 1~2개 이름 붙이기 🏷️", "원인 추정 1줄 🔎", "내가 통제 가능한 것 1개 ✅", "오늘 할 ‘작은 행동’ 1개 📌"]
    ),
    Activity(
        title="방 정리 10분 스프린트",
        emoji="🧺⚡",
        duration="10분",
        intensity="Medium",
        tags=["무기력", "혼란", "정리"],
        why="공간을 정돈하면 통제감이 생기고 마음도 같이 정리되는 효과가 있습니다.",
        steps=["타이머 10분 ⏱️", "눈에 보이는 10개만 제자리 🧹", "쓰레기 먼저 🗑️", "끝나면 체크 ✅"]
    ),
    Activity(
        title="음악 + 스트레칭",
        emoji="🎧🤸",
        duration="8~12분",
        intensity="Low",
        tags=["피곤", "긴장", "회복"],
        why="가벼운 움직임은 긴장을 풀고 기분을 부드럽게 올립니다.",
        steps=["좋아하는 곡 2개 선택 🎶", "목/어깨 30초씩 🙆", "햄스트링 60초 🦵", "마무리 깊게 호흡 🫧"]
    ),
    Activity(
        title="집중 25분(포모도로)",
        emoji="🍅🧠",
        duration="25분",
        intensity="Medium",
        tags=["집중", "초조", "미루기"],
        why="짧은 제한 시간을 두면 시작 장벽이 낮아져 ‘착수’가 쉬워집니다.",
        steps=["할 일 1개만 고르기 🎯", "25분 타이머 ⏳", "끝나면 5분 휴식 ☕", "1회 더 가능하면 반복 🔁"]
    ),
    Activity(
        title="에너지 방출 운동",
        emoji="🏃‍♂️🔥",
        duration="12~20분",
        intensity="High",
        tags=["짜증", "분노", "답답"],
        why="높은 에너지를 안전하게 소모하면 감정의 파고가 내려가고 머리가 맑아집니다.",
        steps=["가벼운 워밍업 2분 🧘", "빠르게 걷기/가벼운 조깅 🏃", "마무리 스트레칭 2분 🤸", "물 마시기 💧"]
    ),
    Activity(
        title="따뜻한 샤워 & 티",
        emoji="🚿🍵",
        duration="15~30분",
        intensity="Low",
        tags=["스트레스", "피곤", "회복"],
        why="온열 자극은 몸을 이완시키고 수면 준비에도 도움이 됩니다.",
        steps=["따뜻한 샤워 10분 🚿", "핸드크림/로션 🧴", "카페인 없는 차 🍵", "화면 밝기 낮추기 🌙"]
    ),
]

# -----------------------------
# Scoring Logic
# -----------------------------
def mood_badges(valence: int, arousal: int) -> Tuple[str, List[str]]:
    """
    valence: -5(매우 부정) ~ +5(매우 긍정)
    arousal:  0(매우 차분) ~ 10(매우 각성)
    """
    if valence <= -2 and arousal >= 7:
        label = "불안/초조 😵‍💫"
        tags = ["불안", "스트레스", "초조", "걱정"]
    elif valence <= -2 and arousal <= 4:
        label = "우울/무기력 🌧️"
        tags = ["우울", "무기력", "회복", "리듬"]
    elif valence >= 2 and arousal >= 7:
        label = "신남/고에너지 ✨🔥"
        tags = ["집중", "도전", "성과"]
    elif valence >= 2 and arousal <= 4:
        label = "평온/만족 🌿🙂"
        tags = ["회복", "정리", "리듬"]
    else:
        label = "복합/보통 😶‍🌫️"
        tags = ["정리", "집중", "회복"]
    return label, tags

def recommend(valence: int, arousal: int, focus: str, time_cap: str, style: str) -> List[Activity]:
    label, mood_tags = mood_badges(valence, arousal)

    # 시간/강도 선호를 간단히 반영
    time_ok = {
        "짧게(5~10분) ⏱️": ["5분", "8~12분", "10분"],
        "보통(15~25분) 🕒": ["15~25분", "25분", "12~20분"],
        "여유(30분+) 🌙": ["15~30분", "25분", "15~25분"]
    }

    intensity_allow = {
        "부드럽게 🌿": ["Low", "Medium"],
        "상관없음 🎛️": ["Low", "Medium", "High"],
        "확실하게(강하게) 🔥": ["Medium", "High"]
    }

    # 기본 점수: 태그 매칭 + 감정 상태 기반 가중치
    scored = []
    for a in ACTIVITIES:
        score = 0

        # mood tags 매칭
        score += 3 * len(set(a.tags) & set(mood_tags))

        # focus 매칭
        if focus in a.tags:
            score += 5

        # 시간 제약
        if any(t in a.duration for t in time_ok.get(time_cap, [])):
            score += 2

        # 강도 선호
        if a.intensity in intensity_allow.get(style, ["Low", "Medium", "High"]):
            score += 1
        else:
            score -= 2

        # 상태별 추가 가중치
        if valence <= -2 and arousal >= 7:
            # 불안/초조 -> Low 우선
            score += 2 if a.intensity == "Low" else -1
        if valence <= -2 and arousal <= 4:
            # 무기력 -> Low/Medium + 리듬/산책/정리
            score += 2 if ("리듬" in a.tags or "정리" in a.tags) else 0
        if valence >= 2 and arousal >= 7:
            # 고에너지 -> 집중/성과 또는 운동
            score += 2 if (a.intensity in ["Medium", "High"] or "집중" in a.tags) else 0

        scored.append((score, a))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [a for _, a in scored[:5]]

# -----------------------------
# Header
# -----------------------------
st.markdown("# 오늘의 마음 추천 🌿🫧")
st.markdown(
    f"<div class='small-muted'>📅 {date.today().isoformat()} · 오늘의 감정 상태를 체크하고, 지금 나에게 맞는 활동을 추천받아보세요 🙂</div>",
    unsafe_allow_html=True
)

col_l, col_r = st.columns([1.05, 1.0], gap="large")

with col_l:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("감정 체크 ✅")

    st.markdown("**1) 기분(긍정/부정)** 🙂↔️😞")
    valence = st.slider("지금 기분은 어떤가요?", -5, 5, 0, help="부정(-) ~ 긍정(+)")

    st.markdown("**2) 각성도(에너지/긴장)** 🫨↔️🧘")
    arousal = st.slider("몸과 마음의 에너지는 어느 정도인가요?", 0, 10, 5, help="0: 매우 차분 · 10: 매우 각성")

    st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

    st.subheader("컨디션 옵션 🎛️")
    focus = st.selectbox(
        "지금 가장 필요한 것은? 🎯",
        ["회복", "집중", "정리", "불안", "무기력", "스트레스", "리듬", "짜증", "걱정", "피곤"],
        index=0
    )

    time_cap = st.selectbox(
        "가능한 시간은? ⏳",
        ["짧게(5~10분) ⏱️", "보통(15~25분) 🕒", "여유(30분+) 🌙"],
        index=1
    )

    style = st.selectbox(
        "원하는 강도는? 🌡️",
        ["부드럽게 🌿", "상관없음 🎛️", "확실하게(강하게) 🔥"],
        index=0
    )

    go = st.button("추천 받기 ✨", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_r:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("추천 결과 🎁")

    label, mood_tags = mood_badges(valence, arousal)

    st.markdown(f"<div class='metric'>{label}</div>", unsafe_allow_html=True)
    st.markdown("<div class='metric-label'>오늘의 상태 요약 🧾</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("".join([f"<span class='pill'>#{t} 🏷️</span>" for t in mood_tags]), unsafe_allow_html=True)
    st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

    if not go:
        st.markdown(
            "<div class='small-muted'>왼쪽에서 슬라이더와 옵션을 설정한 뒤, <b>추천 받기</b>를 눌러주세요 🙂✨</div>",
            unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        recs = recommend(valence, arousal, focus, time_cap, style)

        st.markdown("### 지금 추천하는 활동 TOP 5 🌟")
        for idx, a in enumerate(recs, 1):
            st.markdown(f"#### {idx}. {a.emoji} {a.title}")
        tags_html = "".join([f"<span class='pill'>#{t}</span>" for t in a.tags])

        st.markdown(
            f"<span class='pill'>⏱️ {a.duration}</span>"
            f"<span class='pill'>🌡️ {a.intensity}</span>"
            f"{tags_html}",
            )
        st.write(f"**왜 이 활동이 좋을까요?** {a.why} 🙂")
        with st.expander("바로 하기 체크리스트 ✅"):
        for s in a.steps:
        st.write(f"- {s}")
        st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

        st.info(
            "💡 팁: 추천은 ‘지금의 상태’를 기준으로 한 가이드입니다. "
            "너무 힘들거나 위험하다고 느껴지면, 휴식/주변 도움을 우선해 주세요 🫶"
        )
        st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Optional: 기록(세션 메모리) - 간단 버전
# -----------------------------
st.markdown("")

with st.expander("🗂️ 오늘 기록 남기기 (선택)"):
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    note = st.text_area("오늘의 한 줄 메모 ✍️", placeholder="예: 업무가 많아서 긴장됐지만 산책하니 조금 나아졌어 🙂")
    if st.button("저장하기 💾"):
        st.success("저장 완료! (이 예시는 세션 기반이라 새로고침하면 초기화될 수 있어요) ✅")
    st.markdown("</div>", unsafe_allow_html=True)
