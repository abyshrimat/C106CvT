import csv 
import numpy as np 
def getDataSource(data_path): 
    Marks_In_Percentage = [] 
    Days_Present = [] 
    with open(data_path) as csv_file: 
        csv_reader = csv.DictReader(csv_file) 
        for row in csv_reader: 
            Marks_In_Percentage.append(float(row["Coffee in ml"])) 
            Days_Present.append(float(row["sleep in hours"])) 
            
        return {"x" : Marks_In_Percentage, "y": Days_Present} 
        
        
def findCorrelation(datasource): 
    correlation = np.corrcoef(datasource["x"], datasource["y"]) 
    print("Correlation between Coffee in ml vs sleep in hours :- \n--->",correlation[0,1]) 

def setup(): 
    data_path = "./cups of coffee vs hours of sleep.csv" 
    datasource = getDataSource(data_path) 
    findCorrelation(datasource) 

setup()
