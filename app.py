from flask import Flask
import sys
from housing import exception, logger
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("we are trying to ")
    except Exception as e:
        housing = exception.HousingException(e, sys)
        logger.logging.info(housing.error_message)
        logger.logging.info("adfadfa")

    return "CI CD pipeline has been established. Hello There"


if __name__=="__main__":
    app.run(debug=True)
