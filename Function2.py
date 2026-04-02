def op(a,b):
    return (a+b),(a*b),(a-b)


# add_val,mul_val,sub_val=op(2,3)

# print(add_val)
# print(mul_val)
# print(sub_val)

# def add(*args):
#     print( sum(args))

# add(1,2,3)
# add(1,2,3,5,6,2,5)
# add(1,2,3.34)
# add(1,2)


# 

x = 10 # global

def tets():
    x = 1000 # local
    print(x)

print(x)
tets()
