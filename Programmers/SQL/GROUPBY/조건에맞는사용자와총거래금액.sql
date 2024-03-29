-- 코드를 입력하세요
SELECT user_id, nickname, sum(price) as total_sales
FROM (
SELECT b.user_id, b.nickname, a.price FROM
used_goods_board a join used_goods_user b 
on a.writer_id = b.user_id
where a.status = 'DONE'
) t group by user_id
having total_sales >= 700000
order by total_sales

