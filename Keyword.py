def bank_account(argement1):
    pass
bank_account('SavingsAccount')
#The pass statement in python is used when a statement is required syntactically but you do not want any command or code to execure.
#The pass statement is a null operation: nothing happens when it executes.

def sum(arg1, arg2):
    total = arg1+arg2
    print("inside the function local total: ",total)
    return total
sum(10,20)
print("calling global variable: ",total)