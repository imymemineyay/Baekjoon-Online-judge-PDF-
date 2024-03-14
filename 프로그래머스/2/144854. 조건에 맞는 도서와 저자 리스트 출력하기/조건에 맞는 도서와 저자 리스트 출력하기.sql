-- # 2

SELECT book_id, author_name, 
    DATE_FORMAT(published_date, '%Y-%m-%d') AS published_date
FROM book JOIN author USING (author_id)
WHERE category = '경제'
ORDER BY published_date;

