-- 코드를 입력하세요
SELECT l.car_id
FROM car_rental_company_car l JOIN car_rental_company_rental_history r
ON l.car_id = r.car_id
WHERE l.car_type = '세단' AND month(r.start_date) = 10
GROUP BY l.car_id
ORDER BY l.car_id DESC