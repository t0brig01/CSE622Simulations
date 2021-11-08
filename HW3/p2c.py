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
servicingClient1 = None
servicingClient2 = None
queue = []

time = 0
servicingOrQueue = True
server1Uses = 0
server2Uses = 0
while servicingOrQueue == True:
    for x in customers:
        if x.arrival == time:
            if servicingClient1 == None:
                print("Customer {0} servicing by server 1".format(x.id))
                servicingClient1 = x
                customers.remove(x)
            elif servicingClient2 == None:
                print("Customer {0} servicing by server 2".format(x.id))
                servicingClient2 = x
                customers.remove(x)
            else:
                print("Customer {0} added to queue".format(x.id))
                queue.append(x)
                customers.remove(x)
            
    if servicingClient1 != None:
        servicingClient1.service = servicingClient1.service - 1
        if servicingClient1.service == 0:
            servicingClient1.leftTime=time
            left.append(servicingClient1)
            if(len(queue) > 0):
                servicingClient1 = queue.pop(0)
            else:
                servicingClient1 = None
    if servicingClient2 != None:
        servicingClient2.service = servicingClient2.service - 1
        if servicingClient2.service == 0:
            servicingClient2.leftTime=time
            left.append(servicingClient2)
            if(len(queue) > 0):
                servicingClient2 = queue.pop(0)
            else:
                servicingClient2 = None
    if(len(customers) == 0):
        if(len(queue) == 0):
            if(servicingClient1 == None and servicingClient2 == None):
                servicingOrQueue = False
    # print("Time: {0}\t customerLeft:{1}\t queueLength:{2}\t servicing:{3}".format(time,len(customers),len(queue),bool(servicingClient1)))
    if servicingClient1:
        server1Uses = server1Uses + 1
    if servicingClient2:
        server2Uses = server2Uses + 1
    time = time + 1

print("Done. Time elapsed: {0}".format(time))

for x in left:
    print("Customer {0} left at {1}".format(x.id,x.leftTime))
print("Server 1 usage: %.3f%%" % ((server1Uses/time)*100))
print("Server 2 usage: %.3f%%" % ((server2Uses/time)*100))