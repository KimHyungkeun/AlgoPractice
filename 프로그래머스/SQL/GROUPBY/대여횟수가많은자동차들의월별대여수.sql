-- 코드를 입력하세요

SELECT month, l.car_id as car_id, count(*) as records
FROM
(
    (SELECT car_id, count(*) as counts
    FROM car_rental_company_rental_history
    WHERE MONTH(start_date) BETWEEN 8 AND 10
    GROUP BY car_id
    HAVING counts >= 5) l
    JOIN
    (SELECT MONTH(start_date) as month, car_id
    FROM car_rental_company_rental_history
    WHERE MONTH(start_date) BETWEEN 8 AND 10) r
    ON l.car_id = r.car_id
) 
GROUP BY month, car_id
ORDER BY month, car_id DESC