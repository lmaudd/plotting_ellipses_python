import numpy as np
import matplotlib.pyplot as plt
from math_format_functions import math_func_return

def plot_ellipse(xn,xd,yn,yd):

    title = math_func_return(f"({xn})^2", xd, "+", f"({yn})^2", yd, "1")
    
    # Radius of ellipse
    xr = np.sqrt(int(xd))
    yr = np.sqrt(int(yd))

    # x and y shift
    
    if "+" in xn:
        xn_s = xn.split("+")
        xs = int(xn_s[1])
    elif "-" in xn:
        xn_s = xn.split("-")
        xs = -1 * int(xn_s[1])
    else:
        xs = 0 
    
    if "+" in yn:
        yn_s = yn.split("+")
        ys = int(yn_s[1])
    elif "-" in yn:
        yn_s = yn.split("-")
        ys = -1 * int(yn_s[1])
    else:
        ys = 0
    
    # Acquiring Values for x and y
    t = np.linspace(0, 2 * np.pi, 100)
    x = xr * np.cos(t)
    y = yr * np.sin(t)

    # Format plot
    fig, ax = plt.subplots()
    ax.plot(x - xs, y - ys)
    ax.set_aspect('equal','box')
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    #ax.set_title(title, fontsize=8)

    # Print and plot
    print(f"Function:\n{title}")
    fig.tight_layout()
    plt.show()
