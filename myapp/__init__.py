from flask import Flask

from myapp.task.controllers import taskRoute

from myapp.config import DevConfig

app = Flask(__name__)
app.register_blueprint(taskRoute)
app.config.from_object(DevConfig)


@app.route("/")
def hello_world() -> str:
     return "Hello mundoo 2233!!"
