from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = open('flight_rf_reg.pkl', 'rb')
forest_model = pickle.load(model)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    dep_hour = request.form.get('dep_hour')
    dep_mins = request.form.get('dep_mins')
    arrival_hour = request.form.get('arrival_hour')
    arrival_min = request.form.get('arrival_min')
    duration_hour = request.form.get('duration_hour')
    duration_min = request.form.get('duration_min')
    total_stops = request.form.get('Total_Stops')
    journey_day = request.form.get('journey_day')
    journey_month = request.form.get('journey_month')

    prediction = forest_model.predict([[dep_hour, dep_mins, arrival_hour, arrival_min, duration_hour, duration_min, total_stops, journey_day, journey_month]])
    output = round(prediction[0], 2)

    # return str(output)
    return render_template('result.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
