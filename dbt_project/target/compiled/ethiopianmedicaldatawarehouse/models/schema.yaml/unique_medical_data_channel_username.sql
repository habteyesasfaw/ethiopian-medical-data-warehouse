
    
    

select
    channel_username as unique_field,
    count(*) as n_records

from "EthMedHub"."public"."medical_data"
where channel_username is not null
group by channel_username
having count(*) > 1


