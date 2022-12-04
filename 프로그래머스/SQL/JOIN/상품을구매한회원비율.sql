-- 코드를 입력하세요

SELECT year, month, count(user_id) as puchased_users, round((count(user_id) / (select count(*) from user_info where year(joined) = 2021)),1) as puchased_ratio 
FROM
(
    SELECT year(sales_date) as year , month(sales_date) as month, user_id
    FROM(
      SELECT r.user_id, r.sales_date
        FROM user_info l JOIN online_sale r
        ON l.user_id = r.user_id
        WHERE l.joined LIKE '2021%'
    ) a
    GROUP BY user_id, year(sales_date), month(sales_date)
) b
GROUP BY year,month
ORDER BY year,month