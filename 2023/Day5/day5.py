def parse_map(map_str):
    map_dict = {}
    for line in map_str.split('\n'):
        dest_start, src_start, length = map(int, line.split())
        for i in range(length):
            map_dict[src_start + i] = dest_start + i
    return map_dict

def convert_number(number, conversion_map):
    return conversion_map.get(number, number)

def find_lowest_location(seeds, maps):
    seed_to_soil = parse_map(maps['seed_to_soil_map'])
    soil_to_fertilizer = parse_map(maps['soil_to_fertilizer_map'])
    fertilizer_to_water = parse_map(maps['fertilizer_to_water_map'])
    water_to_light = parse_map(maps['water_to_light_map'])
    light_to_temperature = parse_map(maps['light_to_temperature_map'])
    temperature_to_humidity = parse_map(maps['temperature_to_humidity_map'])
    humidity_to_location = parse_map(maps['humidity_to_location_map'])

    min_location = float('inf')
    for seed in seeds:
        soil = convert_number(seed, seed_to_soil)
        fertilizer = convert_number(soil, soil_to_fertilizer)
        water = convert_number(fertilizer, fertilizer_to_water)
        light = convert_number(water, water_to_light)
        temperature = convert_number(light, light_to_temperature)
        humidity = convert_number(temperature, temperature_to_humidity)
        location = convert_number(humidity, humidity_to_location)
        min_location = min(min_location, location)

    return min_location

def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n\n')

    seeds = list(map(int, lines[0].split(': ')[1].split()))
    maps = {}

    for section in lines[1:]:
        title, values = section.split(':')
        maps[title.strip().replace('-', '_').replace(' ', '_')] = values.strip()

    return seeds, maps

def main(filename):
    seeds, maps = read_input_file(filename)
    lowest_location = find_lowest_location(seeds, maps)
    return lowest_location

print(main('input.txt'))

