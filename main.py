
from flask import Flask, render_template, request
from classes import Clients

app = Flask(__name__)


@app.route('/')
def accueil():
    return render_template('accueil.html')


@app.route('/Garage/factures')
def factures():
    liste_clients = []
    with open("data_folder/clients.txt", "r") as clients_file:
        line = clients_file.readline()
        while line:
            line = line.split(';')
            name = line[0]
            first_name = line[1]
            car = line[2]
            road = line[3]
            zip_code = line[4]
            city = line[5]
            liste_clients.append(Clients(name, first_name, car, road, zip_code, city))
            line = clients_file.readline()
    liste_clients.sort(key=lambda clients: clients.name)
    return render_template('factures.html', clients=liste_clients)


@app.route('/Garage/updateFactures', methods=['GET', 'POST'])
def updateFactures():
    liste_clients = []
    with open("data_folder/clients.txt", "r") as clients_file:
        line = clients_file.readline()
        while line:
            line = line.split(';')
            name = line[0]
            first_name = line[1]
            car = line[2]
            road = line[3]
            zip_code = line[4]
            city = line[5]
            liste_clients.append(Clients(name, first_name, car, road, zip_code, city))
            line = clients_file.readline()
    liste_clients.sort(key=lambda clients: clients.name)

    return render_template('factures.html', clients=liste_clients)


@app.route('/Garage/clients')
def clients():
    liste_clients = []
    with open("data_folder/clients.txt", "r") as clients_file:
        line = clients_file.readline()
        while line:
            line = line.split(';')
            name = line[0]
            first_name = line[1]
            car = line[2]
            road = line[3]
            zip_code = line[4]
            city = line[5]
            liste_clients.append(Clients(name, first_name, car, road, zip_code, city))
            line = clients_file.readline()
    liste_clients.sort(key=lambda clients: clients.name)
    return render_template('clients.html', clients=liste_clients)


@app.route('/Garage/devis')
def devis():
    return render_template('devis.html')


@app.route('/Garage/vehicules')
def vehicules():
    return render_template('vehicules.html')


@app.route('/Garage/fournisseurs')
def fournisseurs():
    return render_template('fournisseurs.html')


@app.route('/Garage/catalogue')
def catalogue():
    return render_template('catalogue.html')


@app.route('/updateClient', methods=['GET', 'POST'])
def updateClient():
    liste_clients = []
    with open("data_folder/clients.txt", "r") as clients_file:
        line = clients_file.readline()
        while line:
            line = line.split(';')
            name = line[0]
            first_name = line[1]
            car = line[2]
            road = line[3]
            zip_code = line[4]
            city = line[5]
            liste_clients.append(Clients(name, first_name, car, road, zip_code, city))
            line = clients_file.readline()
    if request.method == 'POST':
        name = request.form['name']
        first_name = request.form['first_name']
        car = request.form['car']
        road = request.form['road']
        zip_code = request.form['zip_code']
        city = request.form['city']
        clients_file = open("data_folder/clients.txt", "a")
        clients_file.write(name + ";" + first_name + ";" + car + ";" + road + ";" + zip_code + ";" + city + "\n")
        clients_file.close()
        liste_clients.append(Clients(name, first_name, car, road, zip_code, city))
    liste_clients.sort(key=lambda clients: clients.name)
    return render_template('clients.html', clients=liste_clients)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
