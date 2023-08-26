FROM tiangolo/uvicorn-gunicorn-fastapi:latest

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./app /app

CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:8000",\
 "-k", "uvicorn.workers.UvicornWorker", \
 "--log-level", "info", \
 "--threads", "4" \
 ]
