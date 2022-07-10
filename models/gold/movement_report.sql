{{ config(schema='gold') }} -- This is target custom target schema.

with daily_movement as (
    select 
        journey_number,
        bus_number,
        line_number,
        line_name,
        product,
        direction,
        destination,
        start_time,
        end_time,
        journey_finished,
        route,
        received_time_stamp,
        version_of_message
    from
       {{ source('silver', 'movement') }}
)
select
    journey_number,
    bus_number
from 
    daily_movement
