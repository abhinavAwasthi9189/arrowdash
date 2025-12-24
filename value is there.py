import pickle
#file=open("game_values.bin",'wb')
#x={"abh":0,"abhi":1,"abhin":2,"abhna":3,"abinav":4}
#pickle.dump(x,file)
#file.close()

file=open("game_values.bin",'rb')
h=pickle.load(file)
for i in h:
    print(i,h[i])

