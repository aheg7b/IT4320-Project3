#IT 4320 Project 3
#Aidan Engbert
#NAME
#NAME
#NAME

def Stock_Name_Check(name):
    return 0
    #return 1 for valid input
    #return 0 for invalid input

def Chart_Type(chart_type):
    return 0
    #takes input of a number
    #checks number for valid input
    #returns 1 for valid input
    #returns 0 for invalid input

def Time_Series(time_type):
    return 0
    #takes input of a number
    #checks number for valid input
    #returns 1 for valid input
    #returns 0 for invalid input

def Dates(START,END):
    return 0
    #checks for vallid input
    #suggest date swap for invalid input
    #returns 1 for valid input
    #returns 0 for invalid input

def Graph(input):
    return 0
    #takes all the data and makes a graph

def Open_Browser(input):
    return 0
    #opens the browser to view the chart

def main():
    print("**********Stock Data Chart Gen.**********")
    Stock_Name = input("Enter teh stock symbol: ")
    if not Stock_Name_Check(Stock_Name):
        print("Invalid stock symbol, please try again: ")
        return
    
    print("\nChart Type:")
    print("1. Line Chart")
    print("2. Bar Chart")
    chart_type=input("Chart Tipe? (1 or 2) ")
    if not Chart_Type(chart_type):
        print("Invalid input. Please try again ")
        return
    
    print("\nTime Series Options:")
    print("1. TIME_SERIES_DAILY")
    print("2. TIME_SERIES_WEEKLY")
    print("3. TIME_SERIES_MONTHLY")
    time_tipe=input("Time Tipe? (1,2,or3) ")
    if not Time_Series(time_tipe)
        print("Invalid input. Please try again ")
        return
