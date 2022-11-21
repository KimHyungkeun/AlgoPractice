-- 코드를 입력하세요
SELECT
CASE 
WHEN price BETWEEN 0 and 9999 then 0
WHEN price BETWEEN 10000 and 19999 then 10000
WHEN price BETWEEN 20000 and 29999 then 20000
WHEN price BETWEEN 30000 and 39999 then 30000
WHEN price BETWEEN 40000 and 49999 then 40000
WHEN price BETWEEN 50000 and 59999 then 50000
WHEN price BETWEEN 60000 and 69999 then 60000
WHEN price BETWEEN 70000 and 79999 then 70000
ELSE 80000
END as price_group, count(product_id) as products
FROM product
GROUP BY price_group
ORDER BY price_group


