# Write your MySQL query statement below


SELECT w1.Id
FROM weather w1, weather w2
WHERE w1.Temperature > w2.Temperature
AND DATEDIFF(w1.Recorddate, w2.Recorddate) = 1