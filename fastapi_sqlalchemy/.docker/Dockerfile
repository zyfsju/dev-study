# ---- Base python ----
FROM my-common:latest AS base
ARG ROOT_PATH=""
ENV ROOT_PATH=$ROOT_PATH

# ---- Dependencies ----
FROM base AS dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY sql_app/ .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
