from airflow import DAG,utils
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from os import path
from datetime import  date
from airflow.operators.dummy_operator import DummyOperator



default_args = {
    "owner": "yasin",
    "depends_on_past": False,
    "start_date": datetime(2023, 8, 1), 
    "email": ["yasinrezaei058@gmail.com"],
    "retries": 3,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG("fn-dag", default_args=default_args, schedule_interval="*/1 * * * *" , catchup=False );

fn_create_schema = BashOperator(
    task_id='fn_create_schema',
    bash_command='curl -X POST http://192.168.43.67:8080/invoke/01H6F3MV58NG8G00GZJ0000002', 
    dag=dag
)

task_dummy = DummyOperator(task_id="Dummy-Operator", dag=dag)

fn_create_schema >> task_dummy
