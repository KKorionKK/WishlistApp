FROM python:3.11.5-alpine

EXPOSE 8000

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

RUN alembic upgrade head

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]