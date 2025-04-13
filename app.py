from flask import Flask 
from src.logger import logging
from src.exception import CustomException
import os, sys
app = Flask(__name__)

@app.route('/',methods= ['GET', 'POST'])
def index():
    try:
        logging.info("we are testing our second methods of logging")
        return "Welcome to My First Ml Project"
    except Exception as e:
        abc = CustomException(e, sys)
        logging.info(abc.error_message)
        return "Welcome to My happy Place"
        
if __name__ == "__main__":
    app.run(debug=True)