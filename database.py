import cx_Oracle
import simplejson

con_oracle = cx_Oracle.connect(u'schema/password@database')

def check_user(username, password):
	pass


def glebas():
	glebas = []
	cursor = con_oracle.cursor()
	#Example query
	sql = """
		select id_gleba, nm_gleba from florestal.gleba 
		where exists(select id_gleba from florestal.talhao where dt_extinsao_talhao is null and id_gleba is not null)
		order by nm_gleba"""
	cursor.execute(sql)
	for gleba in cursor:
		row = {
			'id_gleba': gleba[0],
			'nm_gleba': gleba[1]
		}
		glebas.append(row)
	return simplejson.dumps(glebas)


def maps():
	mapas = []
	cursor = con_oracle.cursor()
	#Example query
	cursor.execute('select id, nome, descricao, visao from mapas order by nome')
	for mapa in cursor:
		row = {
			'id':        mapa[0],
			'nome': 	 mapa[1],
			'descricao': mapa[2],
			'view':      mapa[3],
		}
		mapas.append(row)
	return simplejson.dumps(mapas)