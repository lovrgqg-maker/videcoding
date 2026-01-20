import streamlit as st
from pathlib import Path

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="자기소개 | Profile",
    page_icon="👋",
    layout="wide",
)

# -----------------------------
# Minimal Styling
# -----------------------------
st.markdown(
    """
    <style>
      .wrap {
        max-width: 980px;
        margin: 0 auto;
        padding-top: 1.2rem;
      }
      .card {
        border: 1px solid rgba(49, 51, 63, 0.2);
        border-radius: 16px;
        padding: 22px;
        background: rgba(255, 255, 255, 0.02);
      }
      .title {
        font-size: 2.0rem;
        font-weight: 800;
        margin-bottom: 0.25rem;
        line-height: 1.2;
      }
      .subtitle {
        font-size: 1.05rem;
        opacity: 0.85;
        margin-bottom: 1.2rem;
      }
      .pill {
        display: inline-block;
        padding: 6px 10px;
        border-radius: 999px;
        border: 1px solid rgba(49, 51, 63, 0.25);
        margin-right: 8px;
        margin-bottom: 8px;
        font-size: 0.9rem;
      }
      .small {
        font-size: 0.95rem;
        opacity: 0.9;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Content (Edit here)
# -----------------------------
NAME = "김무원"
ROLE = "환경/데이터 기반 문제 해결에 관심 있는 직장인"
GREETING = "안녕하세요! 제 프로필 페이지에 오신 것을 환영합니다."
ABOUT = (
    "저는 지속가능성, 환경정책, 데이터 분석에 관심이 많습니다. "
    "새로운 아이디어를 실험하고, 실무에 적용 가능한 형태로 정리하는 것을 좋아합니다."
)

TAGS = ["Sustainability", "환경정책", "데이터 분석", "업무 자동화", "콘텐츠 제작"]

# 원하는 링크로 바꾸세요
LINKS = {
    "LinkedIn": "https://www.linkedin.com/in/muwon-kim-6aa964250/",
    "Blog": "https://blog.naver.com/env_yuelpapa",
    "Email": "lovrgqg@gmail.com",
}

# -----------------------------
# Main Layout
# -----------------------------
st.markdown('<div class="wrap">', unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="card">
      <div class="title">👋 {NAME}</div>
      <div class="subtitle">{ROLE}</div>
      <div class="small">{GREETING}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    img_path = Path("C:\김무원\부업\블로그\사진")
    if img_path.exists():
        st.image(str(img_path), caption="Profile Photo", use_container_width=True)
    else:
        st.warning("assets/profile.jpg 파일을 추가하면 사진이 표시됩니다.")

with col2:
    st.markdown(
        """
        <div class="card">
          <h3 style="margin-top:0;">소개</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write(ABOUT)

    st.write("")
    st.markdown("**관심 분야**")
    tag_html = "".join([f'<span class="pill">{t}</span>' for t in TAGS])
    st.markdown(tag_html, unsafe_allow_html=True)

    st.write("")
    st.markdown("**링크**")
    link_cols = st.columns(4)
    for i, (label, url) in enumerate(LINKS.items()):
        with link_cols[i % 4]:
            st.link_button(label, url)

st.write("")
st.markdown(
    """
    <div class="card">
      <h3 style="margin-top:0;">짧은 한 줄</h3>
      <div class="small">“작게 실험하고, 빠르게 배우고, 꾸준히 개선합니다.”</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Footer
# -----------------------------
st.write("")
st.caption("© 2026 | Built with Streamlit")
