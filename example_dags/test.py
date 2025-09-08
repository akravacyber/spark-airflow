import logging

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

log = logging.getLogger(__name__)


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2022, 1, 1)
}

with DAG(
    dag_id='test_1_dag',
    default_args=default_args,
    schedule=None,
    tags=['example'],
) as dag:
    
    before = BashOperator(
        task_id='before_1_dag',
        bash_command='echo before triggering 1 && sleep 3',
        dag=dag,
    )

    after = BashOperator(
        task_id='after_1_dag',
        bash_command='echo after triggering 1 && sleep 3',
        dag=dag,
    )

    before >> after

with DAG(
    dag_id='test_2_dag',
    default_args=default_args,
    schedule=None,
    tags=['example'],
) as dag:
    
    before = BashOperator(
        task_id='before_2_dag',
        bash_command='echo before triggering 2 && sleep 3',
        dag=dag,
    )

    after = BashOperator(
        task_id='after_2_dag',
        bash_command='echo after triggering 2 && sleep 3',
        dag=dag,
    )

    before >> after

with DAG(
    dag_id='test_3_dag',
    default_args=default_args,
    schedule=None,
    tags=['example'],
) as dag:
    
    before = BashOperator(
        task_id='before_3_dag',
        bash_command='echo before triggering 3 && sleep 3',
        dag=dag,
    )

    after = BashOperator(
        task_id='after_2_dag',
        bash_command='echo after triggering 3 && sleep 3',
        dag=dag,
    )

    before >> after
