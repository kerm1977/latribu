#IMPORTS ----------------
from flask import session, Flask, abort, g
from datetime import datetime, timedelta
from flask import request, make_response, redirect, render_template, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, HiddenField, EmailField, IntegerField
from wtforms.validators import DataRequired, Length, Email,  EqualTo, ValidationError
from wtforms.widgets import TextArea
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_
from flask_ckeditor import CKEditor, CKEditorField #Editor enriquecido con instancia ckeditor = CKEditor(app)
from wtforms import validators
from time import sleep
from flask import Blueprint
from datetime import datetime
from pytz import timezone
from flask import json
from werkzeug.exceptions import HTTPException

# print(now_time.strftime('%I:%M:%S %p'))











# SQLITE3 DB ------------
# Crea una instancia de Flask
app = Flask(__name__)

#Editor enriquecido
ckeditor = CKEditor(app)

import os
#Ruta de la DB
dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/db.db" #CONECTOR - RUTA ABSOLUTA
app.config['SQLALCHEMY_DATABASE_URI'] = dbdir
#importa arriba y configura aquí el tiempo que va a estar activa la session.

db = SQLAlchemy(app)
app.app_context().push()
migrate = Migrate(app,db,render_as_batch=True)
bcrypt 	= Bcrypt(app)

pw_hash = bcrypt.generate_password_hash("SECRET_KEY")
bcrypt.check_password_hash(pw_hash, "SECRET_KEY")
app.config['SECRET_KEY'] = pw_hash
# print(pw_hash)
# -----------------------










# MANEJO DE SESIONES ----
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login" # 
login_manager.login_message = u"Primero necesitas iniciar sesión"
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
# MANEJO DE SESIONES ----









#FECHA ------------------
#Permite pasar al idioma local las fechas y alertas
import locale
locale.setlocale(locale.LC_ALL, 'es_ES')
# -----------------------
@app.add_template_filter
def fecha(date):		
						
						# %a %H:%M %d/%m/%y <-- mié. 21:21 07/02/24
						# %H:%M:%S 
						# %A, %d. %B %Y %I:%M%p <-- miércoles, 07. febrero 2024 09:22p. m.
						# %d-%m-%Y  - formato de raya 
						# %d/%m/%Y  / formato de slash
	return date.strftime("%A, %d de %B %Y ")
# -----------------------










# #VIEWS ------------------
# Viables que se pueden utilizar en jinja
# safe, capitalize, lower, upper, title,trim,striptags
#trim Elimina los espacios finales

# HOME
@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
	date = datetime.now(timezone('America/Chicago'))
	user 	= 	{"username":"Kenneth"}
	lname 	= 	{"lastname":"Ruiz"}
	enlaces = 	["python","flask","bootstrap","vue"]
	title 	= 	"INICIO"
	return render_template("index.html",user=user, title=title, lname=lname, enlaces=enlaces, date=date)


@app.route("/caminocr")
def caminocr():
	date 	= 	datetime.now(timezone('America/Chicago'))
	title 	= 	"Camino de Costa Rica"
	return render_template("caminocr.html", title=title, date=date)


@app.route("/videos")
def videos():
	date 	= 	datetime.now(timezone('America/Chicago'))
	title 	= 	"Camino de Costa Rica"
	return render_template("videos.html", title=title, date=date)

@app.route("/registro")
def registro():
	date 	= 	datetime.now(timezone('America/Chicago'))
	title 	= 	"Camino de Costa Rica"
	return render_template("register.html", title=title, date=date)

@app.route("/login")
def login():
	date 	= 	datetime.now(timezone('America/Chicago'))
	title 	= 	"Camino de Costa Rica"
	return render_template("login.html", title=title, date=date)

@app.errorhandler(404)
# Error página no encontrada
def page_not_found(e):
	date 	= 	datetime.now(timezone('America/Chicago'))
	return render_template('404.html',date=date), 404

@app.errorhandler(500)
# Servidor no encontrada
def server_not_found(e):
	date 	= 	datetime.now(timezone('America/Chicago'))
	return render_template('500.html',date=date), 500



# -----------------------
if __name__ == "__main__":

	db.create_all()
	# db.upgrade_all()
	# db.drop_all()	#Solo se ejecuta para migrar nuevos campos a la db pero borra el contenido
	app.run(debug = True) 

	# Migraciones Cmder
		# set FLASK_APP=main.py 	<--Crea un directorio de migraciones
		# flask db init 			<--
		# $ flask db stamp head
		# $ flask db migrate
		# $ flask db migrate -m "mensaje x"
		# $ flask db upgrade
# -----------------------






