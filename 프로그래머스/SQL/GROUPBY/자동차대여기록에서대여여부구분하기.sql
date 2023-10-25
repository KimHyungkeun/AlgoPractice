-- 코드를 입력하세요
SELECT car_id, 
case 
    when sum(is_rent) = 0 then '대여 가능'
    else '대여중'
end as availability
FROM
    (SELECT car_id, 
    case 
        when start_date <= '2022-10-16' and '2022-10-16' <= end_date then 1
        else 0
    end as is_rent
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    ) t
group by car_id
order by car_id desc

