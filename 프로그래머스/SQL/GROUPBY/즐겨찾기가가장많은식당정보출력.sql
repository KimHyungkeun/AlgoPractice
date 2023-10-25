-- 코드를 입력하세요
SELECT food_type, rest_id, rest_name, max(favorites) as favorites
FROM 
(
    SELECT food_type, rest_id, rest_name, favorites
    FROM rest_info
    GROUP BY food_type, rest_id
    ORDER BY favorites DESC
) T
GROUP BY food_type
ORDER BY food_type DESC
# SELECT food_type, rest_id, rest_name, max(favorites)
# FROM rest_info
# GROUP BY food_type