import random
import numpy as np
import matplotlib.pyplot as plt
import sys

# Q1 = input("Enter Q1: ")
# Q2 = input("Enter Q2: ")
# days = input("Number of days? ")

Q1 = sys.argv[1]
Q2 = sys.argv[2]
days = sys.argv[3]


Q1 = int(Q1)
Q2 = int(Q2)
days = int(days)

print("Starting Simulation...")

P1 = int(Q1/6) 
P2 = int(Q2/6) 

inventory = [[Q1,Q2]]
#day 0, base quantities

if days < 1:
    print("Days must be greater than 1")
    exit()

meanCustomerQ1 = 100
meanCustomerQ2 = 100 

waitTimeP1 = 0
waitTimeP2 = 0
for i in range(0,days):
    if waitTimeP1 == 0:
        #new order for more tendies
        Q1 = Q1 + P1
        #new wait time for orders
        waitTimeP1 = random.randint(1,4)
    else:
        waitTimeP1 = waitTimeP1 - 1
    if waitTimeP2 == 0:
        #new order for more tendies 
        Q2 = Q2 + P2
        #new wait time for orders
        waitTimeP2 += random.randint(1,4)
    else:
        waitTimeP2 = waitTimeP2 - 1
    
    customerPurchasesQ1 = np.random.normal(Q1/meanCustomerQ1,100,1000)
    customerPurchasesQ2 = np.random.normal(Q2/meanCustomerQ2,100,1000)

    customerPurchasesQ1 = [x for x in customerPurchasesQ1 if x > 0]
    customerPurchasesQ2 = [x for x in customerPurchasesQ2 if x > 0]

    itemsPurchasedQ1 = customerPurchasesQ1[random.randint(0,len(customerPurchasesQ1)-1)]
    itemsPurchasedQ2 = customerPurchasesQ1[random.randint(0,len(customerPurchasesQ1)-1)]

    Q1 = Q1 - int(np.floor(itemsPurchasedQ1))
    Q2 = Q2 - int(np.floor(itemsPurchasedQ2))

    if Q1 < 0:
        Q1 = 0
    if Q2 < 0:
        Q2 = 0
    #end of day, record quantities
    inventory.append([Q1,Q2])

Q1R = []
Q2R = []

for i in range(len(inventory)):
    Q1R.append(inventory[i][0])
    Q2R.append(inventory[i][1])

plt.title("Inventory by days")
plt.xlabel("Days")
plt.ylabel("Items in stock")
plt.plot(range(0,len(Q1R)),Q1R, label = "Q1",color="Blue",linewidth=1)
plt.plot(range(0,len(Q2R)),Q2R, label = "Q2",color="Red",linewidth=1)
plt.legend()
plt.show()