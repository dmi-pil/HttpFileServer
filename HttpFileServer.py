import  http.server
import  socketserver
import sys
#from threading import Thread

port = 9090

def recive():

    Handler = http.server.SimpleHTTPRequestHandler
    server = socketserver.TCPServer(("10.10.1.23",port),Handler)
    ip, PORT = server.server_address
    print("server is running ",ip,"port ",PORT)
    return server

connection = recive()
try:
    connection.serve_forever()
except KeyboardInterrupt:
    print(" server is down ")
    sys.exit(0)



