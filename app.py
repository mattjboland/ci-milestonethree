import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'online-cookbook-milestonethree'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-olf6t.mongodb.net/online-cookbook-milestonethree?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def hello():
    return 'Hello World'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
