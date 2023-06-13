FROM jupyter/datascience-notebook

USER $NB_UID
RUN conda install --quiet --yes \
    'prefect=2.10.13' \
    'mlflow=2.3.2' \
    'xgboost' \
    'boto3' \
    'optuna' && \
    conda clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

WORKDIR ${HOME}