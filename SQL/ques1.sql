--#1
SELECT Department.Department_id, Department.Department_Name, COUNT(Employee.Emp_id) AS Employee_Count
FROM Department
LEFT JOIN Employee ON Department.Department_id = Employee.Department_id
GROUP BY Department.Department_id, Department.Department_Name;

--#2
SELECT Department.Department_id, Department.Department_Name, Employee.Emp_Name, MAX(Employee.Salary) AS Highest_Salary
FROM Department
INNER JOIN Employee ON Department.Department_id = Employee.Department_id
GROUP BY Department.Department_id, Department.Department_Name, Employee.Emp_Name;

--#3
SELECT Department.Department_id, Department.Department_Name, SUM(Employee.Salary) AS Total_Salary_By_Department
FROM Department
LEFT JOIN Employee ON Department.Department_id = Employee.Department_id
GROUP BY Department.Department_id, Department.Department_Name;
SELECT SUM(Salary) AS Overall_Total_Salary
FROM Employee;

--#4
SELECT SUBSTRING_INDEX(email_Address, '@', -1) AS Email_Domain, COUNT(*) AS Domain_Count
FROM Employee
GROUP BY Email_Domain;

--#5
SELECT E1.Emp_Name AS Employee_Name, E2.Emp_Name AS Manager_Name
FROM Employee E1
LEFT JOIN Employee E2 ON E1.Manager_id = E2.Emp_id;
