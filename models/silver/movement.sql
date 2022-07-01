
select 
    fahrtnummer as journey_number,
    fahrzeugkennung as  bus_number,
    liniennummer as line_number,
    linienname as line_name,
    produkt as  product,
    richtung as direction,
    richtungstext as destination,
    fahrtStart as start_time,
    fahrtEnde as  end_time,
    beendet as journey_finished,
    fahrweg as route,
    ts as received_time_stamp,
    version as version_of_message
from
    bronze.movement

