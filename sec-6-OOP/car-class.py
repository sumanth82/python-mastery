class FavCar:
    def __init__(self, model, make):
        self.model = model
        self.make = make


apoorva_car_model = FavCar('Honda', 'Civic')
sumant_car_model = FavCar('Subaru', 'Forester')

print(apoorva_car_model)

#O/P: <__main__.FavCar object at 0x10883b290>

print(apoorva_car_model.model)
# O/P: Honda

print(apoorva_car_model.make)

#O/P: Civic

print(sumant_car_model)

#O/P: <__main__.FavCar object at 0x10883b2d0>

print(sumant_car_model.model)

# O/P: Subaru

print(sumant_car_model.make)

#O/P: Forester


