-- 코드를 입력하세요
SELECT first_half.flavor
FROM first_half join icecream_info using(flavor)
where total_order > 3000 
and ingredient_type = 'fruit_based'