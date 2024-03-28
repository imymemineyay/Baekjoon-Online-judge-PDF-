-- #3
WITH RECURSIVE hours(hour) AS (
SELECT 0
UNION ALL
SELECT hour+1 FROM hours WHERE hour<23),
merged_tb AS (SELECT HOUR(datetime) AS hour, COUNT(*) AS count
FROM animal_outs 
GROUP BY HOUR(datetime)
UNION
SELECT hour, 0 AS count
FROM hours
ORDER BY 1)

SELECT hour, SUM(count) AS count FROM merged_tb GROUP BY hour ORDER BY 1;