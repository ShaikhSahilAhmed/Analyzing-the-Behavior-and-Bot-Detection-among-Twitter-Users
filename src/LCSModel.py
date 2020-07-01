import matplotlib.pyplot as plt
import scipy
import pandas as pd
import numpy
from scipy.optimize import curve_fit



col_list = ['num_of_strings', 'lcs_length']
source_file_path = "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\user_content_b6_lcs.csv"
lcs_df = pd.read_csv(source_file_path, usecols = col_list)

x = lcs_df['num_of_strings']
y = lcs_df['lcs_length']
plt.figure(figsize=(9, 6))
plt.plot(x, y, label='Data')
plt.xlabel('no. of strings')
plt.ylabel('length')
plt.title("Data")
plt.show()


plt.plot(x, y, ".", label="Data");

def func(x, a, b, offset): 
    return  a / numpy.power(x, b) + offset

# these are the same as the scipy defaults
initialParameters = numpy.array([1.0, 1.0, 1.0])

fittedParameters, pcov = curve_fit(func, x, y, initialParameters, maxfev=5000)

modelPredictions = func(x, *fittedParameters)

absError = modelPredictions - y

SE = numpy.square(absError) # squared errors
MSE = numpy.mean(SE) # mean squared errors
RMSE = numpy.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (numpy.var(absError) / numpy.var(y))

print('Parameters:', fittedParameters)
print('RMSE:', RMSE)
print('R-squared:', Rsquared)

print()


#plotting of curve
def ModelAndScatterPlot(graphWidth, graphHeight):
    f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    axes = f.add_subplot(111)

    # first the raw data as a scatter plot
    axes.plot(x, y,  'D')

    # create data for the fitted equation plot
    xModel = numpy.linspace(min(y), max(x), 1000)
    yModel = func(xModel, *fittedParameters)

    # now the model as a line plot
    axes.plot(xModel, yModel)

    axes.set_xlabel('Accounts') # X axis data label
    axes.set_ylabel('LCS') # Y axis data label

    plt.xscale('log') # comment this out for default linear scaling

    plt.title("User content b6 LCS")
    plt.show()
    plt.close('all') # clean up after using pyplot
    
    
graphWidth = 600
graphHeight = 400
ModelAndScatterPlot(graphWidth, graphHeight)






