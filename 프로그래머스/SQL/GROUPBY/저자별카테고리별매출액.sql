SELECT a.author_id, author_name, category, sum(price * sales) as total_sales
FROM book b JOIN book_sales bs
ON b.book_id = bs.book_id
JOIN author a
ON b.author_id = a.author_id
WHERE YEAR(sales_date) = 2022 AND MONTH(sales_date) = 1
GROUP BY author_name, category
ORDER BY a.author_id, category DESC