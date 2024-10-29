from flask import Flask, render_template, request

from myapp.task.controllers import taskRoute

from myapp.config import DevConfig

app = Flask(__name__)
app.register_blueprint(taskRoute)
app.config.from_object(DevConfig)


@app.route("/")
def hello_world() -> str:
     return render_template('index.html')
