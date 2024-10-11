
    
    

select
    id as unique_field,
    count(*) as n_records

from "EthMedHub"."public"."medical_data"
where id is not null
group by id
having count(*) > 1


