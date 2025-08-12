-- Use the `ref` function to select from other models

select *
from "warehouse"."analytics"."my_first_dbt_model"
where id = 1