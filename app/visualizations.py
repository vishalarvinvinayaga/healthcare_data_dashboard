import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Load the synthetic data
def load_data():
    data = pd.read_csv('data/simulated_data.csv')
    return data

# Function to create visualizations
def create_visualizations():
    # Load data
    data = load_data()

    # Parse and preprocess data (if needed)
    data['Access Time'] = pd.to_datetime(data['Access Time'])
    data['Date'] = data['Access Time'].dt.date

    # 1. Line Chart - Daily Accesses and Breaches
    daily_counts = data.groupby(['Date', 'Action Type']).size().unstack(fill_value=0)

    line_chart = go.Figure()
    line_chart.add_trace(go.Scatter(x=daily_counts.index, y=daily_counts['Access'], mode='lines', name='Accesses'))
    line_chart.add_trace(go.Scatter(x=daily_counts.index, y=daily_counts['Breach'], mode='lines+markers', name='Breaches'))

    line_chart.update_layout(
        title="Daily Accesses vs Breaches",
        xaxis_title="Date",
        yaxis_title="Count",
        hovermode="x unified"
    )

    # 2. Pie Chart - Breaches by Location
    breach_by_location = data[data['Action Type'] == 'Breach'].groupby('Location').size()

    pie_chart = go.Figure(data=[go.Pie(labels=breach_by_location.index, values=breach_by_location.values)])
    pie_chart.update_layout(title="Breaches by Location")

    # 3. Bar Chart - Data Sensitivity Levels
    sensitivity_counts = data['Data Sensitivity'].value_counts()

    bar_chart = go.Figure(go.Bar(x=sensitivity_counts.index, y=sensitivity_counts.values))
    bar_chart.update_layout(
        title="Data Sensitivity Levels",
        xaxis_title="Sensitivity Level",
        yaxis_title="Count"
    )

    # Convert charts to JSON for rendering in HTML
    charts = {
        'line_chart': line_chart.to_json(),
        'pie_chart': pie_chart.to_json(),
        'bar_chart': bar_chart.to_json(),
    }

    return charts
