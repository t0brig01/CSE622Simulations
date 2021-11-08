arvNums = [12,31,63,95,99,154,198,221,304,346,411,455,537]
servNums = [40,32,55,48,18,50,47,18,28,54,40,72,12]
class Customer:
    leftTime = 0
    def __init__(self, id, arrival,service):
        self.id = id
        self.arrival = arrival
        self.service = service

customers = []

for i in range(0,len(arvNums)):
    customers.append(Customer(int(i+1),arvNums[i],servNums[i]))
for x in customers:
    print("id:{0} \t arrival:{1} \t service:{2}".format(x.id,x.arrival,x.service))
left = []
servicingClient = None
queue = []
print(len(customers))
time = 0
servicingOrQueue = True
serverUses = 0
while servicingOrQueue == True:
    for x in customers:
        if x.arrival == time:
            if servicingClient == None:
                print("Customer {0} servicing".format(x.id))
                servicingClient = x
            else:
                print("Customer {0} added to queue".format(x.id))
                queue.append(x)
            customers.remove(x)
    if servicingClient != None:
        servicingClient.service = servicingClient.service - 1
        if servicingClient.service == 0:
            servicingClient.leftTime=time
            left.append(servicingClient)
            if(len(queue) > 0):
                servicingClient = queue.pop(0)
                print("Customer {0} servicing".format(servicingClient.id))
            else:
                servicingClient = None
    if(len(customers) == 0):
        if(len(queue) == 0):
            if(servicingClient == None):
                servicingOrQueue = False
    # print("Time: {0}\t customerLeft:{1}\t queueLength:{2}\t servicing:{3}".format(time,len(customers),len(queue),bool(servicingClient)))
    if servicingClient:
        serverUses = serverUses + 1
    time = time + 1

print("Done. Time elapsed: {0}".format(time))

for x in left:
    print("Customer {0} left at {1}".format(x.id,x.leftTime))
print("Server usage: %.3f%%" % ((serverUses/time)*100))