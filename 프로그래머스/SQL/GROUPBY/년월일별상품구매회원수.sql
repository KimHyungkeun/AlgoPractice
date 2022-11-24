-- 코드를 입력하세요

SELECT YEAR(sales_date) as year, MONTH(sales_date) as month, gender, count(distinct(l.user_id)) as users
    FROM user_info l JOIN online_sale r
    ON l.user_id = r.user_id
    WHERE gender is not null
    GROUP BY YEAR(sales_date), MONTH(sales_date), gender
    ORDER BY year,month,gender
    
