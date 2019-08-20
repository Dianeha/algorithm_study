import sys
sys.stdin = open("input1.txt", "r")

def electric_bus(knm, bus_stops):
    step = knm[0]
    last_point = knm[1]
    num_bus_stop = knm[2]

    charging_count = 0
    current_location = 0
    able_to_go = step
    for i in range(1, last_point+1):
        current_location += 1
        able_to_go -= 1
        if current_location in bus_stops:
            n = bus_stops.index(current_location)
            if n == (num_bus_stop-1) and able_to_go != 0:
                return charging_count
            if bus_stops[n+1]-bus_stops[n] > able_to_go:
                charging_count += 1
                able_to_go = step
        else:
            if able_to_go == 0:
                return 0
            continue
    return charging_count

T = int(input())
for tc in range(1, T + 1):
    knm = list(map(int, input().split()))
    bus_stops = list(map(int, input().split()))
    print('#%d %d' % (tc, electric_bus(knm, bus_stops)))



