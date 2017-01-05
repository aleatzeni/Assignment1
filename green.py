import matplotlib.pyplot as plt
from Classes.greengraph import Greengraph

def Green(start, end, steps):
    """ Generate a graph showing the proportion of green
		# pixels in a series of satellite images between two points.

    Parameters
    ----------
    start: str
       # Name of a starting location, such as London 
    end: str
       # Name of an ending location, such as Cambridge
    steps: int
       # Number of steps between the two endpoints
    Returns
    -------
    Plot
       # Graph of green pixels between two endpoints
    """
	
    #Test for input insanity
    if type(start) is not str:
        raise TypeError("Start should be a string of characters.")
    if type(end) is not str:
        raise TypeError("End should be a string of characters.")
    if steps < 0:
        raise ValueError("Steps should be a *positive* integer.")
    if type(steps) is not int:
        raise TypeError("Steps should be a *positive* integer.")
    mygraph= Greengraph(start, end)
    data = mygraph.green_between(steps)
    graph=plt.plot(data)
    plt.savefig('file.png')
    return graph