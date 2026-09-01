# etl-local-commerce
A local ETL pipeline that processes local commerce sales data using pandas and SQLAlchemy, following a Bronze-Silver-Gold medallion architecture to move raw data into clean, query-ready datasets.

# Problem
Local commerce businesses generate scattered raw data across multiple sources (inventory, sales, city reports) and formats (.json, .xlsx, .csv). This pipeline consolidates and cleans the incoming data into a single, reliable source of truth for business reporting.

#Architecture
Bronze (raw): Raw, unprocessed data — inventario.json, sucursales.xlsx, ventas.csv.

Silver (processed): Cleaned, validated, and normalized data — datos_maestros_limpios.json.

Gold (reporting): Business-ready output with aggregated metrics — reporte_ventas_ciudad.csv.

# Stack
Language: Python 3.14.5

Data Manipulation: pandas, openpyxl

Database & ORM: PostgreSQL, SQLAlchemy, psycopg2-binary

Environment Management: python-dotenv

#Project Structure
Plaintext
etl-local-commerce/
├── data/
│   ├── raw/          # inventario.json, sucursales.xlsx, ventas.csv
│   └── processed/    # datos_maestros_limpios.json, reporte_ventas_ciudad.csv
└── src/
    ├── generar_datos.py  # Generates synthetic source data
    └── pipeline.py       # Main ETL pipeline (Bronze → Silver → Gold)
# How to Run
Clone the repo:

Bash
git clone https://github.com/Axel200322/etl-local-commerce.git
cd etl-local-commerce
Install dependencies:

Bash
pip install pandas sqlalchemy psycopg2-binary openpyxl python-dotenv
Generate synthetic source data:

Bash
python src/generar_datos.py
Run the ETL pipeline:

Bash
python src/pipeline.py

# What I'd Improve Next
Automated Orchestration & Logging: Implement Apache Airflow or Prefect to schedule execution triggers and replace basic print statements with structured logging for better pipeline observability.

Data Quality Checks: Integrate Great Expectations or custom Pydantic schemas in the Silver stage to automatically catch missing values, invalid data types, or duplicate keys before writing to PostgreSQL.

