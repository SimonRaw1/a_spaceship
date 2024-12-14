from flask import Flask, render_template, jsonify
from markupsafe import escape
from json2table import convert
import json
import trackerinputs
import tablib

app = Flask (__name__)
display_dict = {
    "squat" : "./Squat Sessions.txt",
    "bench" : "./Bench Sessions.txt",
    "deadlift" : "./Deadlift Sessions.txt"
}
squat_data = tablib.Dataset()
bench_data = tablib.Dataset()
deadlift_data = tablib.Dataset()

@app.route("/", methods=["GET", "POST"])
def home_page():
    return render_template('home.html')

@app.route("/display", methods=["GET"])
def display_page():
    return render_template('display.html')

@app.route("/submit", methods=["GET"])
def submit_data():
    return render_template('display.html')

@app.route("/display/squat")
def display_squat():
    build_direction = "TOP_TO_BOTTOM"
    table_attributes = {"style" : "width:100%"}
    a={}
    with open("./Squat Sessions.json") as fh:
        squat_data = fh.read()
    a = json.loads(squat_data)
    table = convert(a, build_direction=build_direction, table_attributes=table_attributes)
    return jsonify(table)

@app.route("/display/bench")
def display_bench():
    build_direction = "TOP_TO_BOTTOM"
    table_attributes = {"style" : "width:100%"}
    a={}
    with open("./Bench Sessions.json") as fh:
        bench_data = fh.read()
    a = json.loads(bench_data)
    table = convert(a, build_direction=build_direction, table_attributes=table_attributes)
    return jsonify(table)

@app.route("/display/deadlift")
def display_deadlift():
    build_direction = "TOP_TO_BOTTOM"
    table_attributes = {"style" : "width:100%"}
    a={}
    with open("./Deadlift Sessions.json") as fh:
        deadlift_data = fh.read()
    a = json.loads(deadlift_data)
    table = convert(a, build_direction=build_direction, table_attributes=table_attributes)
    return jsonify(table)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='80',debug=True)