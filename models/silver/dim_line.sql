
{{
    config(
        materialized='incremental'
    )
}}


select 
    line_number,
    line_name,
    direction,
    destination,
    route
from
    {{ref('movement')}}
group by
    line_number,
    line_name,
    direction,
    destination,
    route
