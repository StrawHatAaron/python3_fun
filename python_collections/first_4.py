#my_list=[1,2,3,4,5,6]
#for n in range(0,4): 
#my_iter=iter(my_list)
#clone = []	
#clone.append(next(my_iter))
#clone.append(next(my_iter)) 
#clone.append(next(my_iter))
#clone.append(next(my_iter))
#print(clone)

#num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
#clone=num[:4]+num[-4:len(num):1]
#print(clone)

def first_4(num):
    return num[:4]

def first_and_last_4(num):
    clone=num[:4]+num[-4:len(num):1]
    return clone

def odds(num):
	clone=num[1::2]
	return clone

num=[0,1,2,3,4,5,6]
#start even
#clone=num[0::2]
#start odd
clone=num[1::2]

#::-1 reverse the list
print(clone[::-1])