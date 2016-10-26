from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
import database
import geo_converter

app = Flask(__name__)
CORS(app)

@app.route('/maps')
def maps():
	return database.maps()


@app.route("/areas")
def areas():
	return database.areas()


@app.route("/geojson", methods=['POST'])
def geojson():
	data = request.get_json(silent=True) 
	geojson_file = geo_converter.get_data(data['glebas'], data['view'])
	return send_file(geojson_file)


@app.route("/kml", methods=['POST'])
	pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')