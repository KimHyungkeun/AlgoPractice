-- 코드를 입력하세요

SELECT car_id, round(date_diff / count_car_id, 1) as average_duration
FROM
(
    SELECT car_id, count(car_id) as count_car_id, sum(datediff(end_date, start_date) + 1)  as date_diff
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    GROUP BY car_id
) t
WHERE round(date_diff / count_car_id, 1) >= 7
ORDER BY average_duration DESC, car_id DESC
