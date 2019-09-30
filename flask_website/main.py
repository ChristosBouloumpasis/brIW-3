from flask import Flask, jsonify, render_template, request

from source.load_database import *

app = Flask(__name__)

people_tbl = populate_dict_from_db("people_tbl")
preferences_tbl = populate_dict_from_db("preferences_tbl")
drinks_tbl = populate_dict_from_db("drinks_tbl")

@app.route("/")
def get_website():
    return render_template("index.html")

@app.route("/api/people")
def get_people():
    people = populate_dict_from_db('people_tbl')
    return jsonify(people)

@app.route("/api/drinks")
def get_drinks():
    return jsonify(drinks_tbl)

@app.route('/submit', methods=['GET', 'POST'])
def submit_order():
    if request.method == "GET":
        return render_template('neworder.html', title="Create Form", people_tbl=people_tbl)

    elif request.method == "POST":
        person_name = request.form.get("person-name")
        search_person_name(person_name)
        return render_template("ordercomplete.html", title="Posted", people_tbl=people_tbl, person=int(person_name), preferences_tbl=preferences_tbl, drinks_tbl=drinks_tbl)


if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
