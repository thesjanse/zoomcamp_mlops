FROM jupyter/datascience-notebook

USER $NB_UID
RUN conda install --quiet --yes \
    'evidently' \
    'prefect' \
    'psycopg' && \
    conda clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

RUN jupyter nbextension install --sys-prefix --symlink --overwrite --py evidently
RUN jupyter nbextension enable evidently --py --sys-prefix

WORKDIR ${HOME}