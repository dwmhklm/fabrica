from flask import Flask as f

app = f(__name__)

from routes import *

if __name__ == "__main__":    
   app.run(debug=True)
   home()
