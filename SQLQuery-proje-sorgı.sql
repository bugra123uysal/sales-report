SELECT * FROM train


SELECT COUNT(*) FROM train

SELECT * FROM train 
WHERE STORE IS NULL
OR Dept IS NULL
OR DATE IS NULL
OR Weekly_Sales IS NULL
OR IsHoliday IS NULL

DELETE FROM train
WHERE WEEKLY_SALES IS NULL




SELECT * FROM train 


SELECT DATE , SUM(WEEKLY_SALES) AS TOTALSUM FROM train
GROUP BY DATE
ORDER BY TOTALSUM DESC

SELECT ISHOL�DAY , SUM(Weekly_Sales) AS TOTALSUMHOL�DAY FROM train
GROUP BY IsHoliday
ORDER BY TOTALSUMHOL�DAY DESC

SELECT MAX(Weekly_Sales) AS  WEEKLY_SALESMAX  , MIN(WEEKLY_SALES) AS  WEEKLY_SALESMIN FROM train



SELECT STORE, MAX(WEEKLY_SALES) AS MAXPR�CE FROM train
GROUP BY STORE

SELECT STORE , MIN(WEEKLY_SALES) AS MINPRICE FROM train
GROUP BY Store

SELECT STORE ,SUM(WEEKLY_SALES) AS WEEKSALES FROM train
GROUP BY Store
ORDER BY WEEKSALES DESC



SELECT  MIN(Store) AS STORE , MIN(DEPT) AS DEPT , MIN(Weekly_Sales) AS WEEKSALES FROM train

SELECT  MAX(STORE) AS STORE, MAX(DEPT) AS DEPT , MAX(WEEKLY_SALES) AS WEEKSALES FROM train




 SELECT 
    YEAR(date) AS YIL,
	MONTH(date) AS AY,
	SUM(WEEKLY_SALES) AS TOTAL_SALES
FROM train
GROUP BY YEAR(date), MONTH(date)
ORDER BY YIL,AY ASC

















