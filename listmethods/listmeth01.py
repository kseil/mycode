#!/usr/bin/env python3

#create first lists
proto=["ssh", "http", "https"]
protoa=['ssh', 'http', 'https']
print(proto)
#add dns to both lists
proto.append('dns')
protoa.append('dns')
print(proto)

#list of common ports)
proto2 = [22, 80, 443, 53]
#extend and print proto
proto.extend(proto2)
print(proto)

#append and print protoa
protoa.append(proto2)
print(protoa)


#list insert attempt

proto.insert(3, proto[6])
print(proto)

