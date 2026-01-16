# DAY 8 (16/01/26) – Unity Catalog Governance

Today’s focus was on understanding and implementing **Unity Catalog Governance** in Databricks to manage data access, enforce policies, and maintain data lineage for secure and compliant data operations.

##  What I Learned Today

- **Catalog → Schema → Table hierarchy**
  - Catalogs contain schemas, which in turn contain tables.
  - Helps organize data assets in a structured way.

- **Access Control (GRANT/REVOKE)**
  - Permissions can be granted or revoked at catalog, schema, or table level.
  - Ensures secure and role-based access.

- **Data Lineage**
  - Tracks how data flows between tables, views, and pipelines.
  - Helps in auditing and understanding data dependencies.

- **Managed vs External Tables**
  - **Managed tables**: Databricks manages data and metadata.
  - **External tables**: Data resides outside Databricks, only metadata is managed.

---

## Tasks I Completed

### 1. Created Catalogs & Schemas
- Set up catalogs to organize data domains
- Created schemas under each catalog to categorize tables

### 2. Registered Delta Tables
- Registered both managed and external Delta tables
- Ensured proper metadata management for lineage tracking

### 3. Set Up Permissions
- Used `GRANT` and `REVOKE` commands to control access
- Configured roles for users and groups for secure data access

### 4. Created Views for Controlled Access
- Built views to restrict sensitive columns
- Enabled users to query data without accessing raw tables directly

---

## Key Takeaways

- Unity Catalog provides **centralized governance** over data assets  
- Access control at multiple levels improves **security and compliance**  
- Views help in enforcing **fine-grained access policies**  
- Data lineage helps in **tracking dependencies and auditing**

---

## Hashtags

#DatabricksWithIDC  
#14DaysAIChallenge  
#UnityCatalog  
#DataGovernance  
#DataEngineering  
#LearningInPublic  

---

## 📸 Screenshot / Proof

![Day 8 Progress](../images/day8.png)
