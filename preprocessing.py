import os
import subprocess
import numpy as np
import pandas as pd
import scipy


## Generating x-coordinates
N=200
x_new=[]
for i in range(1,101):
    teta = np.pi*(i-1)/N
    x = 1-np.cos(teta)
    x_new.append(x)

## Generating y-coordinates
airfoils_list = ["naca0010", "naca0015", "naca0018", "naca0021", "naca0024", "naca000834", "naca001034", "naca001035",
                 "naca001064", "naca001065", "naca001066", "naca001234", "naca001264"]

re_all=[]
cl_all=[]
alpha_all=[]
y_all=[]
y_all=pd.DataFrame(y_all)
y_mid=[]
for airfoil_name in airfoils_list:
    airfoil = np.loadtxt(f"E:/Projects/Python/ML/LiftPrediction/AirfoilsSource/{airfoil_name}.dat", skiprows=1)
    airfoil = np.array(airfoil)
    m = int((len(airfoil)+1)/2)
    x_up = airfoil[:m,0]
    y_up = airfoil[:m,1]
    x_down = airfoil[m:,0]
    y_down = airfoil[m:,1]

    ## Spline Interpolation
    ## y_down_new
    tck=scipy.interpolate.splrep(x_down,y_down)
    y_down_new = scipy.interpolate.splev(x_new,tck)
    ## y_up_new
    x_up_flip = np.flip(x_up)
    y_up_flip = np.flip(y_up)
    tck=scipy.interpolate.splrep(x_up_flip,y_up_flip)
    y_up_new_zo = scipy.interpolate.splev(x_new,tck)
    y_up_new=np.flip(y_up_new_zo)
    ## together
    y_down_new=y_down_new.tolist()
    y_up_new = y_up_new.tolist()
    y_down_new.extend(y_up_new)
    y_new =[]
    y_new.append(y_down_new)
    y_new=pd.DataFrame(y_new)

    ### XFoil ###
    iteration=100
    alpha_i=-10
    alpha_f=10
    alpha_step=1
    for Re in range(500000, 5500000, 500000):
        if os.path.exists(f"{airfoil_name}_{Re}.txt"):
            os.remove(f"{airfoil_name}_{Re}.txt")
        input_file = open("input_xfoil.in", "w")
        input_file.write(f"{airfoil_name}\n")
        input_file.write("oper\n")
        input_file.write("visc{0}\n". format(Re))
        input_file.write("pacc\n")
        input_file.write(f"{airfoil_name}_{Re}.txt\n\n")
        input_file.write("iter{0}\n".format(iteration))
        input_file.write("aseq{0} {1} {2}\n".format(alpha_i, alpha_f, alpha_step))
        input_file.write("\n\n")
        input_file.write("quit\n")
        input_file.close()

        subprocess.call("E:/Projects/XFOIL6.99/xfoil.exe < input_xfoil.in", shell=True)

        result=np.loadtxt(f"{airfoil_name}_{Re}.txt", skiprows=12)
        result=np.array(result)
        alpha = result[:,0]
        cl= result[:,1]
        cl_all.extend(cl)
        alpha_all.extend(alpha)
        y_all = pd.concat([y_all]+ len(cl) * [y_new])
        for n in range(len(cl)):
            re_all.append(Re)


AirfoilData=pd.DataFrame(y_all)
AirfoilData.to_csv("AirfoilData.csv")
ReAlphaCl=pd.DataFrame(data=[re_all, alpha_all, cl_all]).T
columns=["Re", "Alpha", "Cl"]
ReAlphaCl.columns=columns
ReAlphaCl.to_csv("ReAlphaCl.csv")
print(np.array(AirfoilData).shape)
print(np.array(ReAlphaCl).shape)