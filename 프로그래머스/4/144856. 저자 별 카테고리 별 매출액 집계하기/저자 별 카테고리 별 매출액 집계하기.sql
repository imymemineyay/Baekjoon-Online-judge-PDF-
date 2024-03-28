-- #3

SELECT a.author_id, a.author_name, b.category, 
    SUM(bs.sales * b.price) AS total_sales 
FROM author AS a JOIN book AS b USING (author_id)
    JOIN book_sales AS bs USING (book_id)
WHERE DATE_FORMAT(bs.sales_date,'%Y-%m') = '2022-01'
GROUP BY a.author_id,a.author_name, b.category
ORDER BY a.author_id, b.category DESC;