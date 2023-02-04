# TC2008B. Sistemas Multiagentes y Gráficas Computacionales
# Python server to interact with Unity
# Sergio. Julio 2021

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
#import json


import numpy as np
#from boid import Boid

width = 30
height = 30

# Set the number of agents here:
# EN UNITY WIDTH = X, ¿HEIGHT = Z?
#flock = [Boid(*np.random.rand(2)*30, width, height) for _ in range(20)]

# FUNCIÓN PARA ACTUALIZAR LAS POSICIONES
'''def updatePositions():
    # VARIABLE GLOBAL (PARECE SER EL NUMERO DE AGENTES)
    global flock
    # ARRAY DE POSICIONES
    positions = []
    # POR CADA AGENTE EN LA LISTA DE FLOCK, 
    for boid in flock:
        ## boid.py ==> funcion para cambiar parametros iniciales
        boid.apply_behaviour(flock)
        # boid.py ==> función para actualizar los valores dados (posoción, velocidad)
        boid.update()
        # Verificar que no se salga de la cuadricula establecida
        pos = boid.edges()
        # Se agrega la posicion al array de posicion
        positions.append(pos)
        #print(type(pos))
    return positions

# Función para traducir las posicioens a un JSON
def positionsToJSON(ps):
    posDICT = []
    for p in ps:
        pos = {
            "x" : p[0],
            "z" : p[1],
            "y" : p[2]
        }
        posDICT.append(pos)
    return json.dumps(posDICT)'''

# Función para traducir los bool a un JSON
def doJson():
    with open("JSONServer/data.json") as json_file:
        roundaboutdata = json.load(json_file)
    #print(roundaboutdata)
    #print(json.dumps(roundaboutdata))
    #print("JSON1")
    return json.dumps(roundaboutdata)

def doJson2():
    with open("JSONServer/dataSems.json") as json2_file:
        roundaboutdata2 = json.load(json2_file)
    #print(roundaboutdata)
    #print(json.dumps(roundaboutdata))
    #print("JSON2")
    return json.dumps(roundaboutdata2)
    


class Server(BaseHTTPRequestHandler):
    
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        #post_data = self.rfile.read(content_length)
        post_data = json.loads(self.rfile.read(content_length))
        #logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     #str(self.path), str(self.headers), post_data.decode('utf-8'))
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), json.dumps(post_data))
        
        '''
        x = post_data['x'] * 2
        y = post_data['y'] * 2
        z = post_data['z'] * 2
        
        position = {
            "x" : x,
            "y" : y,
            "z" : z
        }

        self._set_response()
        #self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
        self.wfile.write(str(position).encode('utf-8'))
        '''
        
        #positions = updatePositions()
        #print(f'The postitions are {positions}')
        #print(positions) 
        print('\n')
        self._set_response()
        resp = "{\"carros\": " + doJson() + ",\"semaforos\": " + doJson2() + "}"
        #resp = json.dumps(roundaboutdata)
        #print(json.dumps(roundaboutdata))
        print(resp)
        self.wfile.write(resp.encode('utf-8'))


def run(server_class=HTTPServer, handler_class=Server, port=8585):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info("Starting httpd...\n") # HTTPD is HTTP Daemon!
    try:
       httpd.serve_forever()
    except KeyboardInterrupt:   # CTRL+C stops the server
        pass
    
    httpd.server_close()
    logging.info("Stopping httpd...\n")

if __name__ == '__main__':
    from sys import argv
    
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
