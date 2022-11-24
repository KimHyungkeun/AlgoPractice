-- 코드를 입력하세요

SELECT category, max(price) as max_price, product_name
FROM
(
    SELECT product_id, category, product_name, price
    FROM food_product
    GROUP BY product_id, category
    ORDER BY price DESC
) T
GROUP BY category
HAVING category in ('과자','국','김치','식용유')
ORDER BY max_price DESC