#!/usr/bin/env python3


def main():
  
    proto =["ssh","http","https"]    #creates list named proto
    protoa = ["ssh","http","https"]
    print (proto)                    #prints the list proto
    proto.append("dns")
    protoa.append("dns")
    print(proto)                     #prints the list proto 
    proto2 = [22,80,443,53]
    proto.extend(proto2)
    print (proto)
    protoa.append(proto2)
    print (protoa)

main()
