FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-chache-dir \
    fastapi==0.110.0 \
    uvicorn[standard]==0.29.0 \
    sqlalchemy==2.0.30 \
    psycopg2-binary==2.9.9 \
    python-dotenv==1.0.1 \
    passlib[bcrypt]==1.7.4 \
    python-jose==3.3.0 \
    httpx==0.27.0

COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]