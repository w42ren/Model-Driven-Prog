
network={"S1": ["10.0.1.1"],
         "R1": ["10.0.2.1", "10.0.3.1", "10.0.4.1"],
         "R2": ["10.0.5.1", "10.0.6.1", "10.0.7.1"]
         }

#print (type(network))

print (network,"\n")

# To print the values of the keys alone , values alone, or key value pairs  
print (*network.keys(),"\n")
print (*network.values(),"\n")
print (*network.items(),"\n")
#To print a list of ip addresses iterate the ip address values for the keys referenced in the dictionary 'S1' etc
for x in network['S1']:print(x)
for x in network['R1']:print(x)
for x in network['R2']:print(x)
print ("\n")
#iterate the values in the dictionary and print them the *x unpacks the values in the lists which will remove the ['value']
for x in network.values():print(*x)
print ("\n")
#iterate the keys and values and print them the *x unpacks the values in the lists which will remove the ['value']
print ("\n")
for i,x in network.items():print(i,*x)





