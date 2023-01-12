import pandas as pd
import filter as flt
import chart as cht
import reader as rdr

def run():
        df = pd.read_csv('data.csv') # dataframe = donde va la información
        country = input('Ingresa el país que deseas consultar: ').title()
        filtered_country = flt.country_filter(df, country)
        print(filtered_country)
        print(f'La información individual de la población de {country} es: ')
        filtered_population = filter.header_filter(filtered_country)
        print(filtered_population)
        df = df[df['Continent'] == 'South America'] # == filtered_continent = list(filter(lambda item : item['Continent'] == 'South America', data)), filtra por continente
        countries = df['Country/Territory'].values # countries = list(map(lambda item: item['Country/Territory'], filtered_continent))
        percentages = df['World Population Percentage'].values # percentage = list(map(lambda item: item['World Population Percentage'], filtered_continent))
        cht.gen_pie_chart(labels=countries, values=percentages)
        

if __name__ == '__main__':
    run()