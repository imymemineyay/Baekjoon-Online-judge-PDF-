-- 코드를 작성해주세요
SELECT COUNT(id) AS count
FROM ecoli_data
WHERE ((genotype & 2) != 2) AND (genotype & 5)