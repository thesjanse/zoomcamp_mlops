FROM python:3.7-slim

WORKDIR /usr/src/app

COPY ./mlflow/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

CMD mlflow server \
    --backend-store-uri ${BACKEND_URI} \
    --default-artifact-root ${ARTIFACT_ROOT} \
    --host 0.0.0.0