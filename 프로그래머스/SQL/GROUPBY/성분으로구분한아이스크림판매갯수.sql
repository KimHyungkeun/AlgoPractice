-- 코드를 입력하세요
SELECT ingredient_type, sum(total_order) as total_order
FROM first_half l JOIN icecream_info r
ON l.flavor = r.flavor
GROUP BY ingredient_type
ORDER BY total_order