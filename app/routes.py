from flask import render_template
from app import app
from app.visualizations import create_visualizations

@app.route('/')
def index():
    charts = create_visualizations()  # Get the visualizations
    return render_template('index.html', charts=charts)  # Pass them to the template
