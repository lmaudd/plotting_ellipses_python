# imports
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# COC
def c_change(function, vc, uc):

    new_function = function.replace("v", f"({vc})").replace("u", f"({uc})").replace(" ", "")

    split_function = new_function.split("=")

    if "*" not in split_function[0]:
        if "/" not in split_function[0]:

            split_function[0] = split_function[0].replace("(", "").replace(")", "")

            if "y-" in split_function[0]:
                new_split_function = split_function[0].split("-")
                split_function[1] += f"+{new_split_function[1]}"
                complete_function = new_split_function[0] + "=" + split_function[1]

            elif "y+" in split_function[0]:
                new_split_function = split_function[0].split("+")
                split_function[1] += f"-{new_split_function[1]}"
                complete_function = new_split_function[0] + "=" + split_function[1]
                
            else:
                complete_function = new_function
                
            complete_function_final = complete_function.replace("y=", "")
            
            return(complete_function_final)

        else:
            print("ERROR")

    else:
        print("ERROR")

# Plot
def plot_cc(function, vc, uc):
    
    """
    function must be in terms of v = u
    vc must be y
    uc must be x
    """
    
    a = c_change(function, vc, uc)

    x = np.linspace(-10,100,20)
    y = eval(a)

    # Format plot
    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    #ax.set_title(title, fontsize=8)

    # Print and plot
    fig.tight_layout()
    plt.show()