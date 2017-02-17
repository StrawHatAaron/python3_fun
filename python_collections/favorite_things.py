favorite_things=["warm mittens", "whiskers on kittens", "my girlfriend", "in and out"]
print(favorite_things)
favorite_things+=["add it on to the vector/list", "we added another list right here"]
print(favorite_things)
favorite_things.append("how to append something to the end of a list")
print(favorite_things)
#delete the last cell/index
del favorite_things[-1]
a=[1,2,3]
print(a)
a.extend("abc")
print(a)
del a[1]
print("took out the 1 index (they start at an idex of 0) ", a)