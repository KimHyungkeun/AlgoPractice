-- 코드를 입력하세요
SELECT l.product_id , l.product_name, SUM(l.price * r.amount) as total_sales
FROM food_product l JOIN food_order r
ON l.product_id = r.product_id
WHERE r.produce_date LIKE '2022-05%'
GROUP BY l.product_id
ORDER BY total_sales DESC, l.product_id ASC