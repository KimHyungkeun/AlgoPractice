-- 코드를 입력하세요
SELECT user_id, nickname, concat(city, ' ', street_address1, ' ',street_address2) as `전체주소`,
concat(substring(tlno, 1, 3), '-', substring(tlno, 4, 4), '-', substring(tlno, 8, 4)) as `전화번호`  
FROM (
    SELECT *, 1 as summary
    FROM used_goods_board l JOIN used_goods_user r
    ON l.writer_id = r.user_id
) t 
GROUP BY user_id
HAVING sum(summary) >= 3
ORDER BY user_id DESC
