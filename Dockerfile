FROM apache/airflow:2.2.3-python3.8
ADD requirements.txt /usr/local/airflow/requirements.txt
USER root
RUN apt-get update && apt-get install -y git
USER airflow
RUN pip install -r /usr/local/airflow/requirements.txt