#task2 level3 a simple data visualisation implementation using plotly 
import plotly.express as px
import pandas as pd

def load_dataset_from_csv(file_path):
    # Load the dataset from a CSV file
    dataset = pd.read_csv(file_path)
    return dataset

def create_scatter_plot(data):
    # Create an interactive scatter plot
    fig = px.scatter(data, x='X', y='Y', color='Category', title='Interactive Scatter Plot')
    fig.show()

def create_bar_chart(data):
    # Create an interactive bar chart
    fig = px.bar(data, x='Category', y='X', title='Interactive Bar Chart')
    fig.show()

# Load the dataset from the CSV file
loaded_dataset = load_dataset_from_csv('test_dataset.csv')

# Create and display visualizations
create_scatter_plot(loaded_dataset)
create_bar_chart(loaded_dataset)
