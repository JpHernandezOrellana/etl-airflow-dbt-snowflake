# 🛠️ ETL Pipeline con Airflow, dbt y Snowflake

Este repositorio contiene un pipeline de datos local orquestado con **Apache Airflow**, transformaciones con **dbt**, y almacenamiento en **Snowflake** como data warehouse.

## 📦 Estructura del Proyecto

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

---

## 🧱 Instalación y uso

1. **Clona el repositorio**:

```bash
git clone https://github.com/JpHernandezOrellana/etl-airflow-dbt-snowflake.git
cd etl-airflow-dbt-snowflake
Crea y activa el entorno virtual:

bash
Copiar
Editar
python3 -m venv venv_airflow
source venv_airflow/bin/activate
Instala las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Configura tu perfil dbt en ~/.dbt/profiles.yml con tus credenciales de Snowflake.

Inicializa la base de datos de Airflow (solo una vez):

bash
Copiar
Editar
airflow db init
Inicia el scheduler y el webserver:

bash
Copiar
Editar
airflow scheduler &
airflow webserver --port 8080
Accede a la interfaz de Airflow:

Navega a: http://localhost:8080

Activa y ejecuta el DAG llamado: dbt_snowflake_pipeline

📘 Documentación de dbt
Una vez ejecutado el DAG, puedes generar y visualizar la documentación de los modelos:

bash
Copiar
Editar
dbt docs serve --profiles-dir ~/.dbt --project-dir airflow_snowflake_project
Luego ve a: http://localhost:8081

