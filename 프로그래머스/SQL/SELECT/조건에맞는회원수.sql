-- 코드를 입력하세요
SELECT count(user_id)
FROM user_info
WHERE YEAR(JOINED) = 2021 AND age between 20 and 29