import plotly.express as px
import plotly.data as pldata


# Task 3: Interactive Visualizations with Plotly
df = pldata.wind(return_type='pandas')
print(df.head(10))
print(df.tail(10))

# Clean up the strength column to remove the "-" and "+" sign, then convert to float
df['strength'] = df['strength'].str.replace(r'-.*|\+', '', regex=True).astype(float)

fig = px.scatter(
    df, 
    x='strength',
    y='frequency',
    color='direction',
    title="Wind Strength vs Frequency by Direction",
    labels={
        'strength': 'Wind Strength',
        'frequency': 'Frequency',
        'direction': 'Wind Direction'
    }
)
fig.write_html("wind.html", auto_open=True)
