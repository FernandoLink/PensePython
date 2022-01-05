import pickle 
t = [1,2,3]
s = pickle.dumps(t)
t2 = pickle.loads(s)
print(s)
print(t2)
