-- 230816 재도전 시도
-- 1시간 40분 붙잡아봤는데 결국 못풀고 답 봤음
-- 출처 : https://tes-b.github.io/programmers/mysql/sql_calculate_rental_fee/
SELECT car_id, car_type, fee
FROM (SELECT c.car_id, c.car_type,
    round(daily_fee * 30 * (SELECT (100-discount_rate) * 0.01
                        FROM car_rental_company_discount_plan
                        where car_type=c.car_type AND duration_type='30일 이상')
    ) AS fee
    FROM car_rental_company_car AS c
    WHERE car_type IN ('세단', 'SUV')
    AND car_id NOT IN (SELECT car_id
                        FROM car_rental_company_rental_history
                        WHERE (start_date <= '2022-11-30 00:00:00')
                        AND (end_date >= '2022-11-01 00:00:00')
                        GROUP BY car_id)
    ) AS t
WHERE fee >= 500000 AND fee < 2000000
ORDER BY fee DESC, car_type ASC, car_id DESC