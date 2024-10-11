select *
from {{ ref('medical_data') }}
where name is null;