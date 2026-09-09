import sqlite3
import pandas as pd

from matplotlib import pyplot as plt


# Task 1: Plotting with Pandas
sql_statement = """
    SELECT e.last_name, SUM(p.price * l.quantity) AS revenue
    FROM employees e
    JOIN orders o ON e.employee_id = o.employee_id
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY e.employee_id
"""

with sqlite3.connect('../db/lesson.db') as conn:
    df = pd.read_sql_query(sql_statement, conn)

df.plot(x='last_name', y='revenue', kind='bar', title='Employee Revenue', color='skyblue')
plt.show()