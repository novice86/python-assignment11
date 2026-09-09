import sqlite3
import pandas as pd

from matplotlib import pyplot as plt


# Task 2: A Line Plot with Pandas
sql_statement = """
    SELECT o.order_id, SUM(p.price * l.quantity) AS total_order_value
    FROM orders o
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id ASC
"""

with sqlite3.connect('../db/lesson.db') as conn:
    df = pd.read_sql_query(sql_statement, conn)


df['cumulative_revenue'] = df['total_order_value'].cumsum()
df.plot(x='order_id', y='cumulative_revenue', kind='line', title='Cumulative Revenue vs Order ID', color='green')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue')
plt.tight_layout()
plt.show()
