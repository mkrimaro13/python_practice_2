import matplotlib.pyplot as plt

def pie_chart():
    labels = ['A', 'B', 'C']
    values = [100, 200, 90]
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('charts/pie.png')
    plt.close()