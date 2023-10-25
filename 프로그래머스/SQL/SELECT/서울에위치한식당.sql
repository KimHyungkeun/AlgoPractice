-- 코드를 입력하세요
SELECT l.rest_id, l.rest_name, l.food_type, l.favorites, l.address, ROUND(AVG(r.review_score), 2) as score
FROM rest_info l JOIN rest_review r 
ON l.rest_id = r.rest_id
GROUP BY l.rest_id
HAVING address like '서울%'
ORDER BY score DESC, l.favorites DESC