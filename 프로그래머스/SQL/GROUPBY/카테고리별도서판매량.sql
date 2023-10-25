-- 코드를 입력하세요
SELECT category, SUM(sales) as total_sales
FROM book l JOIN book_sales r
ON l.book_id = r.book_id
WHERE YEAR(sales_date) = '2022' AND MONTH(sales_date) = '1'
GROUP BY category
ORDER BY category