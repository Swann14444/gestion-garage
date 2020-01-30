import json


class Clients:

    def __init__(self, name, first_name, car, road, zip_code, city, id):
        self.name = name
        self.first_name = first_name
        self.car = car
        self.road = road
        self.zip_code = zip_code
        self.city = city
        self.id = id

    def toJSON(self):

        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

