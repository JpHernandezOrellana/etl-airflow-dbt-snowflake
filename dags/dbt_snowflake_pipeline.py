from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

# Rutas adaptadas a tu entorno local
PROJECT_DIR = '/home/jp/scripts/etl_airflow_dbt_snowflake/airflow_snowflake_project'
PROFILES_DIR = '/home/jp/.dbt'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
    dag_id='dbt_snowflake_pipeline',
    default_args=default_args,
    description='Pipeline que ejecuta comandos dbt sobre Snowflake con Airflow',
    schedule_interval='@once',  # ⚠️ Ejecuta solo una vez al dispararlo manualmente
    start_date=datetime(2024, 11, 15),
    catchup=False,
    tags=['dbt', 'snowflake', 'airflow']
) as dag:

    start = EmptyOperator(task_id='start_dag')

    with TaskGroup(group_id='dbt_tasks') as dbt_tasks:

        dbt_debug = BashOperator(
            task_id='dbt_debug',
            bash_command=f'dbt debug --profiles-dir {PROFILES_DIR} --project-dir {PROJECT_DIR}',
        )

        dbt_run = BashOperator(
            task_id='dbt_run',
            bash_command=f'dbt run --profiles-dir {PROFILES_DIR} --project-dir {PROJECT_DIR} --select models/',
        )

        dbt_test = BashOperator(
            task_id='dbt_test',
            bash_command=f'dbt test --profiles-dir {PROFILES_DIR} --project-dir {PROJECT_DIR} --select models/',
        )

        dbt_docs_generate = BashOperator(
            task_id='dbt_docs_generate',
            bash_command=f'dbt docs generate --profiles-dir {PROFILES_DIR} --project-dir {PROJECT_DIR}',
        )

        dbt_debug >> dbt_run >> dbt_test >> dbt_docs_generate

    end = EmptyOperator(task_id='end_dag')

    start >> dbt_tasks >> end
