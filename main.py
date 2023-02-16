"""
    Author: Michael Fessler
    Date: 2023/02/16
    Version: 0.1
    Description:
            App to calculate the break even point of a photovoltaic array, this time in python.
"""

#Variabels and Lists for relevant data
decimalFormat2 = "{:.2f}"
directions = ["SOUTH", "SOUTH-EAST", "EAST", "SOUTH-WEST", "WEST"]
directionalModifier = [1.00, 0.95, 0.90, 0.95, 0.90]

peakPower = 0.375
moduleCost = 259.99
achievedPower = 0.375
numModules = -1
subsidy = -1
bearing = -1
rate = -1

y_Spec = 905

#Input verification loops to get assignment data
try:
    numModules = int(input("Number of solar modules: "))
except ValueError:
    numModules = -1
while numModules < 1 or numModules > 80:
    print("Invalid input! "
          "The number of solar modules must be an integer greater than or equal to 1 and less than or equal to 80. ")
    try:
        numModules = int(input("Number of solar modules: "))
    except ValueError:
        numModules = -1

try:
    subsidy = int(input("Subsidy in % of the investment: "))
except ValueError:
    subsidy = -1
while subsidy < 0 or subsidy > 100:
    print("Invalid input! "
          "The subsidy must be an integer greater than or equal to 0 and less than or equal to 100. ")
    try:
        subsidy = int(input("Subsidy in % of the investment: "))
    except ValueError:
        subsidy = -1

try:
    bearing = int(input("Direction of the photovoltaic system: \n"
                        "1: SOUTH \n"
                        "2: SOUTH-EAST \n"
                        "3: EAST \n"
                        "4: SOUTH-WEST \n"
                        "5: WEST \n"
                        "Please enter the direction: "))
except ValueError:
    bearing = -1
while bearing < 1 or bearing > 5:
    print("Invalid input! "
          "The direction input must be an integer greater than or equal 1 and less than or equal 5. ")
    try:
        bearing = int(input("Direction of the photovoltaic system: \n"
                            "1: SOUTH \n"
                            "2: SOUTH-EAST \n"
                            "3: EAST \n"
                            "4: SOUTH-WEST \n"
                            "5: WEST \n"
                            "Please enter the direction: "))
    except ValueError:
        bearing = -1



try:
    rate = int(input("Electricity rate in cents/kWh: "))
except ValueError:
    rate = -1
while rate < 1 or rate > 100:
    print("Invalid input! "
          "The electricity rate must be an integer which is at least 1 and must not exceed 100 cents/kWh. ")
    try:
        rate = int(input("Electricity rate in cents/kWh: "))
    except ValueError:
        rate = -1

if numModules > 1:
    print(str(numModules) + " modules facing " + directions[bearing - 1])
else:
    print("One module facing " + directions[bearing - 1])

print("Achievable total power: " + str(peakPower * numModules) + "kWp. ")

achievedPower = peakPower * numModules * directionalModifier[bearing - 1]

if bearing != 1:
    print("However, due to the suboptimal direction, only " + str(achievedPower) + "kWp are achieved. ")

#calculations for yearly power output, investment in € for the panels,
#yearly earnings, yearly amount of government subsidy in €
Y = y_Spec * achievedPower
investment = numModules * moduleCost
earnings = Y * rate
remCosts = investment
yearlySubsidy = (investment / 100) * subsidy
years = 0

print("Investment of €" + str(decimalFormat2.format(investment)) + " leads to earnings of €" +
      str(decimalFormat2.format(earnings / 100)) + " each year. ")

#loop to perform yearly calculations
while remCosts > 0:
    years += 1
    if subsidy > 0:
        remCosts = remCosts - (earnings / 100) - yearlySubsidy
        if remCosts < 0:
            if years <= 1:
                print("PV system amortized within a year. ")
            else:
                print("PV system amortized within " + str(years) + " years. ")
            break
        print("After year " + str(years) + ": €" + str(decimalFormat2.format(remCosts)) + " still to compensate (€" +
              str(decimalFormat2.format(yearlySubsidy)) + " paid by the government). ")
    else:
        remCosts = remCosts - (earnings / 100)
        if remCosts < 0:
            if years <= 1:
                print("PV system amortized within a year. ")
            else:
                print("PV system amortized within " + str(years) + " years. ")
            break
        print("After year " + str(years) + ": €" + str(decimalFormat2.format(remCosts)) + " still to compensate. ")