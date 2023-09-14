from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Sample CSV URL
csv_url = 'https://raw.githubusercontent.com/nimratmann/azure_flask_deployment/main/Dataset/New_York_City_Leading_Causes_of_Death.csv'

# Load the CSV data
df = pd.read_csv(csv_url)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/data')
def data():
    # Sample 20 rows from the loaded CSV data
    sample_data = df.sample(20)
    return render_template('data.html', data=sample_data)

if __name__ == '__main__':
    app.run(
        debug=True,
        port= 8080
    )