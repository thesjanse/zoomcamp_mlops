### MLFlow setup
In order to run this setup you need to do the following:
- create .env file with MINIO_ROOT_USER, MINIO_ROOT_PASSWORD, POSTGRES_USER, POSTGRES_PASSWORD and add placeholders for MINIO_ACCESS_KEY, MINIO_SECRET_KEY;
- run docker-compose up -d;
- login to minio (localhost:9001) with MINIO_ROOT_USER and MINIO_ROOT_PASSWORD;
- create a new bucket "mlflow-artifacts";
- Go to Access Keys -> Create Access Key. Here you will get MINIO_ACCESS_KEY and MINIO_SECRET_KEY. You'll need to paste them to .env file into corresponding variables.

Inspiration links:
- https://github.com/bubulmet/mlflow-postgres-minio/blob/main/README.md
- https://github.com/aganse/docker_mlflow_db/blob/master/mlflow/Dockerfile
- https://github.com/aganse/docker_mlflow_db
- https://towardsdatascience.com/deploy-mlflow-with-docker-compose-8059f16b6039

Troubleshooting links:
- https://jupyter-docker-stacks.readthedocs.io/en/latest/using/troubleshooting.html