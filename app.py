from data_analysis import formater, data, analysis
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Render Query page."""
    return render_template("index.html")


@app.route("/Dashboard")
def dashboard():
    "Gether analysis and render on dashboard."
    formated_filters = formater.format_filters(request.args.to_dict())
    df = data.filter_data(formated_filters)
    stats = analysis.analyze(df)

    # TODO Get data_stream by:
    # data_stream = slice_data(df,number_of_rows:int = 10 ,page:int =1) -> dict with num rows, current_page, total_number_of_pages, data

    # TODO render analysis and data_stream on dashboard.html
    # return render_template("dashboard.html")
    return {"response": stats, "filters": formated_filters}

# TODO Create stream route
# @app.route("/Stream Data")
# def stream_data(filters: dict): -> dict with num rows, current_page, total_number_of_pages, data
    # Note filter contains number_of_rows and page as well
