from airflow import DAG
from datetime import timedelta
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator
from FetchTweets import Fetchtweets
from Preprocessing import clean_tweets
import os
dagpath = os.getcwd()



dag_args={
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 10, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(seconds=60)
}


with DAG('First_Dag',default_args=dag_args,schedule_interval= "0 * * * *") as dag:

    get_tweets=PythonOperator(
    task_id='fetch_tweet',
    python_callable= Fetchtweets
    )

    Preprocess=PythonOperator(
    task_id='clean_tweet',
    python_callable= clean_tweets
    )
    
    create_table=MySqlOperator(
        task_id='create_table_in_database',
        mysql_conn_id='airflow_db',
        sql='CREATE TABLE IF NOT EXIST tweets(user varchar(255),date DATE,content varchar(255))'
    )


    insert_tweets=MySqlOperator(
        task_id='insert',
        mysql_conn_id='airflow_db',
        sql="LOAD DATA INFILE f'{dagpath}/../temp/file.csv' INTO TABLE tweets FIELDS TERMANITED BY ',' LINES TERMANITED BY '\n' IGNORE 1 ROWS;"
    )



    get_tweets>>Preprocess>>create_table>>insert_tweets