# Data Warehouse Project (Bronze → Silver → Gold) with SQL Server

This project demonstrates a **Data Warehouse pipeline** using **SQL Server** and CSV data sources, following the **medallion architecture**:

- **Bronze (Raw Layer)**: stores raw CSV data imported directly into the `bronze` schema.  
- **Silver (Clean Layer)**: cleans and normalizes data using stored procedures, e.g., `load_crm_cust_info`. Transformations include:
  - Trimming spaces in first and last names.
  - Removing duplicates, keeping the latest record per customer.
  - Normalizing gender (`F` → `Female`, `M` → `Male`, else `n/a`).
  - Normalizing marital status (`S` → `Single`, `M` → `Married`, else `n/a`).
  - Removing records with NULL values in key columns.
- **Gold (Analytics Layer)**: a **View** (`gold.vw_dim_customer`) over the Silver layer.  
  - Columns are renamed for simplicity (`cst_firstname + cst_lastname` → `fullname`, `cst_gndr` → `gender`, `cst_material_status` → `material_status`, `cst_create_date` → `create_date`).  
  - `fullname` is the concatenation of first and last name.  
  - No additional transformations beyond Silver; just column renaming and full name aggregation.  