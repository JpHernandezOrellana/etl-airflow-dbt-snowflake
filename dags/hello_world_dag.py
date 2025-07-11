from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


def print_hello():
    print("Hola, Airflow funciona correctamente!")
    
    
#Definir los argumentos por defecto del DAG
default_args = {
    'owner': 'juan_hernandez',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

#Crear el DAG

with DAG(
    dag_id = 'hello_world_dag',
    default_args = default_args,
    description = 'Un DAG simple que imprime un mensaje de saludo',
    schedule_interval = '@daily',
    start_date = datetime(2025, 7, 10),
    catchup = False,
    tags=['prueba'],
) as dag:
    
    tarea_saludo = PythonOperator(
        task_id='imprimir_hola',
        python_callable=print_hello,   
    ) 