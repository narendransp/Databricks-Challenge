## DAY 10 (18/01/26) – Query Optimization & Performance Tuning

Today’s focus was on **optimizing SQL performance** by understanding how queries execute and applying best practices like partitioning, Z-Ordering, and caching to improve efficiency.

---

## What I Learned Today

### Query Execution Plans

* Understanding how SQL queries are executed internally
* Identifying bottlenecks using execution plans
* Comparing optimized vs non-optimized queries

### Partitioning Strategies

* Partitioning large tables to reduce data scans
* Choosing the right partition columns
* Impact of partition pruning on query speed

### OPTIMIZE & ZORDER

* Using `OPTIMIZE` to compact small files
* Applying `ZORDER` to improve data skipping
* Enhancing performance for frequently filtered columns

### Caching Techniques

* Caching frequently accessed tables
* Reducing repeated computation
* Improving dashboard and query response time

---

## Tasks I Completed

### 1. Analyzed Query Plans

* Used query execution plans to understand performance issues
* Identified expensive operations like full table scans

### 2. Partitioned Large Tables

* Applied partitioning on large datasets
* Verified performance improvement using partition pruning

### 3. Applied OPTIMIZE & ZORDER

* Optimized Delta tables to reduce file fragmentation
* Used ZORDER on commonly filtered columns

### 4. Benchmarked Improvements

* Compared query execution time before and after optimization
* Observed noticeable performance gains

---

## Key Takeaways

* Query execution plans are critical for performance tuning
* Proper partitioning significantly reduces query cost
* OPTIMIZE and ZORDER improve read performance
* Caching boosts efficiency for repeated workloads

---

## 📸 Screenshot / Proof

![Day 10 Progress](../images/day10.png)

---

##  Hashtags

#DatabricksWithIDC
#14DaysAIChallenge
#QueryOptimization
#PerformanceTuning
#DataEngineering
#LearningInPublic
