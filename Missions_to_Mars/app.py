#Import dependencies
from flask import Flask, jsonify, redirect, render_template
import scrape_mars
import pymongo
#########################################################################################################################
# Flask Setup
#########################################################################################################################

#Create an app
app = Flask(__name__)

#CREATE A FREE MONGO CLUSTER MONGODB
#  The default port used by MongoDB is 27017
conn = 'mongodb://localhost:27017/scraped_mars_info'
client = pymongo.MongoClient(conn)

#########################################################################################################################
# FLASK ROUTES
#########################################################################################################################

@app.route("/")
def welcome(): 
        db_pull = client.db.scraped_mars_info.find_one()
        print("Server received request for 'Home' page...")
        return render_template("index.html", mars= db_pull)

#########################################################################################################################

@app.route("/scrape")
def scraper(): 
        db = client.db.scraped_mars_info
        mars_data = scrape_mars.scrape()
        db.update({}, mars_data, upsert= True )
        return redirect("/") 
        

#########################################################################################################################
   
if __name__ == "__main__":
    app.run(debug=True)