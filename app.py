from data_analysis import formater
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/Dashboard")
def dashboard():
    filters = request.args.to_dict()
    formated_filters = formater.format_filters(filters)
    # TODO Get dataframe by:
    # df = data.filter_data(formated_filters)

    # TODO Get analysis by:
    # analysis = data.analyze(df) -> dict

    # TODO Get data_stream by:
    # data_stream = slice_data(df,number_of_rows:int = 10 ,page:int =1) -> dict with num rows, current_page, total_number_of_pages, data

    # TODO render analysis and data_stream on dashboard.html
    return formated_filters
    # return render_template("dashboard.html")

# TODO Create stream route
# @app.route("/Stream Data")
# def stream_data(filters: dict): -> dict with num rows, current_page, total_number_of_pages, data
    # Note filter contains number_of_rows and page as well
