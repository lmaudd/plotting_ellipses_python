# plotting_ellipses_python
This is a collection of Python code I have written. It includes three files, one of which is a dependent for another. 

Math_format_functions.py is  file on which math_plotting_functions.py is based. It comprises one function that 
formats string into the equation of an ellipse. It is used in math_plotting_functions.py to display the function the graph is based on. 
I wan ed the user to have a more interactive experience while inputting their math function, as in they could see it update in real
time as they typed. I thought this could be done using a while loop that would constantly refresh and updat the  rint. I decided not to 
try it because it would seriously clutter the user's ter inal. It might be possible with more front-end coding.

Changes_of_coordinates.py is a disaster. It was supposed to be able to receive a function and a change of coordinates and then print the function
with the change of coordinates. It works, albeit in a very narrow scope of conditions. If there is too much deviation from the conditions in
which it works, it simply will malfunction without explaining why. I included the appropriate conditions in the docstring. 

I would like to come back to this and fix some of the errors later when I have time.
