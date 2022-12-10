
with open('2019/day_6/input.txt', 'r') as input_file:
    map_orbits = input_file.read().splitlines()
    map_orbits = [orbit.split(')') for orbit in map_orbits]
    # print(map_orbits)

orbits = {}
for orbit in map_orbits:
    if orbit[1] not in orbits.keys():
        orbits[orbit[1]] = {orbit[0]}
    else:
        orbits[orbit[1]].add(orbit[0])

# print(orbits)

changed = True
while changed:
    changed = False
    
    for target_object, orbiting_objects in orbits.items():
        for orbiting_object in orbiting_objects:
            if orbiting_object in orbits.keys():
                old_orbits = orbits[target_object].copy()
                orbits[target_object] |= orbits[orbiting_object]
                if orbits[target_object] != old_orbits:
                    changed = True
                break

# print(orbits)

count = 0
for _, orbiting_objects in orbits.items():
    count += len(orbiting_objects)

print(count)
