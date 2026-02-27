-- Write your MySQL query statement below
SELECT A.Department
     , A.Employee
     , A.Salary
FROM
(SELECT R.ID       AS Id
      , R.NAME     AS Department
      , L.NAME     AS Employee
      , L.SALARY   AS Salary
  FROM Employee L
 INNER JOIN Department R ON L.DEPARTMENTID = R.ID) A
INNER JOIN
(SELECT R.ID          AS DepartmentId
     , MAX(L.SALARY) AS Salary
  FROM Employee L
 INNER JOIN Department R ON L.DEPARTMENTID = R.ID
 GROUP BY R.ID) B
 ON A.Id = B.DepartmentId AND A.Salary = B.Salary