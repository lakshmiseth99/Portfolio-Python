# Portfolio-Python


n VS CODE:


PS C:\Users\laksh\Documents\PYTHON> cd C:\Users\laksh\Documents\PYTHON\WebServer                                                           
PS C:\Users\laksh\Documents\PYTHON\WebServer> cd .venv                    
PS C:\Users\laksh\Documents\PYTHON\WebServer\.venv> cd Scripts                                                                             
PS C:\Users\laksh\Documents\PYTHON\WebServer\.venv\Scripts> ./activate                     
(.venv) PS C:\Users\laksh\Documents\PYTHON\WebServer\.venv\Scripts> 
(.venv) PS C:\Users\laksh\Documents\PYTHON\WebServer> $env:FLASK_APP = "server.py"   
(.venv) PS C:\Users\laksh\Documents\PYTHON\WebServer> flask run




If its in pythonAnywhere:

# +++++++++++ FLASK +++++++++++
# Flask works like any other WSGI-compatible framework, we just need
# to import the application.  Often Flask apps are called "app" so we
# may need to rename it during the import:
#
#
import sys
#
## The "/home/sethulak" below specifies your home
## directory -- the rest should be the directory you uploaded your Flask
## code to underneath the home directory.  So if you just ran
## "git clone git@github.com/myusername/myproject.git"
## ...or uploaded files to the directory "myproject", then you should
## specify "/home/sethulak/myproject"
path = '/home/sethulak/Portfolio-Python'
if path not in sys.path:
    sys.path.append(path)

from server import app as application  # noqa
#
# NB -- many Flask guides suggest you use a file called run.py; that's
# not necessary on PythonAnywhere.  And you should make sure your code
# does *not* invoke the flask development server with app.run(), as it
# will prevent your wsgi file from working.
