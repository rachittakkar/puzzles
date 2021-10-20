#Roi_calculator

Investment = 500000
Rent = 900
Additional_cost = 1000

def ROI(Investment, Rent, Loss):
    Profit = (Rent * 12) - Loss
    ROI = (Profit/Investment) * 100
    print(ROI)

ROI(Investment, Rent, Additional_cost)    