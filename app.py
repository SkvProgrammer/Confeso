from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
import pytz

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config["MONGO_URI"] = "mongodb+srv://satyamkumarverman:GQVEhFHLlykNsUgr@twitty.mylyp.mongodb.net/your_database_name?retryWrites=true&w=majority"
mongo = PyMongo(app)

# Test the MongoDB connection
@app.before_first_request
def test_connection():
    if mongo.db is None:
        print("MongoDB connection failed!")
    else:
        print("MongoDB connection successful.")

# Home route to display confessions feed
@app.route('/')
def index():
    confessions = list(
        mongo.db.confessions.find({'is_deleted': False}).sort('timestamp', -1)
    )
    return render_template('index.html', confessions=confessions)

# Route to post a new confession
@app.route('/post_confession', methods=['POST'])
def post_confession():
    content = request.form.get('content')
    if content:
        mongo.db.confessions.insert_one({
            'content': content,
            'is_deleted': False,
            'timestamp': datetime.now(pytz.utc).astimezone(pytz.timezone('Asia/Kolkata')
)  # Save the current time when the confession is posted
        })
        return redirect(url_for('index'))
    return 'Error: Content cannot be empty'

# No delete or edit functionality available now.
# The routes for deleting and editing are removed.

if __name__ == "__main__":
    app.run(debug=True)
