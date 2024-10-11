
  create view "EthMedHub"."public"."raw_data__dbt_tmp"
    
    
  as (
    -- models/raw_data.sql
select
    id,
    date,
    channel_title,
    channel_username,
    message,
    media_path
from public.medical_data
  );