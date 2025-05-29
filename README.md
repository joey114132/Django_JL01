# Django 공식 튜토리얼 따라하기
---
이 프로젝트는 [Django 공식문서 튜토리얼](https://docs.djangoproject.com/ko/5.2/intro/)을 기반으로 학습 목적으로 만든 웹 애플리케이션입니다.

# 📁 프로젝트 구조
~~~python
Django_OfficialDocumentTutorial/  
├── mysite/ # Django 프로젝트 디렉토리  
├── polls/ # 튜토리얼에서 생성한 앱  
├── venv/ # (가상환경 - .gitignore에 의해 제외됨)  
├── db.sqlite3 # SQLite DB 파일  
└── .gitignore
~~~

# ⚙️ 개발 환경
	Python 3.12.3
	Django 5.2.1
	가상환경: venv 사용

# ▶️ 실행 방법
가상환경 활성화:
~~~python
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
~~~

패키지 설치:
~~~python
pip install -r requirements.txt
~~~