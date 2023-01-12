import pandas as pd
import filter
import chart

def run():
        df = pd.read_csv('data.csv') # dataframe = donde va la información
        # print(df)
        country = input('Ingresa el país que deseas consultar: ').title()
        cdf = df[df['Country/Territory'] == country]
        print(cdf)
        df = df[df['Continent'] == 'Europe']
        

if __name__ == '__main__':
    run()