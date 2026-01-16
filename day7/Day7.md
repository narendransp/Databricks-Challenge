# DAY 7 (15/01/26) – Workflows & Job Orchestration

Today’s focus was on understanding and implementing Databricks Workflows and Job Orchestration to automate end-to-end data pipelines with scheduling, task dependencies, and error handling in a production environment.

##  What I Learned Today

- **Databricks Jobs vs Notebooks**
  - Notebooks are mainly used for development and interactive analysis.
  - Databricks Jobs are used for production-grade execution, scheduling, and monitoring.

- **Multi-task Workflows**
  - Allow chaining multiple notebooks or tasks into a single pipeline.
  - Useful for building end-to-end data pipelines.

- **Parameters & Scheduling**
  - Widgets enable dynamic inputs to notebooks.
  - Jobs can be scheduled using time-based triggers.

- **Error Handling**
  - Task failures can stop dependent tasks.
  - Retry policies help improve workflow reliability.

---

## Tasks I Completed

### 1. Added Parameter Widgets
- Created input widgets using `dbutils.widgets`
- Passed parameters such as processing date and environment
- Made notebooks reusable and configurable

### 2. Created Multi-Task Job (Bronze → Silver → Gold)
- Configured a Databricks Job with three tasks:
  - **Bronze**: Raw data ingestion
  - **Silver**: Data cleaning and validation
  - **Gold**: Business-level aggregations

### 3. Set Up Dependencies
- Defined task dependencies so that:
  - Silver runs only after Bronze completes
  - Gold runs only after Silver succeeds
- Ensured proper data flow across layers

### 4. Scheduled Execution
- Scheduled the workflow for automatic execution
- Monitored job runs using logs and run history

---

## Key Takeaways

- Databricks Workflows enable end-to-end pipeline automation
- Multi-task jobs ensure structured and reliable execution
- Parameters improve notebook flexibility and reusability
- Scheduling and dependencies are critical for production pipelines

---

## Hashtags

#DatabricksWithIDC  
#14DaysAIChallenge  
#Workflows  
#JobOrchestration  
#DataEngineering  
#LearningInPublic



## 📸 Screenshot / Proof

![Day 1 Progress](../images/day7.png)

