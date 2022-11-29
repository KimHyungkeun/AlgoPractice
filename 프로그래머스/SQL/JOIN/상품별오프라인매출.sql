-- 코드를 입력하세요
SELECT l.product_code, SUM(l.price * sales_amount) as sales
FROM product l JOIN OFFLINE_SALE r
ON l.product_id = r.product_id
GROUP BY l.product_id
ORDER BY sales DESC, l.product_code ASC