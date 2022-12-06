from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():

    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async
    src="https://www.googletagmanager.com/gtag/js?id=G-XE21ZZ8ZV7"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-XE21ZZ8ZV7');
    </script>
    """
    return prefix_google + "Hello World"

# https://gscx4f.deta.dev

@app.route('/text', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route('/logger')
def logger():

    return print(app.logger)

if __name__ == '__main__':
    app.run(debug=True)