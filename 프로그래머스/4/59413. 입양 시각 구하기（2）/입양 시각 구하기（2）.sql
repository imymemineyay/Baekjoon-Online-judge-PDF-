-- #2

WITH RECURSIVE hours (hour) AS
(
  SELECT 0 
  UNION ALL
  SELECT hour+1 FROM hours WHERE hour < 23
)


SELECT hour, COUNT(animal_id) AS count
FROM hours LEFT JOIN animal_outs ON hours.hour = HOUR(animal_outs.datetime)
GROUP BY hour
ORDER BY hour;
