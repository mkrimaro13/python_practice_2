# import reader

def country_filter(data, country):
    filtered_country = list(filter(lambda item: item['Country/Territory'] == country, data))
    return filtered_country

def header_filter(data):
    filtered_headers = list(filter(lambda item: ' Population' in item[0] and ' Percentage' not in item[0], data[0].items())) # Esto me entrega una lista de tuplas
    fil_head_dict = {key[:4]:int(value) for (key, value) in filtered_headers}
    return fil_head_dict

def continent_filter(data):
    filtered_continent = list(filter(lambda item : item['Continent'] == 'South America', data))
    return filtered_continent

