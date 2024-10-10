select *
from {{ ref('../../data/cleaned_telegram_data') }}
where name is null;