#IMPORTS ----------------
from flask import request, make_response, redirect, render_template, url_for, flash, Flask, abort, g
from flask.globals import session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TimeField, SubmitField, BooleanField, HiddenField, EmailField, IntegerField
from wtforms.validators import DataRequired, Length, Email,  EqualTo, ValidationError
from wtforms.widgets import TextArea
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_
from flask_ckeditor import CKEditor, CKEditorField #Editor enriquecido con instancia ckeditor = CKEditor(app)
from wtforms import validators
from time import sleep
from flask import Blueprint
from datetime import datetime, timedelta
from pytz import timezone
from flask import json
from werkzeug.exceptions import HTTPException
import pymysql.cursors
# from mysql.connector import

# print(now_time.strftime('%I:%M:%S %p'))
# pip uninstall -y -r  fichero








app = Flask(__name__)
# app.permanent_session_lifetime = timedelta(minutes=1)

#Editor enriquecido
ckeditor = CKEditor(app)

# SQLITE3 DB ------------
# -----------------------
# /::::::::::::::::::::/
# -----------------------
app = Flask(__name__)
#Editor enriquecido
ckeditor = CKEditor(app)










# DB SQLITE
# import os
# dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/db.db" #CONECTOR - RUTA ABSOLUTA

# app.config['SQLALCHEMY_DATABASE_URI'] = dbdir
	#host = "LaTribuHiking.mysql.pythonanywhere-services.com",
	#user = "LaTribuHiking",
	#password = "latribu1977",
	#database = "LaTribuHiking$db"


#DB MYSQL LOCAL
				 #-U  -P  -UBICACION -NOMBRE DB
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/db"



#DB MYSQL PYTHONANYWHERE INSTALAR
#pip uninstall mysql-connector-python-8.0.6
#pip install mysql-connector-python
# pip3  install mysql-connector-python
# pip3  install mysql-connector		
											                 #-U          -P                      -UBICACION                          -NOMBRE DB
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://LaTribuHiking:latribu1977@LaTribuHiking.mysql.pythonanywhere-services.com/LaTribuHiking$db"





# OTRA CONFIGURACIÓN
db = SQLAlchemy(app)
app.app_context().push()
migrate = Migrate(app,db,render_as_batch=True)

# CLAVE SECRETA
bcrypt 	= Bcrypt(app)
pw_hash = bcrypt.generate_password_hash("SECRET_KEY")
bcrypt.check_password_hash(pw_hash, "SECRET_KEY")
app.config['SECRET_KEY'] = pw_hash
# print(f"La Clave secreta es {pw_hash}")
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










#TABLAS -----------------
# -----------------------
# /::::::::::::::::::::/
# -----------------------

class User(db.Model, UserMixin):
	#Al agregar un campo hay que migrarlo a la DB y aquí se crean los campos del usuario
	id 					=	db.Column(db.Integer, 		primary_key=True)
	username 			= 	db.Column(db.String(20),	unique=False, 	nullable=False)
	apellido 			= 	db.Column(db.String(20),	unique=False,	nullable=True)
	apellido2 			= 	db.Column(db.String(20),	unique=False,	nullable=True)
	residencia 			= 	db.Column(db.String(120),	unique=False,	nullable=True)
	email 				= 	db.Column(db.String(120),	unique=True, 	nullable=False)
	telefono			= 	db.Column(db.String(15),	unique=False, 	nullable=True)
	telefonoE			= 	db.Column(db.String(15),	unique=False, 	nullable=True)
	celular				= 	db.Column(db.String(15),	unique=False, 	nullable=True)
	password 			= 	db.Column(db.String(60),	unique=False, 	nullable=False)
	confirmpassword		= 	db.Column(db.String(60),	unique=False, 	nullable=False)
	alergias			= 	db.Column(db.String(100),	unique=False, 	nullable=True)
	tiposangre 			= 	db.Column(db.String(100),	unique=False, 	nullable=True)
	cronico				= 	db.Column(db.String(100),	unique=False, 	nullable=True)
	medicamentos		= 	db.Column(db.String(100),	unique=False, 	nullable=True)
	nacimiento			= 	db.Column(db.String(20),	unique=False, 	nullable=True)
	imagen_perfil		= 	db.Column(db.String(20),	nullable=False, default="default.jpg")
	date_added			= 	db.Column(db.DateTime,		nullable=False,	default=datetime.utcnow)
	# El usuario puede tener muchos posts y "Posts" es el nombre de la clase a la que se va a referenica
	posts_ref 			= 	db.relationship("Posts", 	backref="user")

	#Al agregar un campo hay que migrarlo a la DB y también agregarlo en esta fila con la misma sintaxis y orden
	def __repr__(self):
		return f"User('{self.username}',{self.apellido}',{self.apellido2}','{self.residencia}','{self.email}','{self.telefono}','{self.celular}','{self.password}','{self.confirmpassword}','{self.alergias}','{self.cronico}','{self.nacimiento}','{self.medicamentos}','{self.imagen_perfil}')"

class Posts(db.Model):
	id 					=	db.Column(db.Integer, primary_key=True)
	titulo 				= 	db.Column(db.String(255))
	descripcion			=	db.Column(db.Text)
	content				=	db.Column(db.Text)
	kilometros			=	db.Column(db.Float)
	altura				=	db.Column(db.Float)
	lugar				=	db.Column(db.Text)
	finaliza			=	db.Column(db.Text)
	etapa				=	db.Column(db.Integer)
	capacidad			=	db.Column(db.Integer)
	hora				=	db.Column(db.Integer)
	salida				=	db.Column(db.Text)
	dificultad			=	db.Column(db.Text)
	sinpe				=	db.Column(db.Integer)
	coordinador			=	db.Column(db.Text)
	precio				=	db.Column(db.Text)
	limite_pago			=	db.Column(db.DateTime)
	parqueo				= 	db.Column(db.Text)
	mascotas			=	db.Column(db.Text)
	duchas				= 	db.Column(db.Text)
	banos				= 	db.Column(db.Text)
	date_posted			=	db.Column(db.DateTime, default=datetime.utcnow)
	slug 				= 	db.Column(db.String(255))

	#Crear una llave foranea entre los Posts y los usuarios referenciado con la llave primaria del usuario
	# Donde user.id es la clase del modelo llamada  class User y .id el id de esa clase
	poster_id = db.Column(db.Integer, db.ForeignKey("user.id"))

# -----------------------








# MODELOS FORMULARIO TABLAS LOGIN Y DE REGISTRO 
# -----------------------
# /::::::::::::::::::::/
# -----------------------
# Formulario de Registro
class formularioRegistro(FlaskForm):

	# Para agregar un campo a la DB se agrega dentro de este formulario, también 
	# en el modelo y la función _repr_ del modelo, Además del formulario registro 
	# y en  los formularios que se van a representar el campo. luego se migra  el 
	# nuevo campo con los pasos que están aquí mismo en la última línea  comentada
	# llamada migracion en ----RUN----- y en actualizar contactos

	#Estos son los campos que van a crearse al momento de crear la base de datos
 # CAMPOS EN DB			   TIPO DE DATO		NOMBRE DE CAMPO EN HTML Y VALIDACIONES	
	username 			= 	StringField		('username', validators=[DataRequired(), Length(min=3, max=20)]) 
	apellido 			= 	StringField		('apellido', validators=[Length(min=3, max=20)]) 
	apellido2 			= 	StringField		('apellido2', validators=[Length(min=3, max=20)])
	residencia			= 	SelectField		('residencia', choices=[("Cartago"),("San José"),("Alajuela"),("Heredia"),("Limón"),("Guanacaste"),("Puntarenas")])
	email 				= 	EmailField		('email', 	validators=[DataRequired(message="Digite un Email")])
	telefono			= 	StringField		('telefono', [validators.NumberRange(message="Digite un Teléfono")])
	telefonoE			= 	StringField		('emergencia', [validators.NumberRange(message="Digite un Teléfono de emergencia")])
	celular				= 	StringField		('celular', [validators.NumberRange(message="Digite un Celular")])
	password 			= 	PasswordField	('password',validators=[DataRequired(message='Se Requiere Password'), Length(min=8, max=20)]) 
	confirmpassword 	= 	PasswordField	('confirmpassword',validators=[DataRequired(message='Se Requiere Confirmación de Password'), EqualTo('password', message='Password No Coincide')], id="confirmpassword")
	alergias			= 	StringField		('alergias', validators=[Length(min=3, max=100)])
	tiposangre 			= 	SelectField		("sangre", validators=[DataRequired()], choices=[("No Indico"),("No Recibo Transfuciones"),("A+"),("A-"),("B+"),("B-"),("AB+"),("AB-"),("O+"),("O-")],)
	cronico				= 	StringField		('cronica', validators=[ Length(min=3, max=100)])
	medicamentos		= 	StringField		('medicamentos', validators=[Length(min=3, max=100)])
	nacimiento			= 	StringField		('nacimiento', validators=[Length(min=3, max=60)])		
	submit 				= 	SubmitField		('Registrarme')

	def validate_email(self, email):
		#user es la variable que almacena el primer email de contenido de la db
		user = User.query.filter_by(email.email.data).first()
		#Si la variable o si el email existe
		if user:
			#Advierte que el Email ya fue tomado.
			flash("El email ya fue tomado. Use otro ")

# Formularios de Login
class formularioLogin(FlaskForm):
 # CAMPOS EN DB			   TIPO DE DATO		NOMBRE DE CAMPO EN HTML Y VALIDACIONES
	email 				= 	StringField		('email', validators=[DataRequired(), Email()])
	password 			= 	PasswordField	('password', validators=[DataRequired()]) 
	rememberme 			= 	BooleanField	('checkbox')
	submit  			= 	SubmitField		('Ingresar')

# Formulario de posteo
class PostForm(FlaskForm):
	titulo 		= CKEditorField("Titulo", validators=[DataRequired()])
	descripcion = StringField("Breve Descripción", validators=[DataRequired()], widget=TextArea())	
	# content = StringField("Contenido", validators=[DataRequired()], widget=TextArea())
	content 	= CKEditorField("Descripción", validators=[DataRequired()])
	kilometros 	= IntegerField("Distancia | Millas", validators=[DataRequired()])
	altura 		= IntegerField("Altimetría")
	lugar		= StringField("Nombre del Lugar", validators=[DataRequired()])
	finaliza	= StringField("Finaliza", validators=[DataRequired()])
	etapa		= SelectField("Etapa #", validators=[DataRequired()], choices=[("1"),("2"),("3"),("4"),("5"),("6"),("7"),("8"),("9"),("10"),("11"),("12"),("13"),("14"),("15"),("16")])
	capacidad	= IntegerField("Capacidad de Transporte", validators=[DataRequired()])
	hora		= TimeField("Hora de Inicio", validators=[DataRequired()])
	salida		= StringField("Salimos de:", validators=[DataRequired()]) 
	dificultad	= StringField("Dificultad:", validators=[DataRequired()])
	capacidad	= IntegerField("Capacidad de Transporte", validators=[DataRequired()])
	sinpe		= IntegerField("Número Sinpe Autorizado", validators=[DataRequired()])
	coordinador = StringField("Guía", validators=[DataRequired()])	
	precio		= IntegerField("Capacidad de Transporte", validators=[DataRequired()])
	limite_pago	= IntegerField("Capacidad de Transporte", validators=[DataRequired()])
	parqueo 	= SelectField("Parqueo", validators=[DataRequired()], choices=[("SI"),("NO"),("NO APLICA")])
	mascotas	= SelectField("Acepta Mascotas", validators=[DataRequired()], choices=[("SI"),("NO"),("NO APLICA")])				
	duchas		= SelectField("Hay Duchas", validators=[DataRequired()], choices=[("SI"),("NO"),("NO APLICA")])
	banos		= SelectField("Servicios Sanitarios", validators=[DataRequired()], choices=[("SI"),("NO"),("NO APLICA")])
	poster_id 	= StringField("Autor", validators=[DataRequired()])
	slug 		= StringField("Detalle", validators=[DataRequired()])
	submit 		= SubmitField("Crear")

		
	
	# BORRAR SOLO referenciado
	# 			=	db.Column(db.Float)

	
	
	
	


	
	
	
	
	
	# date_posted			=	db.Column(db.DateTime, default=datetime.utcnow)
	# slug 				= 	db.Column(db.String(255))

# Formulario de búsqueda
class SearchForm(FlaskForm):
 # CAMPOS EN DB			   TIPO DE DATO		NOMBRE DE CAMPO EN HTML Y VALIDACIONES
  	searched			= 	StringField		('Buscar', validators=[DataRequired()])	
  	submit 				= 	SubmitField		('Buscar')
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

#PERMANENCIA
# @app.before_request
# def before_request():
#     session.permanent = True
#     # app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1)
#     app.permanent_session_lifetime = timedelta(minutes=1)
 
# DASHBOARD
@app.route("/dashboard", methods=["GET","POST"])
@login_required #Solo se puede editar con login
def dashboard():
	title = "Configuración"
	date = datetime.now(timezone('America/Chicago'))
	return render_template("dashboard.html", title=title, date=date)

# ADVANCE SEARCH
@app.route("/advanceSearch")
def advanceSearch():
	posts = Posts.query.all()
	return render_template("advanceSearch.html", posts=posts)

# LISTA DE CONTACTOS
@app.route("/contacts")
@login_required #Solo se puede editar con login
def contacts():
	values=User.query.all()
	users= len(values)
	titulo = "Inicio"
	date = datetime.now(timezone('America/Chicago'))
	return render_template("contacts.html", titulo=titulo, values=values, users=users,date=date)

#ACTUALIZAR CONTACTOS
@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
	date = datetime.now(timezone('America/Chicago'))
	form = formularioRegistro()
	values=User.query.all()
	users= len(values)
	actualizar_registro = User.query.get_or_404(id)
	if request.method == "POST":
		actualizar_registro.username = request.form["username"]
		actualizar_registro.apellido = request.form["apellido"]
		actualizar_registro.apellido2 = request.form["apellido2"]
		actualizar_registro.residencia = request.form["residencia"]
		actualizar_registro.email = request.form["email"]
		actualizar_registro.telefono = request.form["telefono"]
		actualizar_registro.telefonoE = request.form["telefonoE"]
		actualizar_registro.celular = request.form["celular"]
		actualizar_registro.alergias = request.form["alergias"]
		actualizar_registro.tiposangre = request.form["tiposangre"]
		actualizar_registro.cronico = request.form["cronico"]
		actualizar_registro.medicamentos = request.form["medicamentos"]
		actualizar_registro.nacimiento = request.form["nacimiento"]
		try:
			db.session.commit()
			flash(f"{form.username.data.title()} {form.apellido.data.title()} {form.apellido2.data.title()} {form.residencia.data.title()} {form.telefono.data.title()} {form.telefonoE.data.title()} {form.celular.data.title()} {form.telefono.data.title()} {form.tiposangre.data.title()} {form.tiposangre.data.title()} {form.cronico.data.title()} {form.medicamentos.data.title()} {form.nacimiento.data.title()} ha sido modificad@", "success")
			return render_template("contacts.html", form=form, date=date, actualizar_registro=actualizar_registro, values=values, users=users)
		except IntegrityError:
			db.session.rollback()
			flash(f"{form.email.data} YA EXISTE", "danger")
			return render_template("update_profile.html", form=form, date=date, actualizar_registro=actualizar_registro)	
		except:
			db.session.commit()
			flash("Hubo un error al intentar modificar el registro", "warning")
			return render_template("update.html", form=form, date=date, actualizar_registro=actualizar_registro)
	else:
		return render_template("update.html", form=form, date=date, actualizar_registro=actualizar_registro)

# ACTUALIZAR PERFIL SOLO SI ESTÁ LOGUEADO DASHBOARD
@app.route("/update_profile/<int:id>", methods=["GET","POST"])
@login_required #Solo se puede editar con login
def update_profile(id):
	form = formularioRegistro()
	values=User.query.all()
	users= len(values)
	date = datetime.now(timezone('America/Chicago'))
	actualizar_registro = User.query.get_or_404(id)
	if request.method == "POST":
		actualizar_registro.username 		= 	request.form["username"]
		actualizar_registro.apellido 		= 	request.form["apellido"]
		actualizar_registro.apellido2 		= 	request.form["apellido2"]
		actualizar_registro.residencia 		= 	request.form["residencia"]
		actualizar_registro.email 			= 	request.form["email"]
		actualizar_registro.telefono 		= 	request.form["telefono"]
		actualizar_registro.telefonoE 		= 	request.form["telefonoE"]
		actualizar_registro.celular 		= 	request.form["celular"]
		actualizar_registro.alergias 		= 	request.form["alergias"]
		actualizar_registro.tiposangre 		= 	request.form["tiposangre"]
		actualizar_registro.cronico 		= 	request.form["cronico"]
		actualizar_registro.medicamentos 	= 	request.form["medicamentos"]
		actualizar_registro.nacimiento 		= 	request.form["nacimiento"]
		
	
		try:
			db.session.commit()
			flash(f"{form.username.data.title()} {form.apellido.data.title()} {form.apellido2.data.title()} ha sido modificad@", "success")
			return render_template("dashboard.html", form=form, actualizar_registro=actualizar_registro, values=values, users=users)
		except IntegrityError:
			db.session.rollback()
			flash(f"{form.email.data} YA EXISTE", "danger")
			return render_template("update_profile.html", form=form, actualizar_registro=actualizar_registro,date=date)
		except:
			flash("Hubo un error al intentar modificar el registro", "warning")
			return render_template("update_profile.html", form=form, actualizar_registro=actualizar_registro,date=date)
	else:
		return render_template("update_profile.html", form=form, actualizar_registro=actualizar_registro,date=date)

# BORRAR CONTACTOS
@app.route("/delete/<int:id>")
@login_required
def delete(id):
	id_delete=id
	borrar_registro = User.query.get_or_404(id)
	
	try:
		db.session.delete(borrar_registro)
		db.session.commit()
		flash(f"El usuario fué Eliminado", "warning")
		return redirect(url_for("contacts"))
		return render_template("contacts.html", borrar_registro = borrar_registro)
	except:
		db.session.commit()
		flash("Hubo un error al intentar borrar este registro", "danger")
		return render_template("delete.html", borrar_registro=borrar_registro, id_delete=id_delete)
	
	return render_template("delete.html")

# LOGOUT
@app.route("/logout")
@login_required #Solo se puede editar con login
def logout():
   	logout_user()
   	flash("Sesión finalizada","warning")
   	return redirect(url_for("login"))

#CAMINO DE CR
@app.route("/caminocr")
@login_required #Solo se puede editar con login
def caminocr():
	date 	= 	datetime.now(timezone('America/Chicago'))
	title 	= 	"Camino de Costa Rica"
	return render_template("caminocr.html", title=title, date=date)

#MULTIMEDIA
@app.route("/videos")
def videos():
	date 	= 	datetime.now(timezone('America/Chicago'))
	title 	= 	"Camino de Costa Rica"
	return render_template("videos.html", title=title, date=date)

# REGISTRO
@app.route("/registro", methods=["GET","POST"]) 
def registro():
	date 	= 	datetime.now(timezone('America/Chicago'))
	titulo="Registro | Inicio"
	form = formularioRegistro()

	if request.method == "POST":
		username = User.query.filter_by(username=request.form["username"]).first()
		email = User.query.filter_by(email=request.form["email"]).first()
		
		if {form.password.data} is None:
			flash(f"El Mail no puede quedar vacio", "danger")
		elif {form.password.data} is None and {form.confirmpassword.data} is None:
			flash(f"El password no puede quedar vacio", "danger")
		elif {form.password.data} != {form.confirmpassword.data}:
			flash(f"La contraseña y la verificación NO son iguales", "danger")
		elif email:
			flash("""Email ya existen. intente con otro""", "warning")
		else:
			hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
	
			# CADA CAMBIO QUE SE REALICE EN FLASKFORM Y DB.MODELS HAY QUE ELIMINARLO O AGREGARLO AQUI	
			user = User(
				username 			=		form.username.data.title(), 
				apellido			=		form.apellido.data.title(),
				apellido2			=		form.apellido2.data.title(),
				residencia			=		form.residencia.data,
				email 				=		form.email.data.lower(), 
				telefono			=		form.telefono.data,
				telefonoE			=		form.telefonoE.data,
				celular				=		form.celular.data,
				password 			=		hashed_password, 
				confirmpassword 	=		hashed_password,
				alergias			=		form.alergias.data.title(),
				cronico				=		form.cronico.data.title(),
				medicamentos		=		form.medicamentos.data.title(),
				nacimiento			=		form.nacimiento.data,
				#  nombre			= 			campo
				)

			db.session.add(user)
			db.session.commit()
			flash(f"Cuenta creada por {form.username.data.upper()} {form.apellido.data.upper()}", "success")
			return redirect(url_for("login"))
	return render_template("registro.html", titulo=titulo, form=form, date=date)

# LOGIN
@app.route("/login", methods=["GET","POST"]) 
def login():
	titulo="Inicio "
	form = formularioLogin()
	date 	= 	datetime.now(timezone('America/Chicago'))
	if request.method == "POST":
		user = User.query.filter_by(email=form.email.data.lower()).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			# Caducidad de sesion con timedelta (from datetime import datetime, timedelta) para que funcione
			session.permanent = True
			app.permanent_session_lifetime = timedelta(minutes=5)
			session.modified = True
			login_user(user)
			flash(f"Hola {user.username.upper()}", "alert-primary")
			return redirect(url_for("home"))
		else:
			flash("CADUCADO", "alert-warning")
			return redirect("login")
		flash("Contraseña o Usuario invalidos", "danger")
	return render_template("login.html", titulo=titulo, form=form, date=date)

# CREAR POSTS
@app.route("/add-post", methods=["GET","POST"])
@login_required #Solo se puede editar con login
def add_post():
	form = PostForm() #PostForm es la clase modelo creada en la parte superior 	
	if request.method == "POST":
		poster = current_user.id
		post = Posts(
			titulo			=		form.titulo.data, 
			description		=		form.description.data, 
			content			=		form.content.data, 
			poster_id 		=		poster, 
			slug			=		form.slug.data)

		#Limpia el formulario
		form.title.data 	= 		""
		form.description.data = 	""
		form.content.data 	= 		""
		form.slug.data 		= 		""

		#Agregar el formulario a la db
		db.session.add(post)
		db.session.commit() 

		flash("Publicado correctamente", "success")
		return redirect("post")
	return render_template("add_Post.html", form=form)	

# EDITAR POSTS
@app.route("/posts/edit/<int:id>", methods=["GET","POST"])
@login_required #Solo se puede editar con login
def edit_post(id):
	post = Posts.query.get_or_404(id)
	form = PostForm() #PostForm es la clase modelo creada en la parte superior 
	if request.method == "POST":
		post.titulo			=		form.titulo.data 
		post.description	=		form.description.data
		post.content		=		form.content.data 
		post.slug			=		form.slug.data
		
		#Actualizar la base de datos
		db.session.add(post)
		db.session.commit()
		flash("El post ha sido modificado")
		return redirect(url_for('post', id=post.id))
	
	form.titulo.data		= 		post.titulo
	form.description.data 	= 		post.description
	form.content.data 		= 		post.content
	form.slug.data 			= 		post.slug
	return render_template("edit_post.html", form=form)

# BORRAR POSTS
@app.route("/posts/delete/<int:id>")
@login_required #Solo se puede editar con login
def delete_post(id):
	borrar_post = Posts.query.get_or_404(id)

	try:
		db.session.delete(borrar_post)
		db.session.commit()
		flash(f"El Post fué Eliminado", "success")
		return redirect(url_for("post"))
		return render_template("post.html", borrar_post = borrar_post)
	except:
		db.session.commit()
		flash("Hubo un error al intentar borrar este Post", "danger")
		return render_template("post.html", borrar_registro=borrar_registro, id_delete=id_delete)
	else:
		return render_template("post.html")
			
# VISUALIZAR POSTS
@app.route("/post")
@login_required #Solo se puede editar con login
def post():
	post = Posts.query.order_by(Posts.date_posted)
	return render_template("post.html", post=post)

# LEER POST INDIVIDUALMENTE
@app.route("/posts/<int:id>")
#@login_required
def posts(id):
	post = Posts.query.get_or_404(id)
	return render_template("posts.html", post=post)


#_______________________
# ALERTA DE ERRORES
# Error URL Invalida
@app.errorhandler(404)
# Error página no encontrada
def page_not_found(e):
	date 	= 	datetime.now(timezone('America/Chicago'))
	return render_template('404.html',date=date), 404

# Error Servidor Interno
@app.errorhandler(500)
# Servidor no encontrada
def server_not_found(e):
	date 	= 	datetime.now(timezone('America/Chicago'))
	return render_template('500.html',date=date), 500
# -----------------------








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






