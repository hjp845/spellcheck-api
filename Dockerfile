# Python 이미지 기반
FROM python:3.11-slim

# 필수 패키지 설치 (py-hanspell 빌드용)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 생성
WORKDIR /app

# 프로젝트 파일 복사
COPY . /app

# 의존성 설치
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 포트 설정
EXPOSE 5000

# Flask 실행
CMD ["python", "main.py"]
