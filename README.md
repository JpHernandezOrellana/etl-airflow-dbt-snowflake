# 🛠️ ETL Pipeline con Airflow, dbt y Snowflake

Este repositorio contiene un pipeline de datos local orquestado con **Apache Airflow**, transformaciones con **dbt**, y almacenamiento en **Snowflake** como data warehouse.

## 📦 Estructura del Proyecto

```
text
etl_airflow_dbt_snowflake/
├── airflow.cfg                 # Configuración de Airflow
├── airflow_snowflake_project/ # Proyecto dbt
├── dags/                      # DAG de Airflow con BashOperators para ejecutar dbt
├── requirements.txt           # Dependencias del entorno
├── .gitignore                 # Exclusiones del repositorio
└── venv_airflow/              # Entorno virtual (excluido del repo)
```


---

## 🚀 ¿Qué hace este proyecto?

- **Extrae, transforma y documenta datos en Snowflake** usando `dbt`.
- **Orquesta el flujo de trabajo** con Airflow de forma modular.
- **Genera documentación automática** de los modelos dbt.

---

## ⚙️ Requisitos

- Python 3.10+
- Snowflake (cuenta activa)
- Airflow 2.9+
- dbt-core 1.10+
- Entorno virtual (`venv`) para aislamiento

## Uso:

Configura tu perfil dbt (profiles.yml)

Activa y ejecuta el DAG llamado: dbt_snowflake_pipeline


Una vez ejecutado el DAG, puedes generar y visualizar la documentación de los modelos:



