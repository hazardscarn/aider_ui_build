from flask import Flask, render_template, request

app = Flask(__name__)
response_agent = ResponseAgent()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = response_agent.respond(user_input)
        chat_history.append({'user_input': user_input, 'response': response})
        return render_template('index.html', user_input=user_input, response=response)

    chat_history = response_agent.chat_history
    return render_template('index.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)
