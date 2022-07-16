{{
    config(
        materialized='incremental'
    )
}}



select 
    bus_number,
    product
from
    {{ref('movement')}}
group by
    bus_number,
    product

