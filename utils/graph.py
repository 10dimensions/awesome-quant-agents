import matplotlib.pyplot as plt

def linePlots(dat, xLegend, yLegend, title):
    for i, d in enumerate(dat):
        print(d)
        plt.plot(d[0], d[1], label="Run "+ str(i))

    # Set axes labels and title.
    plt.xlabel(xLegend)
    plt.ylabel(yLegend)
    plt.title(title)
    plt.legend()
  
    # Display a figure.
    plt.show()