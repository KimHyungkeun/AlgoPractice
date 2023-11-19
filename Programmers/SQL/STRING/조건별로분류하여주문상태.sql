-- 코드를 입력하세요
SELECT order_id, product_id, date_format(out_date, '%Y-%m-%d') `out_date`, 
CASE 
    WHEN out_date is null then "출고미정"
    WHEN out_date > date_format("2022-05-01", '%Y-%m-%d') then "출고대기"
    ELSE "출고완료"
END `출고여부`
FROM food_order
ORDER BY order_id