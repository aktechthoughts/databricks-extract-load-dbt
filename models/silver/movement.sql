
{{ config(materialized='view') }}

select 
    * 
from
    movement

