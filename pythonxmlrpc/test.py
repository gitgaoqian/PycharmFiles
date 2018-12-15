from SimpleXMLRPCServer import SimpleXMLRPCServer
s=SimpleXMLRPCServer(("127.0.0.1",4444))
def twice(x):
    return x*x
s.register_function(twice)
s.serve_forever()

