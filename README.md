# ☀️☔ SafeK Summer

**외국인 여행자를 위한 실시간 날씨/안전 기반 스마트 관광 가이드 애플리케이션입니다.**

## 프로젝트 소개

한국을 방문한 외국인 관광객이 폭염, 장마 등 예측하기 어려운 극단적 기상 상황 속에서도 목적지에 안전하게 도달하고 편안하게 여행할 수 있도록 돕는 서비스입니다.
실시간 기상청 데이터, 지하철 혼잡도(Prophet AI 예측), 공공 편의시설(화장실, 안내소) 위치 정보를 종합하여 가장 안전한 추천 관광 경로를 제공합니다.

## 디렉토리(모노레포) 구조

* `docs/`: PRD (기획 문서) 및 프로젝트 관련 도큐먼트
* `backend/`: FastAPI 애플리케이션, 데이터 파이프라인, Prophet 기반 혼잡도 예측 모델
* `frontend/`: React Native (Expo) 기반 모바일 클라이언트 소스
* `data_samples/`: 증빙용 원시 데이터 및 카테고리별 정제(Cleaned) 샘플 데이터셋

## 로컬 실행 방법 (Quick Start 가이드)

1. **[Backend]** 인프라 실행: `docker-compose up -d` (PostgreSQL DB, 캐시 서버 구동)
2. **[Backend]** 서버 실행: `cd backend` 진입 후 `uvicorn app.main:app --reload`
3. **[Frontend]** 앱 실행: `cd frontend` 진입 후 패키지 설치(`npm install`) 및 실행(`npx expo start`)
