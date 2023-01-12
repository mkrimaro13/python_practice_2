import filter
import reader
import chart

'''
Este Script, toma la información de los módulos en el paquete csvpractice, para la lectura y filtrado de un archivo csv sacado de www.kaggle.com sobre la población mundial, adicional imprime dos graficas utilizando la librería matplotlib.
'''


def run():
    data = reader.read_csv('data.csv')
    # data = list(filter(lambda item: item['Continent'] =='South America', data))

    # Me imprime únicamente la información de un solo país, es que le indique consultar
    country = input('Ingresa el país que deseas consultar: ').title()
    filtered_country = filter.country_filter(data, country)
    print(filtered_country)
    # Imprime únicamente la información de la población
    print(f'La información individual de la población de {country} es: ')
    filtered_population = filter.header_filter(filtered_country)
    print(filtered_population)
    # Genera el gráfico de barras del crecimiento del país
    labels = filtered_population.keys()
    values = filtered_population.values()
    chart.gen_bar_chart(country, labels, values)
    # Genera el gráfico de torta de la población por continente
    filtered_continent = filter.continent_filter(data)
    countries = list(map(lambda item: item['Country/Territory'], filtered_continent))
    percentage = list(map(lambda item: item['World Population Percentage'], filtered_continent))
    chart.gen_pie_chart(labels=countries, values=percentage)


if __name__ == '__main__':
    run()
