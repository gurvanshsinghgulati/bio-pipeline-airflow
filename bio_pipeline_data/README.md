# Biological Data Processing ETL Pipeline with Apache Airflow 3.0

A robust, distributed data engineering pipeline built using **Apache Airflow 3.0** to automate the Extraction, Transformation, and Loading (ETL) of genomic expression metrics. The pipeline orchestrates tasks using a **CeleryExecutor** architecture backend by **Redis** as a message broker and **PostgreSQL** as the operational metadata store.

The workflow ingests raw biological dataset logs, processes the information using advanced analysis patterns, structures the metrics into a relational storage engine, and renders data visualization charts automatically.

---

## 🧬 Pipeline Architecture & Workflow

The pipeline is registered as `bio_etl_dag` and manages four sequential data engineering operations:

1. **`create_table`**: Initializes the underlying storage matrix (`gene_data.db`) inside an isolated, secure user space and structures the relational schema tables.
2. **`load_data`**: Ingests raw biological data streams (`sample_gene_expression.csv`) using `pandas` data frames and appends records directly into the database engine.
3. **`analyze_data`**: Executes internal relational query blocks to calculate group analytics and statistical means across targeted gene markers.
4. **`plot_data`**: Compiles the final parsed analytical data frame and uses `matplotlib` to render a data visualization bar chart (`gene_expression_chart.png`).

---

## 🛠️ Stack Components & Layout

- **Orchestrator**: Apache Airflow 3.0 (Standalone decoupled daemons: Scheduler, Worker, API Server, DAG Processor)
- **Executor Pattern**: CeleryExecutor
- **Message Broker**: Redis 7.2 (Permissive Bookworm Layer)
- **Metadata Database**: PostgreSQL 16
- **Data Engine**: SQLite 3 / Python 3.13 Virtual Environments
- **Primary Libraries**: `pandas`, `matplotlib`, `scikit-learn`

---

## 🚀 Deployment & Operations Guide

### 1. Project Prerequisites
Ensure your local workspace directories match the mounted volume layout structure:
```bash
mkdir -p dags logs config plugins bio_pipeline_data
```

### 2. Microservice Configuration (`.env`)
Create an `.env` file next to your `docker-compose.yaml` to securely declare connection metrics and execution variables:
```env
FERNET_KEY=NkNZd1Z4M19kM1ZaR1pXN1k5bVJ5WE5zYjNkbU5FUkM=
_PIP_ADDITIONAL_REQUIREMENTS=matplotlib pandas scikit-learn
```

### 3. Build & Initialize Cluster Infrastructure
To build the specialized virtual environment containers and launch the infrastructure services in detached mode, execute:
```bash
docker-compose down --volumes --remove-orphans
docker-compose up -d --build
```

### 4. Trigger & Verify the Execution Loop
1. Open the Airflow UI backend dashboard in your browser.
2. Navigate to the **DAGs** main dashboard index tab.
3. Click the toggle switch on the far left to turn `bio_etl_dag` **On**.
4. In the upper right corner of the workspace, click the **Play Button (Trigger DAG)**.

The task instances will automatically cascade from **Queued** ──> **Running** ──> **Success (Dark Green)**.

---

## 🛡️ Critical Troubleshooting & Infrastructure Fixes

During the deployment lifecycle of this project, several architectural hurdles were diagnosed and permanently resolved:

### 1. Unjamming Database Zombie Loops
- **Symptom**: Tasks were stuck indefinitely in the `queued` state due to a metadata database lock drop crash (`psycopg2.OperationalError: server closed the connection unexpectedly`).
- **Fix**: Executed a deep volume-prune reset (`docker-compose down -v && docker volume prune -a -f`) to drop corrupted relational transaction history logs and allow the `airflow-init` container to rebuild a flawless data tracking schema.

### 2. Resolving Scheduler Core File Blocks
- **Symptom**: The Scheduler thread froze instantly on boot-up at the `Adopting or resetting orphaned tasks...` execution step.
- **Fix**: Discovered that active SQLite binary database files (`gene_data.db`) were sitting inside the `/dags` directory, forcing the scheduler's continuous Python compilation loops to deadlock. Moved all data binaries completely outside the DAG directory to decouple file parsing from operational storage.

### 3. Overcoming Docker Directory Permission Layers (`Errno 13`)
- **Symptom**: Python scripts crashed with `PermissionError: [Errno 13] Permission denied` when attempting to write files to shared container layers.
- **Fix**: Relocated all data processing execution file paths to Airflow's native user-space home directory (`/home/airflow/`). Because the running container user account (`UID 50000`) natively owns this path, file reads/writes pass completely clear of Linux administrative blocks.

---

## 📊 Extracting the Output Visualizations

Once the final pipeline box turns dark green, you can copy the generated biological visualization straight from the runtime worker container directly onto your physical machine:

```bash
docker cp bio-pipeline-airflow-airflow-worker-1:/home/airflow/gene_expression_chart.png ./
```
