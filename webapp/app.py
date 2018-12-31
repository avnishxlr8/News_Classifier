
# coding: utf-8


import flask
import pickle
import run_model


app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        input_text = flask.request.form['textarea']
        prediction = run_model.predict(input_text)
        return flask.render_template('main.html',
                                     result=prediction
                                     )
if __name__ == '__main__':
    app.run()

