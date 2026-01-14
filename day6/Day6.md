# DAY 6 (14/01/26) – Medallion Architecture

## Learnings

Today’s focus was on understanding and implementing the **Medallion Architecture**, a layered data design pattern widely used in modern data engineering platforms like Databricks and Delta Lake.

### Core Concepts
- **Bronze Layer (Raw Data)**
  - Stores raw, ingested data exactly as received
  - No transformations applied
  - Acts as a historical source of truth

- **Silver Layer (Cleaned & Refined Data)**
  - Data is cleaned, validated, and standardized
  - Handles missing values, duplicates, and schema corrections
  - Suitable for analytics and further transformations

- **Gold Layer (Business-Level Aggregates)**
  - Contains aggregated, business-ready data
  - Optimized for reporting and dashboards
  - Used directly by analysts and stakeholders

- **Incremental Processing**
  - Processes only new or changed data
  - Improves performance and reduces compute cost
  - Commonly implemented using MERGE and timestamps

---

## Tasks Completed

### 1️ Designed a 3-Layer Architecture
- Defined clear responsibilities for Bronze, Silver, and Gold layers
- Structured storage paths and naming conventions for each layer

### 2️ Built Bronze Layer (Raw Ingestion)
- Ingested raw data from source files
- Stored data in Delta format without transformations
- Preserved original schema and records

### 3️ Built Silver Layer (Cleaning & Validation)
- Removed duplicate records
- Handled NULL and invalid values
- Standardized data types and column names
- Applied basic business rules

### 4️ Built Gold Layer (Business Aggregates)
- Created aggregated metrics such as totals, averages, and counts
- Prepared datasets optimized for reporting and dashboards
- Ensured data quality and performance

---

## Key Takeaways
- Medallion Architecture improves **data quality, scalability, and maintainability**
- Separating raw, cleaned, and aggregated data simplifies debugging
- Incremental processing is essential for efficient large-scale pipelines
- Gold layer datasets should always be business-focused and optimized

---

###  Hashtags
#DatabricksWithIDC  
#14DaysAIChallenge  
#MedallionArchitecture  
#DataEngineering  
#DeltaLake  
#LearningInPublic

## 📸 Screenshot / Proof

![Day 1 Progress](../images/day6.png)

