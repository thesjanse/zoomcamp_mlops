FROM svizor/zoomcamp-model:mlops-3.10.0-slim

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pip install pipenv
RUN pipenv install --system --deploy

COPY ["dockerize.py", "./"]

ENTRYPOINT ["python", "dockerize.py", "2022", "04"]