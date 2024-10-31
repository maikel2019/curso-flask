from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from myapp.config import DevConfig

app = Flask(__name__) #template_folder='/pages'

#configurations
app.config.from_object(DevConfig)
# app.debug = True

#db
db=SQLAlchemy(app)

#blueprints
from myapp.tasks.controllers import taskRoute
app.register_blueprint(taskRoute)

#create db
with app.app_context():
    db.create_all()

#route
@app.route('/')
def hello_world(): # -> str
    name = request.args.get('name','Desarrollolibre')
    return render_template('index.html',task=name,name=name)
    # return 'Hello Flask'