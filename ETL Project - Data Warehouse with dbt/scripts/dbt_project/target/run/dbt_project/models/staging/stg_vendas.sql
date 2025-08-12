
  create view "warehouse"."analytics"."stg_vendas__dbt_tmp"
    
    
  as (
    select
    id_venda,
    cast(data_venda as date) as data_venda,
    lower(trim(cliente)) as cliente,
    produto,
    cast(valor as numeric) as valor
from "warehouse"."analytics"."vendas_raw"
  );