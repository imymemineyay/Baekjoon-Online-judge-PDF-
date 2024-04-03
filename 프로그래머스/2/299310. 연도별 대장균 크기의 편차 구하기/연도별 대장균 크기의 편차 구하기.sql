-- 코드를 작성해주세요
WITH year_max AS (SELECT YEAR(differentiation_date) AS year, 
                         MAX(size_of_colony) AS max_values 
                 FROM ecoli_data
                 GROUP BY YEAR(differentiation_date)),
    ecoli_tb AS (SELECT YEAR(differentiation_date) AS year, size_of_colony, id
                 FROM ecoli_data)
                 
SELECT year, max_values-size_of_colony AS year_dev , id
FROM ecoli_tb JOIN year_max USING(year) 
ORDER BY 1, 2;

