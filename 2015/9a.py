with open("input9.txt") as f:
    data = f.read().splitlines()
cities = {}
for line in data:
    line = line.split(" ")
    if not cities.has_key(line[0]):
        cities[line[0]] = {}
    if not cities.has_key(line[2]):
        cities[line[2]] = {}
    cities[line[0]][line[2]] = line[4]
    cities[line[2]][line[0]] = line[4]

shortest_route = 0

for city in cities:
    route = 0
    not_visited = cities.keys()
    not_visited.remove(city)
    current_city = city
    
    while len(not_visited) > 0:
        shortest = 0
        next = current_city
        for neighbour in cities[current_city]:
            if int(cities[current_city][neighbour]) > int(shortest) and neighbour in not_visited:
                shortest = cities[current_city][neighbour]
                next = neighbour
        route += int(shortest)
        current_city = next
        not_visited.remove(current_city)

    if route > shortest_route or shortest_route == 0:
        shortest_route = route

print shortest_route
    