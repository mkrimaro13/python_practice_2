import pandas as pd
import filter as flt
import chart as cht

def run():
        df = pd.read_csv('data.csv') # dataframe = donde va la información
        
        country = input('Ingresa el país que deseas consultar: ').title()
        filtered_country = filter.country_filter(df, country)
        print(filtered_country)
        # Imprime únicamente la información de la población
        print(f'La información individual de la población de {country} es: ')
        filtered_population = filter.header_filter(filtered_country)
        print(filtered_population)
        # Genera el gráfico de barras del crecimiento del país
        labels = filtered_population.keys()
        values = filtered_population.values()
        cht.gen_bar_chart(country, labels, values)
        # Genera el gráfico de torta de la población por continente
        df=df[df['Continent']=='Europe']
        filtered_continent = filter.continent_filter(df)
        countries = list(map(lambda item: item['Country/Territory'], filtered_continent))
        percentage = list(map(lambda item: item['World Population Percentage'], filtered_continent))
        cht.gen_pie_chart(labels=countries, values=percentage)
        

if __name__ == '__main__':
    run()