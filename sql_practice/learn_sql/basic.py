
SELECT *
FROM drive_test;

SELECT serial,result 
FROM drive_test;

SELECT *
FROM drive_test
WHERE result = "FAIL";

SELECT *
FROM drive_test
WHERE result = "FAIL"
AND temperature > 75;

SELECT *
FROM drive_test
WHERE machine = 'M01'
OR machine = 'M02';

SELECT *
FROM drive_test
ORDER BY temperature DESC;

SELECT COUNT(*)
FROM drive_test
WHERE result = 'FAIL';

SELECT
    machine,
    AVG(temperature) as AVG_temp
FROM drive_test
GROUP BY machine;

SELECT
    result,
    COUNT(*) AS total
FROM drive_test
GROUP BY result;

SELECT
    machine,
    AVG(temperature) AS avg_temp
FROM drive_test
GROUP BY machine
HAVING AVG(temperature) > 75;

SELECT
    machine,
    AVG(temperature) AS avg_temp
FROM drive_test
WHERE result = 'FAIL'
GROUP BY machine
HAVING AVG(temperature) > 75;