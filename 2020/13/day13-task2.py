# with open("2020/13/day13testdata.txt") as f:
with open("2020/13/day13bustimes.txt") as f:
    data = f.read().splitlines()

time_now = int(data[0])
bus_ids = data[1]
bus_ids = bus_ids.split(",")
bus_ids = list(filter(lambda a: a != "x", bus_ids))
bus_ids = list(map(int, bus_ids))

print(time_now)
print(bus_ids)

next_time_to_bus = 999
next_bus_id = 0
times = {}

for bus_id in bus_ids:
    time_to_bus = bus_id - (time_now % bus_id)
    times[bus_id] = time_to_bus
    if time_to_bus < next_time_to_bus:
        next_bus_id = bus_id
        next_time_to_bus = time_to_bus

print(times)
print(next_bus_id)
print(next_time_to_bus)
print("answer =", next_bus_id * next_time_to_bus)