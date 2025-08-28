-- Create the 'DataWarehouse' database
CREATE DATABASE dw;
GO

USE dw;
GO

-- Create Schemas
CREATE SCHEMA bronze;
GO

CREATE SCHEMA silver;
GO

CREATE SCHEMA gold;
GO


-- Bronze and Silver tables created

CREATE TABLE bronze.crm_cust_info (
    cst_id              INT,
    cst_key             NVARCHAR(50),
    cst_firstname       NVARCHAR(50),
    cst_lastname        NVARCHAR(50),
    cst_marital_status  NVARCHAR(50),
    cst_gndr            NVARCHAR(50),
    cst_create_date     DATE
);


CREATE TABLE silver.crm_cust_info (
    cst_id             INT,
    cst_key            NVARCHAR(50),
    cst_firstname      NVARCHAR(50),
    cst_lastname       NVARCHAR(50),
    cst_marital_status NVARCHAR(50),
    cst_gndr           NVARCHAR(50),
    cst_create_date    DATE,
    dwh_create_date    DATETIME2 DEFAULT GETDATE()
);



-- Imported via BULK INSERT

BULK INSERT bronze.crm_cust_info
FROM 'C:\dataset\cust_info.csv'
WITH (
    FIRSTROW = 2,              
    FIELDTERMINATOR = ',',    
    ROWTERMINATOR = '\n',      
    TABLOCK,
    CODEPAGE = '65001'       
);



-- SP for Silver

USE [dw]
GO
/****** Object:  StoredProcedure [silver].[load_crm_cust_info]    Script Date: 28/08/2025 20:10:46 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER   PROCEDURE [silver].[load_crm_cust_info] AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRY
        -- Trim names in Silver table to remove leading/trailing spaces
        UPDATE silver.crm_cust_info
        SET 
            cst_firstname = TRIM(cst_firstname),
            cst_lastname  = TRIM(cst_lastname);

        PRINT '>> Names trimmed in Silver table';

        -- Insert new records from Bronze table without duplicating existing Silver data
        INSERT INTO silver.crm_cust_info (
            cst_id,
            cst_key,
            cst_firstname,
            cst_lastname,
            cst_material_status,
            cst_gndr,
            cst_create_date
        )
        SELECT
            cst_id,
            cst_key,
            TRIM(cst_firstname) AS cst_firstname,
            TRIM(cst_lastname) AS cst_lastname,
            CASE 
                WHEN UPPER(TRIM(cst_material_status)) = 'S' THEN 'Single'
                WHEN UPPER(TRIM(cst_material_status)) = 'M' THEN 'Married'
                ELSE 'n/a'
            END AS cst_material_status,
            CASE
                WHEN UPPER(TRIM(cst_gndr)) = 'F' THEN 'Female'
                WHEN UPPER(TRIM(cst_gndr)) = 'M' THEN 'Male'
                ELSE 'n/a'
            END AS cst_gndr,
            cst_create_date
        FROM (
            -- Assign row numbers to remove duplicates, keeping the latest record per customer
            SELECT *,
                   ROW_NUMBER() OVER (PARTITION BY cst_id ORDER BY cst_create_date DESC) AS rn
            FROM bronze.crm_cust_info
            WHERE cst_id IS NOT NULL
        ) t
        WHERE rn = 1                          -- Keep only the latest record per customer
          AND TRIM(cst_firstname) <> ''       -- Exclude records with first name as empty spaces
          AND NOT EXISTS (
                -- Exclude records that already exist in Silver
                SELECT 1
                FROM silver.crm_cust_info s
                WHERE s.cst_id = t.cst_id
          );

        PRINT '>> New clean records inserted from Bronze';

        -- Remove any records that have NULL in any column
        DELETE FROM silver.crm_cust_info
        WHERE cst_id IS NULL
           OR cst_key IS NULL
           OR cst_firstname IS NULL
           OR cst_lastname IS NULL
           OR cst_material_status IS NULL
           OR cst_gndr IS NULL
           OR cst_create_date IS NULL;;
    END TRY
    BEGIN CATCH
        PRINT 'ERROR during Silver CRM Customer Info load: ' + ERROR_MESSAGE();
    END CATCH
END;


-- Gold View

CREATE OR ALTER VIEW gold.vw_dim_customer AS
SELECT
    CONCAT(TRIM(cst_firstname), ' ', TRIM(cst_lastname)) AS fullname,
    cst_gndr            AS gender,
    cst_material_status AS material_status,
    cst_create_date     AS create_date,
    GETDATE()           AS dwh_create_date
FROM silver.crm_cust_info
WHERE cst_id IS NOT NULL
  AND TRIM(cst_firstname) <> ''
  AND TRIM(cst_lastname) <> '';