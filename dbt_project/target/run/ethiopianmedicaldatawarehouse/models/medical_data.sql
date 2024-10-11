
  
    

  create  table "EthMedHub"."public"."medical_data__dbt_tmp"
  
  
    as
  
  (
    -- models/medical_data.sql
with raw as (
    select
        id,
        date,
        channel_title,
        channel_username,
        message,
        media_path
    from "EthMedHub"."public"."raw_data"
)

select * from raw
  );
  