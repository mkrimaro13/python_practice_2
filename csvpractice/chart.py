import matplotlib.pyplot as plt

# Gráfico de barras
def gen_bar_chart(name='bar', labels=1, values=1): 
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'images/{name}.png') # Se deben crear las carpetas donde se espera que se guarde el archivo
    plt.close()

# Gráfico de torta
def gen_pie_chart(name='pie', labels=1, values=1):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig(f'images/pie_{name}.png') 
    plt.close()