-- 코드를 입력하세요
SELECT history_id, 
CASE 
    WHEN datediff(end_date, start_date) + 1 < 7 THEN (daily_fee * (datediff(end_date, start_date) + 1)) 
    WHEN datediff(end_date, start_date) + 1 >= 7 AND datediff(end_date, start_date) + 1 < 30 THEN round((daily_fee * ((100 - (SELECT discount_rate FROM car_rental_company_discount_plan WHERE duration_type LIKE '7%' AND car_type = '트럭')) / 100)) * (datediff(end_date, start_date) + 1), 0)
    WHEN datediff(end_date, start_date) + 1 >= 30 AND datediff(end_date, start_date) + 1 < 90 THEN round((daily_fee * ((100 - (SELECT discount_rate FROM car_rental_company_discount_plan WHERE duration_type LIKE '30%' AND car_type = '트럭')) / 100)) * (datediff(end_date, start_date) + 1), 0)
    ELSE round((daily_fee * ((100 - (SELECT discount_rate FROM car_rental_company_discount_plan WHERE duration_type LIKE '90%' AND car_type = '트럭')) / 100)) * (datediff(end_date, start_date) + 1), 0)
END as fee
FROM car_rental_company_car l
JOIN car_rental_company_discount_plan c
ON l.car_type = c.car_type 
JOIN car_rental_company_rental_history r
ON l.car_id = r.car_id
WHERE c.car_type = '트럭'
GROUP BY history_id
ORDER BY fee DESC, history_id DESC