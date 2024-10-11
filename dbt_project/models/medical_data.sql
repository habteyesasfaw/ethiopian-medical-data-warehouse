-- models/medical_data.sql
with raw as (
    select
        id,
        date,
        channel_title,
        channel_username,
        message,
        media_path
    from {{ ref('raw_data') }}
)

select * from raw
