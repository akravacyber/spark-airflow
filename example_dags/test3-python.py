from airflow import DAG
from airflow.decorators import task
from datetime import datetime
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from kubernetes.client import models as k8s

with DAG("test_image_pull",
         
    start_date=datetime(2024,4,4),
    access_control={'Admin': {'can_read', 'can_edit', 'can_delete'}},
    params={
        'image_to_pull' : 'python'
    },
	schedule_interval=None) as dag:

    start_pod_with_image = KubernetesPodOperator(
                        image="python",
                        cmds=["bash", "-cx"],
                        arguments=[
                                """
                                echo "hello world"
                                """
                            ],
                        labels={"sidecar.istio.io/inject": "false"},
                        name="passing-test",
                        task_id="passing-task",
                        on_finish_action="delete_pod",
                        do_xcom_push=True,
                        dag=dag
                        )

    start_pod_with_image
