# Healthcare Data Security Dashboard

This project is a **Healthcare Data Security Dashboard** built using **Flask** and **Plotly**. The dashboard visualizes synthetic healthcare access logs, showing events like daily accesses and breaches. The primary objective is to track access to healthcare data and monitor breaches across various locations and sensitivity levels.

## Project Features

- **Line Chart**: Displays daily accesses and breaches.
- **Pie Chart**: Shows the distribution of breaches by location.
- **Bar Chart**: Displays the sensitivity levels of accessed data.
- **Interactive Dashboard**: Allows users to explore the visualizations interactively using Plotly's responsive charts.

## Technologies Used

- **Python**: Core programming language for data processing and web development.
- **Flask**: Lightweight web framework used to build the backend.
- **Plotly**: A powerful data visualization library for interactive charts and graphs.
- **Pandas**: For loading and preprocessing the synthetic dataset.
- **HTML/CSS/JavaScript**: For frontend and embedding the visualizations.

## Dataset

The dataset used in this project is **synthetic healthcare data security logs**. It includes columns like:

- **User ID**: Unique identifier for each user.
- **Access Time**: The timestamp of when the data was accessed.
- **Action Type**: Whether the action was an "Access" or "Breach."
- **Data Sensitivity**: The sensitivity level of the accessed data (Low, Medium, High).
- **Location**: Geographic location of the access (e.g., USA, Europe, Asia).

The dataset is stored as `data/simulated_data.csv` and is generated using a Python script. The visualizations are built based on this dataset.

## How to Run the Project

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

1. **Clone the repository**:

   Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/vishalarvinvinayaga/healthcare_data_dashboard.git


   cd healthcare_data_dashboard

    python3 -m venv env
    source env/bin/activate  # For macOS/Linux
    # or
    .\env\Scripts\activate   # For Windows


    pip install -r requirements.txt


    python run.py


    http://127.0.0.1:5000/

   ```
