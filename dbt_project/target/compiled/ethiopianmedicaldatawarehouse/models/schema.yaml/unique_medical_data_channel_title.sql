
    
    

select
    channel_title as unique_field,
    count(*) as n_records

from "EthMedHub"."public"."medical_data"
where channel_title is not null
group by channel_title
having count(*) > 1


