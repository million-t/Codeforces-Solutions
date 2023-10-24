cities, capacity = map(int, input().split())


cost = min(cities - 1, capacity)
cur_fuel = capacity

for i in range(2, cities + 1):
    cur_fuel -= 1

    if cur_fuel >= cities - i:
        break

    cost += i
    cur_fuel += 1

print(cost)