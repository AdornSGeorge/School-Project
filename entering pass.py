import pickle
f = open("password.dat","wb")
e = input("enter passw: ")
l=[]
l.append(e)
pickle.dump(l,f)
