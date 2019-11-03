#%%
def prime(n):
    primelist = []
    for i in range(2,n):
        for j in range(2,i):
            if i % j == 0:
                 break
             
        else:
            primelist.append(i)
    return primelist
            


#%%
print(prime(1000))

#%%
