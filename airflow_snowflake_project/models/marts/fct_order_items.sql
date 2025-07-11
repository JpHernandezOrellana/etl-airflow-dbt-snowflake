{{ config(materialized='view') }}

-- fct_order_items: líneas de pedido con detalles de producto

with orders as (

    select
        ordernumber,
        orderdate,
        status
    from {{ ref('stg_orders') }}  -- solo 'Shipped'

),

order_details as (

    select
        ordernumber,
        product_id,
        quantity
    from {{ source('snowflake_staging', 'orderdetails') }}

),

joined as (

    select
        o.ordernumber,
        o.orderdate,
        o.status,
        od.product_id,
        od.quantity
    from orders o
    join order_details od on o.ordernumber = od.ordernumber

)

select * from joined
