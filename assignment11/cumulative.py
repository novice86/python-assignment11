import sqlite3
import pandas as pd

from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator


# Task 2: A Line Plot with Pandas
sql_statement = """
    SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
    FROM orders o
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id ASC
"""

with sqlite3.connect('../db/lesson.db') as conn:
    df = pd.read_sql_query(sql_statement, conn)

df['cumulative'] = df['total_price'].cumsum()
df.plot(
    x='order_id', 
    y='cumulative', 
    kind='line', 
    title='Cumulative Revenue vs Order ID', 
    color='green',
    legend=False
)
plt.xlabel('order_id')
plt.ylabel('Cumulative Revenue ($)')

plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

plt.tight_layout()
plt.show()
