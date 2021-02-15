#Create a dictionary called network
#The network should contain a switch called S1 and 2 routers called R1 and R2
#store the IP addresses in the dictionary store the IP addresses as strings
#Print a list of all the IP addresses
#S1 10.0.1.1
#R1 10.0.2.1 10.0.3.1 10.0.4.1
#R2 10.0.5.1 10.0.6.1 10.0.7.1


network={"S1": "10.0.1.1",
         "R1": ["10.0.2.1", "10.0.3.1", "10.0.4.1"],
         "R2": ["10.0.5.1", "10.0.6.1", "10.0.7.1"]
         }
print (type(network))
print (network ['S1'],network['R1'],
       network['R2'][0],network['R2'][1],network['R2'][2])
print (network ['S1'],network['R1'][0],network['R1'][1],network['R1'][2],
       network['R2'][0],network['R2'][1],network['R2'][2])
