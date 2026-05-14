-- 1.
-- Without subquery
SELECT DISTINCT C.customer_name, C.customer_street, C.customer_city
FROM customer C, account A, branch B
WHERE C.customer_name IN (SELECT D.customer_name
                          FROM depositor D
                          WHERE D.account_number = A.account_number)
      AND A.branch_name = B.branch_name
      AND C.customer_city = B.branch_city;
      
      -- With subquery
SELECT DISTINCT C.customer_name, C.customer_street, C.customer_city
FROM customer C
WHERE C.customer_name IN (
    SELECT D.customer_name
    FROM depositor D, account A, branch B
    WHERE D.account_number = A.account_number
      AND A.branch_name = B.branch_name
      AND C.customer_city = B.branch_city
);


----2.
-- Without subquery
SELECT DISTINCT C.customer_name, C.customer_street, C.customer_city
FROM customer C, loan L, branch B
WHERE C.customer_name IN (SELECT BR.customer_name
                          FROM borrower BR
                          WHERE BR.loan_number = L.loan_number)
      AND L.branch_name = B.branch_name
      AND C.customer_city = B.branch_city;
      
      
    
      -- With subquery
SELECT DISTINCT C.customer_name, C.customer_street, C.customer_city
FROM customer C
WHERE C.customer_name IN (
    SELECT BR.customer_name
    FROM borrower BR, loan L, branch B
    WHERE BR.loan_number = L.loan_number
        AND L.branch_name = B.branch_name
        AND C.customer_city = B.branch_city);
        
   ---3.
   -- With HAVING clause
SELECT B.branch_city, AVG(A.balance) AS avg_balance
FROM branch B, account A
WHERE A.branch_name = B.branch_name
GROUP BY B.branch_city
HAVING SUM(A.balance) >= 1000;

-- without HAVING clause
SELECT branch_city, AVG(balance) AS avg_balance
FROM (
    SELECT B.branch_city, A.balance, SUM(A.balance) OVER (PARTITION BY B.branch_city) AS total_balance
    FROM branch B, account A
    WHERE A.branch_name = B.branch_name
) T
WHERE T.total_balance >= 1000
GROUP BY branch_city;

---4. 
-- With HAVING clause
SELECT B.branch_city, AVG(L.amount) AS avg_amount
FROM branch B, loan L
WHERE L.branch_name = B.branch_name
GROUP BY B.branch_city
HAVING AVG(L.amount) >= 1500;

-- Without HAVING clause
SELECT branch_city, AVG(amount) AS avg_amount
FROM (
    SELECT B.branch_city, L.amount
    FROM branch B, loan L
    WHERE L.branch_name = B.branch_name
) 
WHERE amount >= 1500
GROUP BY branch_city;

--5.
--With ALL   Keyword---

SELECT C.customer_name, C.customer_street, C.customer_city
FROM customer C, depositor D, account A
WHERE C.customer_name = D.customer_name
  AND D.account_number = A.account_number
  AND A.balance >= ALL (SELECT balance FROM account);


--without  ALLL keyword----
SELECT customer_name, customer_street, customer_city
FROM (
    SELECT C.customer_name, C.customer_street, C.customer_city
    FROM customer C
    JOIN depositor D ON C.customer_name = D.customer_name
    JOIN account A ON D.account_number = A.account_number
    ORDER BY A.balance DESC
)
WHERE ROWNUM = 1;

--6.
-- With ALL keyword
SELECT C.customer_name, C.customer_street, C.customer_city
FROM customer C, borrower B, loan L
WHERE C.customer_name = B.customer_name
  AND B.loan_number = L.loan_number
  AND L.amount <= ALL (SELECT amount FROM loan);


-- Without ALL keyword
SELECT customer_name, customer_street, customer_city
FROM (
    SELECT C.customer_name, C.customer_street, C.customer_city
    FROM customer C
    JOIN borrower B ON C.customer_name = B.customer_name
    JOIN loan L ON B.loan_number = L.loan_number
    ORDER BY L.amount ASC
)
WHERE ROWNUM = 1;

--7.

-- Using IN
SELECT DISTINCT B.branch_name, B.branch_city
FROM branch B
WHERE B.branch_name IN (SELECT branch_name FROM account)
  AND B.branch_name IN (SELECT branch_name FROM loan);

-- Using EXISTS
SELECT DISTINCT B.branch_name, B.branch_city
FROM branch B
WHERE EXISTS (SELECT 1 FROM account A WHERE A.branch_name = B.branch_name)
  AND EXISTS (SELECT 1 FROM loan L WHERE L.branch_name = B.branch_name);


--8.
-- Using NOT IN
SELECT DISTINCT C.customer_name, C.customer_city
FROM customer C
WHERE C.customer_name NOT IN (SELECT customer_name FROM borrower)
  AND C.customer_name IN (SELECT customer_name FROM depositor);

-- Using NOT EXISTS
SELECT DISTINCT C.customer_name, C.customer_city
FROM customer C
WHERE NOT EXISTS (SELECT 1 FROM borrower B WHERE B.customer_name = C.customer_name)
  AND EXISTS (SELECT 1 FROM depositor D WHERE D.customer_name = C.customer_name);


--9. 
-- With WITH clause
WITH BranchBalance AS (
    SELECT branch_name, SUM(balance) AS total_balance
    FROM account
    GROUP BY branch_name
),
AvgBalance AS (
    SELECT AVG(total_balance) AS avg_balance FROM BranchBalance
)
SELECT branch_name
FROM BranchBalance
WHERE total_balance > (SELECT avg_balance FROM AvgBalance);

-- Without WITH clause
SELECT branch_name
FROM (
    SELECT branch_name, SUM(balance) AS total_balance
    FROM account
    GROUP BY branch_name
) BranchBalance
WHERE total_balance > (SELECT AVG(SUM(balance)) FROM account GROUP BY branch_name);


--10. 

-- With WITH clause
WITH BranchLoan AS (
    SELECT branch_name, SUM(amount) AS total_loan
    FROM loan
    GROUP BY branch_name
),
AvgLoan AS (
    SELECT AVG(total_loan) AS avg_loan FROM BranchLoan
)
SELECT branch_name
FROM BranchLoan
WHERE total_loan < (SELECT avg_loan FROM AvgLoan);

-- Without WITH clause
SELECT branch_name
FROM (
    SELECT branch_name, SUM(amount) AS total_loan
    FROM loan
    GROUP BY branch_name
) BranchLoan
WHERE total_loan < (SELECT AVG(SUM(amount)) FROM loan GROUP BY branch_name);
        
