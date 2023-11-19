-- 코드를 입력하세요
SELECT round(AVG(daily_fee), 0) as average_fee
FROM car_rental_company_car
GROUP BY car_type
HAVING car_type = 'SUV'