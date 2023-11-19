-- 코드를 입력하세요
SELECT history_id, car_id, date_format(start_date, '%Y-%m-%d') as start_date, date_format(end_date, '%Y-%m-%d') as end_date, 
CASE 
    WHEN datediff(end_date, start_date) + 1 >= 30 THEN '장기 대여'
    ELSE '단기 대여'
END AS rent_type
FROM (
SELECT *
FROM car_rental_company_rental_history
WHERE YEAR(start_date) = 2022 AND MONTH(start_date) = 9
) t
ORDER BY history_id DESC


-- 틀린 답안
SELECT history_id, car_id, date_format(start_date, '%Y-%m-%d') as start_date, date_format(end_date, '%Y-%m-%d') as end_date, 
CASE 
    WHEN datediff(end_date, start_date) >= 30 THEN '장기 대여'
    ELSE '단기 대여'
END AS rent_type
FROM (
SELECT *
FROM car_rental_company_rental_history
WHERE YEAR(start_date) = 2022 AND MONTH(start_date) = 9
) t
ORDER BY history_id DESC