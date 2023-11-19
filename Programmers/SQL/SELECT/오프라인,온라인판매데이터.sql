-- 코드를 입력하세요
SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') as sales_date, product_id, user_id, sales_amount
FROM 
(
    (SELECT online_sale_id, user_id, product_id, sales_amount, sales_date FROM online_sale) 
    UNION ALL
    (SELECT offline_sale_id, NULL, product_id, sales_amount, sales_date FROM offline_sale) 
) t
WHERE SALES_DATE LIKE '2022-03-%'
ORDER BY sales_date, product_id, user_id