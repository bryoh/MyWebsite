import os
from flask import Flask
import flask_admin as admin
from flask_admin.contrib import fileadmin
from flask_admin.contrib.fileadmin import FileAdmin

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'


@app.route("/")
def index():
    return '<a href="/admin/"> click here </a>'

if __name__ == '__main__':
    path = f'{os.getcwd()}/static'
    FileAdmin.can_mkdir = False
    admin = admin.Admin(app, 'Welcome to your admin page')
    admin.add_view(fileadmin.FileAdmin(path, 'static'))
    app.run(debug=True)
