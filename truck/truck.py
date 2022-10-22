# Parse problem
from heapq import heappush, heappop

test_cases = int(input())
class TruckState:
    def __init__(self, station_id, liters_left, total_cost):
        self.station_id = station_id
        self.liters_left = liters_left
        self.total_cost = total_cost

class Station:
    def __init__(self, liters, price):
        self.liters = liters
        self.price = price


for case in range(test_cases):
    num_stations, tank_capacity, cost_origin = input().split(" ")
    num_stations = int(num_stations)
    tank_capacity = int(tank_capacity)
    cost_origin = int(cost_origin)
    stations = []
    for station in range(num_stations):
        liters, price = input().split(" ")
        liters = int(liters)
        price = int(price)
        stations.append(Station(liters=liters, price=price))
    nodes = []
    cost = cost_origin * tank_capacity
    state = TruckState(station_id=-1, liters_left=tank_capacity, total_cost=cost)
    solution = None
    heappush(nodes, (-cost, state))
    if num_stations == 1:
        print(cost)
        continue
    while len(nodes) > 0:
        (cost, state) = heappop(nodes)
        if solution is not None and state.total_cost >= solution:
            continue
        next_station = stations[state.station_id+1]
        if next_station.liters > state.liters_left:
            # Not enought fuel for this the next station
            continue
        # Fill the tank
        liters_left = state.liters_left - next_station.liters
        next_state = TruckState(
            station_id=state.station_id+1,
            liters_left=tank_capacity,
            total_cost=state.total_cost + 500 + (tank_capacity-liters_left)*next_station.price
        )
        if next_state.station_id == num_stations-1:
            # Solved
            if solution is None or solution > next_state.total_cost:
                solution = next_state.total_cost
        else:
            if solution is None or next_state.total_cost < solution:
                heappush(nodes, (-(next_state.total_cost/(next_state.station_id+1)), next_state))

        # Do not fill
        next_state = TruckState(
            station_id=state.station_id+1,
            liters_left=state.liters_left-next_station.liters,
            total_cost=state.total_cost
        )
        if next_state.station_id == num_stations - 1:
            # Solved
            if solution is None or solution > next_state.total_cost:
                solution = next_state.total_cost
        else:
            if solution is None or next_state.total_cost < solution:
                heappush(nodes, (-(next_state.total_cost/(next_state.station_id+1)), next_state))

    print(solution)






