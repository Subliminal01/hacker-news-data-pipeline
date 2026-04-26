# Hacker News End-to-End ELT Pipeline 🚀

A robust, fully automated ELT (Extract, Load, Transform) data pipeline that extracts live data from the Hacker News API, loads it into a serverless warehouse, and models it for business analytics.

## 🧠 Why I Built This
Coming from a strong foundation in Quality Assurance and software testing, my goal was to engineer a data pipeline where **data integrity** is treated as a first-class citizen. Rather than just moving data from Point A to Point B, this project demonstrates how strict QA principles can be applied to Data Engineering via automated `dbt` testing, ensuring the final analytical layer is completely trustworthy.

## 🏗️ Architecture & Tech Stack
* **Extraction (Python & REST API):** Programmatically fetches live top stories using the `requests` library.
* **Storage (DuckDB):** A serverless, hyper-optimized in-memory SQL data warehouse.
* **Transformation (dbt):** Converts raw JSON into structured Bronze, Silver, and Gold layers using pure SQL.
* **Testing & QA (dbt):** Automated schema tests to catch nulls, duplicates, and broken referential integrity.
* **Orchestration (Python):** A custom directed execution script that manages dependencies and triggers the pipeline.

## 🗂️ Data Modeling Strategy
1. **Bronze Layer:** Raw JSON landing zone.
2. **Silver Layer:** Cleaned, casted, and standardized data with unnested columns.
3. **Gold Layer:** Business-level aggregations (e.g., Top Authors by total score).

## 🚀 How to Run It Locally
1. Clone this repository.
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt` *(Note: create this file if you haven't!)*
4. Run the master orchestrator: 
   ```bash
   python run_pipeline.py