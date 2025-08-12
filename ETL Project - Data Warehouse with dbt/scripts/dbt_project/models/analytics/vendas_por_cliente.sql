select
    cliente,
    count(*) as total_vendas,
    round(sum(valor), 2) as total_receita
from {{ ref('stg_vendas') }}
group by cliente
order by total_receita desc
