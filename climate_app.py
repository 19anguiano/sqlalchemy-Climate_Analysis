import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#######################################
# Database Setup
#######################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
Station = Base.classes.station

#######################################
# Flask Setup
#######################################
app = Flask(__name__)

#######################################
# Flask Routes
#######################################

@app.route("/")
def homepage():
    """List all available api routes."""
    return (
        f"WELCOME!<br/>"
        f"<br/>"
        f"This homepage is the hub for Hawaii Climate Analysis. Data ranges from 2016-08-23 Through 2017-08-23. Here are the available routes:<br/>"
        f"<br/>"
        f"<br/>"
        f"Precipitation Data:<br/>"
        f"http://localhost:5000/api/v1.0/precipitation<br/>"
        f"<br/>"
        f"Active Weather Stations:<br/>"
        f"http://localhost:5000/api/v1.0/stations<br/>"
        f"<br/>"
        f"Most Active Station Temperature Observations:<br/>"
        f"http://localhost:5000/api/v1.0/tobs<br/>"
        f"<br/>"
        f"Temperature Data Description for a Customized Start Date (Ex: http://localhost:5000/api/v1.0/2016-10-23):<br/>"
        f"http://localhost:5000/api/v1.0/<start><br/>"
        f"<br/>"
        f"Temperature Data Description for a Range of Dates (Ex: http://localhost:5000/api/v1.0/2016-10-23/2017-08-23):<br/>"
        f"http://localhost:5000/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Create session
    session = Session(engine)
    
    # Calculate the date one year from the recent date
    year_ago_date = dt.date(2017,8,23) - dt.timedelta(days = 365)
    
    # Query the data and precipitation scores
    results = session.query(measurement.date, measurement.prcp).filter(measurement.date >= year_ago_date).all()
    
    # Close Session                                                  
    session.close()
    
    # Create a dictionary using 'date' as the key and 'prcp' as the value and append to list prcp_data
    prcp_data = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict[date] = prcp
        prcp_data.append(prcp_dict)
        
    return jsonify(prcp_data)

@app.route("/api/v1.0/stations")
def stations():
    
    # Create session
    session = Session(engine)
    
    # Query data for all stations
    stations = session.query(Station.name, Station.station, Station.elevation, Station.latitude, Station.longitude).all()
    
    # Close Session                                                  
    session.close()
    
    # Create a dictionary append to list station_data
    station_data = []
    for name, station, elevation, latitude, longitude in stations:
        station_dict = {}
        station_dict["Name"] = name
        station_dict["Station ID"] = station
        station_dict["Elevation"] = elevation
        station_dict["Latitude"] = latitude
        station_dict["Longitude"] = longitude
        station_data.append(station_dict)
        
    return jsonify(station_data)

@app.route("/api/v1.0/tobs")
def tobs():
    
    # Create session
    session = Session(engine)
    
    # Calculate the date one year from the recent date
    year_ago_date = dt.date(2017,8,23) - dt.timedelta(days = 365)
    
    # Query the dates and temperature observations of the most active station 
    active_station = session.query(measurement.date, measurement.tobs).filter(measurement.station == 'USC00519281').\
                            filter(measurement.date >= year_ago_date).all()
    
    # Close Session                                                  
    session.close()
    
    # Create a dictionary and append to list most_active
    most_active = []
    for date, temp in active_station:
        active_dict = {}
        active_dict[date] = temp
        most_active.append(active_dict)
        
    return jsonify(most_active)

@app.route("/api/v1.0/<start>")
def start(start):

    # Create session
    session = Session(engine)
    
    # Query the minimum, maximum, and average temperature for a specified start date to the end of the dataset
    query_results = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
            filter(measurement.date >= start).all()
    
    # Close Session                                                  
    session.close()
    
    # Create a dictionary and append to list start_date
    start_date = []
    for min, max, avg in query_results:
        start_dict = {}
        start_dict["Minimum Temperature"] = min
        start_dict["Maxium Temperature"] = max
        start_dict["Average Temperature"] = avg
        start_date.append(start_dict)
        
    return jsonify(start_date)

@app.route("/api/v1.0/<start>/<end>")
def range_date(start,end):
    
    # Create session
    session = Session(engine)
    
    # Query the minimum, maximum, and average temperature for a specified start date to the end of the dataset
    query_results = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
            filter(measurement.date >= start).filter(measurement.date <= end).all()
    
    # Close Session                                                  
    session.close()
    
    # Create a dictionary and append to list range_date
    range_date = []
    for min, max, avg in query_results:
        range_dict = {}
        range_dict["Minimum Temperature"] = min
        range_dict["Maxium Temperature"] = max
        range_dict["Average Temperature"] = avg
        range_date.append(range_dict)
        
    return jsonify(range_date)
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)