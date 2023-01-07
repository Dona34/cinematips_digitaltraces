from flask import Flask, render_template
import requests
from pytrends.request import TrendReq
from datetime import datetime
import time
from collections import Counter

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')

app.config["DEBUG"] = True

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/logger/', methods = ["GET"])
def logger():
    return render_template('logger.html')

@app.route('/cookies/', methods = ["GET"])
def req():
    #req = requests.get("https://www.google.com/")
    req = requests.get("https://analytics.google.com/analytics/web/#/p344238092/reports/intelligenthome")
    
    #return req.cookies.get_dict()
    return req.text


# add a route to print the user input in the console from the textbox
@app.route('/textbox', methods=["POST"])
def text():
    return render_template('text.html')

# TP3
# pytrends 
@app.route('/trend_egea/', methods=["GET"])
def trend_egea():

    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(kw_list=['egea'])
    interest_over_time_df = pytrends.interest_over_time()
    egea = interest_over_time_df['egea'].values.tolist()
    dates = [datetime.fromtimestamp(int(date/1e9)).date().isoformat() for date in interest_over_time_df.index.values.tolist()]

    params = { 
        "type": 'line',
        "data": {
        "labels": dates,
        "datasets": [{
            "data": egea,
            "label": "Egea",
            "borderColor": "#3e95cd",
            "fill": 'false'
            }]},
            
            "options": {
                "title": {
                "display": 'true',
                "text": 'Research of the word "Egea" over time'
                },
                "hover": {
                "mode": 'index',
                "intersect": 'true'
                },
            }
    }

    prefix_google = """

        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>

        <canvas id="myChart" width="50" height="50"></canvas>""" + f"""
        <script>
        var ctx = document.getElementById('myChart');
        var myChart = new Chart(ctx, {params});
        </script>

        """

    return prefix_google


#timer Log        

def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper

@app.route('/log_time/')
@log_time
def counter():
    for i in range(1):
        start_time = time.time()
        with open('shakespeare.txt', 'r') as f:
            text = f.read()
        word_count_dict = count_words_dict(text)
        start_time_2 = time.time()
        word_count_counter = count_words_function(text)
        print(word_count_dict)
        print(word_count_counter) 
    return "Counting time dictionnary"+"   "+f"  {(time.time() - start_time_2)}"+"Counting time counter"+"   "+f"{(start_time_2 - start_time)}"

#counter of words in shakespeare file
@app.route('/counter')
def counter():
    with open('shakespeare.txt', 'r') as f:
        text = f.read()
    start_time = time.time()
    word_count_dict = count_words_dict(text)
    dict_time = f"The time to compute with dict is {time.time() - start_time}"

    start_time = time.time()
    word_count_counter = count_words_function(text)
    func_time = f"The time to compute with Counter function is {time.time() - start_time}"

    return f"""{dict_time}<br><br>{func_time}<br><br>{word_count_dict}<br><br>{word_count_counter}"""


def count_words_dict(text):
    word_dict = {}
    for word in text.split():
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


def count_words_function(text):
    return Counter(text.split())

# TP1


    # def hello_world():

#     prefix_google = """
#     <!-- Google tag (gtag.js) -->
#     <script async
#     src="https://www.googletagmanager.com/gtag/js?id=G-XE21ZZ8ZV7"></script>
#     <script>
#     window.dataLayer = window.dataLayer || [];
#     function gtag(){dataLayer.push(arguments);}
#     gtag('js', new Date());
#     gtag('config', 'G-XE21ZZ8ZV7');
#     </script>
#     """
#     return prefix_google + "Hello World"

# https://gscx4f.deta.dev

# @app.route('/text/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return processed_text
