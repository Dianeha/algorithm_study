import sys
sys.stdin = open("input1.txt", "r")

def electric_bus(knm, bus_stops):
    step = knm[0]
    last_point = knm[1]
    num_bus_stop = knm[2]

    charging_count = 0
    current_location = 0
    i = 0
    while i < num_bus_stop:
        current_location += step

        if current_location >= last_point:
            return charging_count

        if current_location in bus_stops:
            charging_count += 1
            i = bus_stops.index(current_location)+1
        elif current_location < bus_stops[i]:
            return 0  # step 만큼 갔는데도 충전소가 더 멀리있어 충전할 수 없으면 0을 리턴
        else: # 이동할 수 있는 거리 내에 충전소가 있는 경우
            if i != (num_bus_stop-1):
                if bus_stops[i] < bus_stops[i+1] and bus_stops[i+1] < current_location:
                    i += 1
            charging_count += 1
            current_location = bus_stops[i]
            i += 1
    return charging_count

T = int(input())
for tc in range(1, T + 1):
    knm = list(map(int, input().split()))
    bus_stops = list(map(int, input().split()))
    print('#%d %d' % (tc, electric_bus(knm, bus_stops)))


