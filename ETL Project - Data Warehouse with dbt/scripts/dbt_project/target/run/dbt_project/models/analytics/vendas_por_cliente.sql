
  create view "warehouse"."analytics"."vendas_por_cliente__dbt_tmp"
    
    
  as (
    select
    cliente,
    count(*) as total_vendas,
    round(sum(valor), 2) as total_receita
from "warehouse"."analytics"."stg_vendas"
group by cliente
order by total_receita desc
  );