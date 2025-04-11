from flask import Flask, render_template
import plotly.graph_objs as go
import plotly.offline as pyo
import random
import os

app = Flask(__name__)

@app.route('/')
def index():
    x_vals = list(range(10))
    y_vals = [random.randint(0, 10) for _ in x_vals]

    trace = go.Scatter(
        x=x_vals,
        y=y_vals,
        mode='lines+markers',
        line=dict(width=2),
        marker=dict(size=8),
        name='Random Numbers'
    )

    layout = go.Layout(
        title='Random Number Plot',
        xaxis=dict(title='Index'),
        yaxis=dict(title='Value'),
        template='plotly_dark',
        margin=dict(l=40, r=40, t=50, b=40)
    )

    fig = go.Figure(data=[trace], layout=layout)
    plot_html = pyo.plot(fig, output_type='div', include_plotlyjs=True)

    return render_template('index.html', plot_div=plot_html)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


