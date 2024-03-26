-- #3

SELECT category, SUM(sales) AS total_sales
FROM book JOIN book_sales USING(book_id)
WHERE DATE_FORMAT(sales_date, '%Y-%m')='2022-01'
GROUP BY category
ORDER BY category;
