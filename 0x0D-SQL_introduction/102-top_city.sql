-- script that displays the top 3 of cities temperature during July and August
SELECT `city`, AVG(`value`) as `tmp_avg`
FROM `temperatures`
WHERE `month` = 7 or `month` = 8
GROUP BY `city`
ORDER BY `tmp_avg` DESC
LIMIT 3;
