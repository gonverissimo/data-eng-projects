
  create view "warehouse"."analytics"."vendas_raw__dbt_tmp"
    
    
  as (
    select * from raw.vendas_raw
  );