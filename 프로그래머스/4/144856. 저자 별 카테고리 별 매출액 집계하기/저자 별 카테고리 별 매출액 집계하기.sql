-- #2

-- author 1 : book n : book_sales n

SELECT b.author_id, a.author_name, category, SUM(sales*price) AS total_sales
FROM book AS b
    JOIN author AS a USING (author_id)
    JOIN book_sales  AS s USING (book_id) 
WHERE DATE_FORMAT(sales_date, '%Y-%m') = '2022-01'
GROUP BY b.author_id, category
ORDER BY b.author_id, category DESC;
