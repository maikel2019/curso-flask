from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from myapp.config import DevConfig

app = Flask(__name__) #template_folder='/pages'

#configurations
app.config.from_object(DevConfig)
# app.debug = True

#db
db=SQLAlchemy(app)
migrate = Migrate(app, db)



#blueprints
from myapp.tasks.controllers import taskRoute
app.register_blueprint(taskRoute)

#create db (Al usar Migrate esta parte ya no tendríamos que tenerla. Aquí creaba la tabla y los elementos cada vez
# que recargaba la página. Ahora con Migrate lo haremos manualmente)
#with app.app_context():
#    db.create_all()

#route
@app.route('/')
def hello_world(): # -> str
    name = request.args.get('name','Desarrollolibre')
    return render_template('index.html',task=name,name=name)
    # return 'Hello Flask'