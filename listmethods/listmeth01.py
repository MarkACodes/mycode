#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") #this will add "dns" to end of our list
protoa.append("dns") # this will also add "dns" to the end of this specific list
print(proto)
proto2  = [22, 81, 443, 54, 80, 53 ] # port numbers
proto.extend(proto2) # pass proto2 as argument to extend the method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

