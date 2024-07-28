from flask import Flask, render_template, request
from response import ResponseAgent

app = Flask(__name__)
response_agent = ResponseAgent()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = response_agent.respond(user_input)
        return render_template('index.html', user_input=user_input, response=response)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
