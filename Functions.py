"""def sum(argmentA,argmentB):
    if argmentA==argmentB:
        print("condition is True")
    elif argmentA>argmentB:
        print("yes")
    elif argmentA<argmentB:
        print(argmentA,"is less than ",argmentB)
    else:
        print("condition is false")
    return

values=sum(10,20)"""

"""def tinku(argmenta,argmentb):
    if argmenta*argmentb==10:
        print("Value added")
    else:
        print("value not added")
    return
values=tinku(5,3)"""

def info(arg1,*vart):

    for maru in vart:
        print(maru)
        return

info("rosy","jack","puli","mater")

