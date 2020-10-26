#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
proto.append("dns")
proto.append("smtp")
proto2 = [ 22, 80, 443, 53 ]
proto.append(proto2)
proto.extend(proto2)
#extend passes the values into list; the append passes the reference of the list
proto2[0] = 1
print(proto)
