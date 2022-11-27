import matplotlib.pyplot as plt


# Multiple lineplots with legend
def linePlots(dat, xLegend, yLegend, title):
    for i, d in enumerate(dat):
        plt.plot(d['timepoints'], d['positions'], label="Run "+ str(i+1))

    # Set axes labels and title.
    plt.xlabel(xLegend)
    plt.ylabel(yLegend)
    plt.title(title)
    plt.legend()
  
    # Display a figure.
    plt.show(block=False)