-- models/stg_orders.sql

SELECT
  ordernumber,
  orderdate,
  status
FROM {{ source('snowflake_staging', 'orders') }}
WHERE status = 'Shipped'

UNION ALL

SELECT
  9999 AS ordernumber,
  CURRENT_DATE() AS orderdate,
  'Shipped' AS status
