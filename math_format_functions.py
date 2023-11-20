import numpy as np

# math formatting

def math_func(xn, xd, s, yn, yd, o):
    
    # lines
    l1 = ""
    for n in range(len(xn)+2):
        l1 += "–"   
    l2 = ""
    for n in range(len(yn)+2):
        l2 += "–"

    # spaces

    s1 = ""
    for n in np.arange((len(l1) - len(xn)) / 2):
        s1 += " "

    s2 = ""
    for n in np.arange((len(l1) - len(xn))/2 + 3 + (len(l2) - len(yn))/2):
        s2 += " "

    s3 = ""
    for n in np.arange((len(l1) - len(xd)) / 2):
        s3 += " "

    s4 = ""
    for n in np.arange((len(l1) - len(xd))/2 + 3 + (len(l2) - len(yd))/2):
        s4 += " "

    print(f"""
    {s1}{xn}{s2}{yn}
    {l1} {s} {l2} = {o}
    {s3}{xd}{s4}{yd}
    """)

def math_func_return(xn, xd, s, yn, yd, o):
    
    # lines
    l1 = ""
    for n in range(len(xn)+2):
        l1 += "–"   
    l2 = ""
    for n in range(len(yn)+2):
        l2 += "–"

    # spaces

    s1 = ""
    for n in np.arange((len(l1) - len(xn)) / 2):
        s1 += " "

    s2 = ""
    for n in np.arange((len(l1) - len(xn))/2 + 3 + (len(l2) - len(yn))/2):
        s2 += " "

    s3 = ""
    for n in np.arange((len(l1) - len(xd)) / 2):
        s3 += " "

    s4 = ""
    for n in np.arange((len(l1) - len(xd))/2 + 3 + (len(l2) - len(yd))/2):
        s4 += " "
        
    return(f"""
    {s1}{xn}{s2}{yn}
    {l1} {s} {l2} = {o}
    {s3}{xd}{s4}{yd}
    """)