#I wan to define a functio nand import the necessary libraries to run analysis on data
import pandas
# need pandas to import dataset
import numpy
# need numpy for numerical analysis
import matplotlib.pyplot as plt
# need matplotlib.pyplot to plot data; visual representation of data
import csv
# need csv for file reading and writing
import os
import sys 
# need this in order to run dynamic inputs and outputs for code 
def np_from_csv(csv_file):
	 tmp_data = pandas.read_csv(csv_file, header =None) 
   	 data = tmp_data.to_numpy()
   	 return data
#This function will import a CSV file as pandas stored in data and then converting that into numpy
data= np_from_csv("Final-Project.csv") 
#Uploading data files for CO2 Emissions by Year
df = pd.read_csv("Final-Project.csv", names=['Year', "Total CO2 Emissions", "Emissions from solid fuel comsumption" , "Emissions from liquid fuel consumption", "Emissions from gas fuel consumption", "Emissions from cement production", "Emissions from gas flaring", "Per capita CO2 emissions (metric tons of carbon)", "Emissions from bunker fuels (not included in the totals)"])
#This code is going to define all the headers for each of my columns, making the code easier to understand and manipulate
def plot_column__vs_column(str(x), str(y)):
    x=input( "What column would you like to compare as x value (exact name of column):")
    y=input("What column would you like to compare as y value (exact name of column):")
    plt.plot(str(x), str(y))
    plt.axis([0, 12, 0, 100])
    z= input("What is the name of the x axis:")
    plt.xlabel(str(z))
    w=input("What is the name of the y axis:")
    plt.ylabel(str(w))
    v=input("What is the name of the plot:")
    plt.title(str(v))
    plt.show()
    return plot_column_vs_column (str(x), str(y)):
#This function is meant to dynamically take inputs from the columns and plot the data. It will take the columns specified and plot them against one another
#This helps improve my code prior because by adding headers, I can call entire columns to plot. 
#This improves my code, because I will be able to visualize and compare multiple values to do analysis
def total_CO2_emissions:
	sum = csv.reader(open("Final-Project.csv","rb"))
	sum.next()
	# to skip the header when doing the for loop 
	total = 0
	#This will start the value of total at 0 which is where we want to be when adding things together  
	b=input("What column number would you like (1,2,3, etc):")
	for column in sum:  
   		total += int(column[int(b)])
		print total
	#This for loop is also dynamic in that it will take any element value that corresponds with any row of the CSV file and add all of the values together
	#This will help figure out different trends in data, such as hisotrically what has contributed most to CO2 Emissions depending on type of fuel
with open('Final-Project.csv', mode = 'r', encoding = 'utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    occurrences = 0
    for row in reader:
        occurrences = occurences +1
    print('we have {} occurrences of values to a key.\n'.format(occurrences))
#This will help us count the file number of occurrences of data points of any given column. This will help determine the impact that different CO2 emissions 
#Have based on the type of emissions. This will also help us understand historically what has affected CO2 emissions as certain columns will have
#more data than others. 
Years= set([])
with open('Final-Project.csv', 'r') as csvfile: 
    extracted = csv.DictReader(csvfile)
    for line in extracted:
        Year.add(line['Year'])

yearcount = {} 
import csv 
with open('Final-Project.csv', 'r') as f: 
    my_csv = csv.DictReader(f)
    for line in my_csv:
        eachyear = line['year']
        yearcount[year] = yearcount.get(eachyear, 0)
        yearcount[year] = yearcount[eachyear] + 1
for year in Years:
    print(year, yearcount[eachyear])
#This function will help us get all of the years present in our data as well as the number of data points that they have. This begins with 
#a function that will take all of the years in the data set nad put them in a set. Next, the column year is counted and added together and printed.
#This will give the total amount of data per each year.

#Assert Conditions

print(total)
Assert(total)=25,000
#This would take the total sum of CO2 emissions and using the assert functions, we can test to see if our data is outputting the correct values. The 
#assert here would print an error which makes sense because the actual sum of all of the CO2 emissions is much larger than 25,000

