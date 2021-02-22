#Import dependencies
from flask import Flask, jsonify
import pymongo
#########################################################################################################################
# Flask Setup
#########################################################################################################################

#Create an app
app = Flask(__name__)

#########################################################################################################################
# FLASK ROUTES
#########################################################################################################################

@app.route("/")
def welcome(): 
        print("Server received request for 'Home' page...")
        return ( 
        f"Available api routes:<br/>" 
        f"/api/v1.0/precipitation : Precipitation percentages for the past year<br/>"
        f"/api/v1.0/stations : Unique stations<br/>"
        f"/api/v1.0/tobs : Temperatures for the most active station over the past year<br/>"
        f"/api/v1.0/<start> : User inputs given start date (yyyymmdd) to search for minimum, maximum, and average temperature <br/>"
        f"/api/v1.0/<start>/<end> : User inputs given start date (yyyymmdd) and end date (yyyymmdd) to search for minimum, maximum, and average temperature<br/>"
        )

#########################################################################################################################
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Perform a query to retrieve the data and precipitation scores and sort the dataframe by date
    precipitation_year = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).order_by(Measurement.date).all()
    
    prcp_list = list(np.ravel(precipitation_year))
    return jsonify(prcp_list)

    session.close()
    
#########################################################################################################################


   
if __name__ == "__main__":
    app.run(debug=True)