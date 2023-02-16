"""
    Author: Michael Fessler
    Date: 2023/02/16
    Version: 0.1
    Description:
            App to calculate the break even point of a photovoltaic array, this time in python.
"""

decimalFormat2 = "{:.2f}"
decimalFormat3 = "{:.3f}"

peakPower = 0.375
moduleCost = 259.99
achievedPower = 0.375

numModules = int(input("Number of solar modules: "))
while numModules < 1 or numModules > 80:
    print("Invalid input! The number of solar modules must be an integer greater than or equal to 1 and less than or equal to 80.")
    numModules = int(input("Number of solar modules: "))

subsidy = int(input("Subsidy in % of the investment: "))
while subsidy < 0 or subsidy > 100:
    print("Invalid input! The subsidy must be an integer greater than or equal to 0 and less than or equal to 100.")
    subsidy = int(input("Subsidy in % of the investment: "))

