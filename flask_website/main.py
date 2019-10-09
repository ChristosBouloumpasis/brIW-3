from flask import Flask, jsonify, render_template, request

from source.load_database import *

app = Flask(__name__)

# people_tbl = populate_dict_from_db("people_tbl")
# preferences_tbl = populate_dict_from_db("preferences_tbl")
# drinks_tbl = populate_dict_from_db("drinks_tbl")


def get_people_dict():
    people_tbl = populate_dict_from_db("people_tbl")
    return people_tbl

def get_drinks_dict():
    drinks_tbl = populate_dict_from_db("drinks_tbl")
    return drinks_tbl

def get_pref_tbl():
    pref = populate_dict_from_db("preferences_tbl")
    return pref


@app.route("/")
def get_website():
    return render_template("index.html")

@app.route("/api/people")
def get_people():
    people_tbl = get_people_dict()
    return jsonify(people_tbl)

@app.route("/api/drinks")
def get_drinks():
    return jsonify(get_drinks_dict())

@app.route("/api/pref")
def get_pref():
    return jsonify(get_pref_tbl())

@app.route('/add-order', methods=['GET', 'POST'])
def submit_order():
    people_tbl = get_people_dict()
    if request.method == "GET":
        return render_template('neworder.html', title="Create order", people_tbl=people_tbl)

    elif request.method == "POST":
        person_id = request.form.get("person-name")
        drinks_tbl = get_drinks_dict()
        people_tbl = get_people_dict()
        preferences_tbl = get_pref_tbl()

        # search_peoples_name(person_name)
        round_id = get_active_round_id()

        if round_id == 0:
            create_round(int(person_id))
            round_id = get_active_round_id()
                    
        if int(person_id) in get_pref_tbl().keys():
            drink_id = get_pref_tbl()[int(person_id)]
            add_round_order(round_id, person_id, drink_id)

    return render_template("ordercomplete.html", title="Posted", people_tbl=people_tbl, preferences_tbl=preferences_tbl, drinks_tbl=drinks_tbl, person=int(person_id))

@app.route('/add-drink', methods=['GET', 'POST'])
def new_drink():
    if request.method == "GET":
        return render_template('add-drink.html', title="Create drink", input="Drink")

    elif request.method == "POST":
        drink_name = request.form.get("input-name")
        add_drink(drink_name)
        return render_template("drinkcomplete.html", title="Posted", input=drink_name)

@app.route('/add-person', methods=['GET', 'POST'])
def new_person():
    if request.method == "GET":
        return render_template('add-drink.html', title="Create person", input="Person")

    elif request.method == "POST":
        person_name = request.form.get("input-name")
        add_person(person_name)
        return render_template("drinkcomplete.html", title="Posted", input=person_name)

@app.route('/add-preference', methods=['GET', 'POST'])
def update_preference():
    drinks_tbl = get_drinks_dict()
    if request.method == "GET":
        people_tbl = get_people_dict()
        return render_template('add-pref.html', title="Update preference", people_tbl=people_tbl, drinks_tbl=get_drinks_dict())

    elif request.method == "POST":
        person_id = request.form.get("person-name")
        drink_id = request.form.get("drink-name")
        print(person_id + " " + drink_id)
        people_tbl = get_people_dict()

        if int(person_id) in get_pref_tbl().keys():
            modify_preferences(int(person_id), int(drink_id))

        else:
            print("else" + person_id + " " + drink_id)
            add_preferences(int(person_id), int(drink_id))

        return render_template("prefcomplete.html", title="Posted", people_tbl=people_tbl, drinks_tbl=drinks_tbl, person=int(person_id), drink=int(drink_id))

@app.route('/round', methods=['GET'])
def get_round_info():
    round_id = get_active_round_id()

    if round_id == 0:
        return render_template('error.html', title="Error", error="A round doesn't exist.")

    else:
        round_id = get_active_round_id()
        orderinfo = get_all_orders_in_round(round_id)
        roundinfo = get_a_rounds_info(round_id)
        people_tbl = get_people_dict()
        drinks_tbl = get_drinks_dict()

        return render_template('roundinfo.html', title="Round info", orderinfo=orderinfo, roundinfo=roundinfo, people_tbl=people_tbl, drinks_tbl=drinks_tbl)

@app.route('/endround', methods=['POST'])
def end_route():
    round_id = get_active_round_id()
    orderinfo = get_all_orders_in_round(round_id)
    roundinfo = get_a_rounds_info(round_id)

    if round_id >= 0:
        end_round(round_id)
        return render_template('roundend.html', title="Round Ended", orderinfo=orderinfo, roundinfo=roundinfo, people_tbl=get_people_dict(), drinks_tbl=get_drinks_dict())

    else:
        return render_template('error.html', title="Error", error="A round doesn't exist.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
