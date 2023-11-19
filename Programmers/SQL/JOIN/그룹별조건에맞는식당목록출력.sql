-- 코드를 입력하세요

SELECT l.member_name, r.review_text, date_format(r.review_date, '%Y-%m-%d') as review_date
FROM member_profile l JOIN rest_review r
ON l.member_id = r.member_id
WHERE l.member_name IN 
(SELECT member_name
    FROM (
        SELECT l.member_name, count(l.member_name) as counts
        FROM member_profile l JOIN rest_review r
        ON l.member_id = r.member_id
        GROUP BY l.member_name
        ORDER BY counts DESC
    ) t 
    WHERE counts = (SELECT count(l.member_name) as counts
        FROM member_profile l JOIN rest_review r
        ON l.member_id = r.member_id
        GROUP BY l.member_name
        ORDER BY counts DESC LIMIT 1)
)
ORDER BY review_date, r.review_text






