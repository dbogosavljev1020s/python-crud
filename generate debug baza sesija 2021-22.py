import os
import time

dir_path = os.path.dirname(os.path.realpath(__file__))
pname = input("Enter the project name: ")

os.system("mkdir " + pname)
os.chdir(dir_path + "\\" + pname)
with open("internal_install.bat", "w") as f:
	command = "python -m venv venv"
	command += " & venv\\Scripts\\activate"
	command += " & pip install flask"
	command += " & pip install flask-cors"
	command += " & pip install pymongo"
	command += " & pip install dnspython"
	command += " & pip install mysql-connector"
	command += " & pip install bson"
	command += " & pip install hashlib\n"
	f.write(command)
	
os.system("internal_install")
os.remove("internal_install.bat")

os.system("mkdir src")
os.chdir(dir_path + "\\" + pname + "\\src")
with open("main.py", "w") as f:
	command = """
from flask import Flask,render_template,request,session
import mysql.connector
app = Flask(__name__)
app.config['SECRET_KEY'] = "RAF2021-2022"
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="", # ako niste nista menjali u phpmyadminu ovo su standardni
    # username i password
	database="naziv_baze" # iz phpmyadmin 
    )

@app.route('/')
def index():
    return 'Hello world'


app.run(debug=True)
"""
	f.write(command)

os.system("mkdir templates")
os.chdir(dir_path + "\\" + pname + "\\src\\templates")
with open("index.html", "w") as f:
	html = []
	html.append("<html>")
	html.append("	<head>")
	html.append("		<title> Home Page </title>")
	html.append("	</head>")
	html.append("	<body>")
	html.append("		<p> Hello, World! from Home Page </p>")
	html.append("	</body>")
	html.append("</html>")
	f.write("\n".join(html))
	
os.chdir(dir_path + "\\" + pname)
	
with open("start_console.bat", "w") as f:
	command = "start venv\\Scripts\\activate\n"
	f.write(command)
	
with open("start_flask_server.bat", "w") as f:
	command = "venv\\Scripts\\activate & python src\\main.py"
	f.write(command)
	
with open("README.txt", "w") as f:
	text = []
	text.append('[Web Sistemi i Tehnologije]')
	text.append('')
	text.append('Skripta start_console.bat pokrece konzolu u novom virtual enviromentu za trenutni projekat')
	text.append('Skripta start_flask_server.bat pokrece main.py skriptu unutar src foldera')
	text.append('')
	text.append('Za sve dodatne informacije: dsijacic@raf.rs')
	f.write("\n".join(text))
	
print("Install done")























