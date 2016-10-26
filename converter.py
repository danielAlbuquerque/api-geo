import subprocess
import shapefile
from json import dumps

def get_data(areas, view):
	areas = ','.join("'{0}'".format(g) for g in areas)	
	shp_file = to_shape(areas, view)
	return shp_file


def to_shape(glebas, view):
	cmd = 'ogr2ogr -a_srs EPSG:31976 -f "ESRI Shapefile" -where "NM_GLEBA in({glebas})" d:\\app_mapas\\shapes/{view}.shp OCI:"SHECMA/PASS@(DESCRIPTION = (ADDRESS_LIST= (ADDRESS = (PROTOCOL = TCP)(HOST = )(PORT = 1521)))(CONNECT_DATA = (SID = ))):SCHEMA.{view}" -progress'.format(view=view, glebas=areas)
	subprocess.call(cmd, shell=True)
	return to_geojson("{view}.shp".format(view=view))


def to_geojson(shp_file):
	cmd = 'ogr2ogr -f "GeoJSON" -t_srs crs:84 d:\\app_mapas\\geojson\\{shp_file}.geojson d:\\app_mapas\\shapes\\{shp_file}'.format(shp_file=shp_file)
	subprocess.call(cmd, shell=True)
	return "d:\\app_mapas\\geojson\\{shp_file}.geojson".format(shp_file=shp_file)