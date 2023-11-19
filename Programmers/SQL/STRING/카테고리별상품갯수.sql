-- 코드를 입력하세요
SELECT substr(product_code,1,2) as category, count(product_code) as products
FROM product
GROUP BY category
ORDER BY category ASC