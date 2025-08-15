import logging

from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

log = logging.getLogger(__name__)


default_args = {
    'owner': 'airflow',
    'start_date': days_ago(2)
}

with DAG(
    dag_id='example_dag_trigger_operator',
    default_args=default_args,
    schedule_interval=None,
    tags=['example'],
) as dag:
    
    before = BashOperator(
        task_id='before_trigger_dag',
        bash_command='echo before triggering && sleep 3',
        dag=dag,
    )

    trigger = TriggerDagRunOperator(
        task_id='trigger_kubernetes_dag',
        trigger_dag_id='example_kubernetes_operator',
        dag=dag
    )

    after = BashOperator(
        task_id='after_trigger_dag',
        bash_command='echo after triggering && sleep 3',
        dag=dag,
    )

    before >> trigger >> after
