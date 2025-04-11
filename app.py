from flask import Flask, render_template, request
import plotly.graph_objs as go
import plotly.offline as pyo
import random
import numpy as np
import os  


app = Flask(__name__)

def simulate_heart_data(age):
    # Base ranges
    hr_base = max(60, 220 - age)  # Approximate max HR for age
    hrv_base = max(20, 120 - age)  # Rough guess: HRV declines with age

    x = list(range(30))  # 30 seconds

    # Simulate HR (bpm)
    hr = [random.randint(hr_base - 10, hr_base + 10) for _ in x]

    # Simulate HRV (ms)
    hrv = [random.uniform(hrv_base - 10, hrv_base + 10) for _ in x]

    return x, hr, hrv

@app.route('/', methods=['GET', 'POST'])

def index():
    plot_hr = ''
    plot_hrv = ''

    if request.method == 'POST':
        age = int(request.form['age'])
        x, hr_data, hrv_data = simulate_heart_data(age)

        # Heart Rate plot
        fig_hr = go.Figure()
        fig_hr.add_trace(go.Scatter(x=x, y=hr_data, mode='lines+markers', name='Heart Rate'))
        fig_hr.update_layout(title='Simulated Heart Rate (bpm)', template='plotly_dark')
        plot_hr = pyo.plot(fig_hr, output_type='div', include_plotlyjs=False)

        # HRV plot
        fig_hrv = go.Figure()
        fig_hrv.add_trace(go.Scatter(x=x, y=hrv_data, mode='lines+markers', name='HRV'))
        fig_hrv.update_layout(title='Simulated HRV (ms)', template='plotly_dark')
        plot_hrv = pyo.plot(fig_hrv, output_type='div', include_plotlyjs=False)

    return render_template('index.html', plot_hr=plot_hr, plot_hrv=plot_hrv)



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


