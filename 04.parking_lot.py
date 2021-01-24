n = int(input())
parking = []
for _ in range(n):
    data = input().split(", ")
    directions, car_number = data
    if directions == "IN":
        parking.append(car_number)
    elif directions == "OUT":
        parking.remove(car_number)
parking = set(parking)
if parking:
    for el in parking:
        print(el)
else:
    print("Parking Lot is Empty")