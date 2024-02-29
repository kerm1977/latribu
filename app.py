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













# SQLITE3 DB ------------
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










#VIEWS ------------------

# HOME
@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
	date 	= 	datetime.now()
	user 	= 	{"username":"Kenneth"}
	lname 	= 	{"lastname":"Ruiz"}
	enlaces = 	["python","flask","bootstrap","vue"]
	title 	= 	"INICIO"
	return render_template("index.html",user=user, title=title, lname=lname, enlaces=enlaces, date=date)


@app.route("/caminocr")
def caminocr():
	date 	= 	datetime.now()
	title 	= 	"Camino de Costa Rica"
	return render_template("caminocr.html", title=title, date=date)


@app.route("/videos")
def videos():
	date 	= 	datetime.now()
	title 	= 	"Camino de Costa Rica"
	return render_template("videos.html", title=title, date=date)




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






