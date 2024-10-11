-- models/raw_data.sql
select
    id,
    date,
    channel_title,
    channel_username,
    message,
    media_path
from public.medical_data
