from source.load_database import *
from source.app import *
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
# from encoder import *

print(startOperation())

class SingleHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type','text/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()

        if self.path == '/':
            goodbye = ("HA nice try")
            jd = json.dumps(goodbye)
            self.wfile.write(jd.encode('utf-8'))

        if self.path == '/people':
            people = populate_dict_from_db('people_tbl')
            jd = json.dumps(people)
            print(jd)
            self.wfile.write(jd.encode('utf-8'))

        if self.path == '/people/preferences':
            preferences_readable = {}
            preferences = populate_dict_from_db('preferences_tbl')

            for key, value in preferences.items():
                person_name = people_tbl[key]
                drink_name = drinks_tbl[value]

            preferences_readable[person_name] = drink_name

            jd = json.dumps(preferences_readable)
            print(jd)
            self.wfile.write(jd.encode('utf-8'))


        if self.path == '/drinks':
            drinks = populate_dict_from_db('drinks_tbl')
            jd = json.dumps(drinks)
            print(jd)
            self.wfile.write(jd.encode('utf-8'))


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length))
            
        if self.path == '/people/add':
            person = (data["name"])
            add_person(person)

            self.send_response(201)
            self.end_headers()
        
        if self.path == '/people/remove':
            person = (data["id"])
            remove_person(person)

            self.send_response(202)
            self.end_headers()

        
        if self.path == '/drinks/add':
            drink = (data["name"])
            add_drink(drink)

            self.send_response(201)
            self.end_headers()

        if self.path == '/drinks/remove':
            drink = (data["id"])
            remove_drink(drink)

            self.send_response(202)
            self.end_headers()

if __name__ == "__main__":
    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, SingleHandler)
    print("Starting server")

    httpd.serve_forever()


