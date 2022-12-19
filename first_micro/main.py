from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/logger/', methods = ["GET"])
def logger():
    return render_template('logger.html')


# add a route to print the user input in the console from the textbox
@app.route('/textbox', methods=["POST"])
def print():
    script = """
    <script>
        function myFunction() {
        var message = document.getElementById("message").value;
        console.log(message);
        }
    </script>"""
    return """
    <input type="text" id="message" placeholder="Enter a message">
    <button onclick="myFunction()">Print</button>""" + script



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
