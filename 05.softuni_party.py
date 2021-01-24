n = int(input())

guest = []
for _ in range(n):
    guest.append(input())

while True:
    reservation = input()
    if reservation == "END":
        break
    if reservation in guest:
        guest.remove(reservation)
vip = []
regular = []
for el in guest:
    if el[0].isdigit():
        vip.append(el)
    else:
        regular.append(el)
vip.sort()
regular.sort()
print(len(vip) + len(regular))
for vip_guest in vip:
    print(vip_guest)
for regular_guest in regular:
    print(regular_guest)