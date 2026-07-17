#single error
'''try:
    if n>0:
        print("+ve")
    else:
        print("-ve or 0")
except NameError:
    print("Define the n")
else:
    print("No errors occured")
finally:
    print("End of the program")'''

'''try:
    n=10
    if n>0:
        print("+ve")
    else:
        print("-ve or 0")
except NameError:
    print("Define the n")
else:
    print("No errors occured")
finally:
    print("End of the program")'''
#multiple errors
'''try:
    print(n)
    print(" "+12)
    print(int(input("Enter a number:")))
    d={1:2,2:3,3:4}
    print(d[9])
    l=[23,67,98]
    print(l[12])
    print(1/0)
          
except NameError:
    print("Define the n")
except TypeError:
    print("Give same datatypes")
except ValueError:
    print("Give the proper datatype")
except KeyError:
    print("Key is not present")
except IndexError:
    print("Index is not present")
except ZeroDivisionError:
    print("cant be divisible with zero")
else:
    print("No errors occured")
finally:
    print("End of the program")'''

'''try:
    n=10
    print(n)
    print(11+12)
    print(int(input("Enter a number:")))
    d={1:2,2:3,3:4}
    print(d[2])
    l=[23,67,98]
    print(l[1])
    print(1/9)
          
except NameError:
    print("Define the n")
except TypeError:
    print("Give same datatypes")
except ValueError:
    print("Give the proper datatype")
except KeyError:
    print("Key is not present")
except IndexError:
    print("Index is not present")
except ZeroDivisionError:
    print("cant be divisible with zero")
else:
    print("No errors occured")
finally:
    print("End of the program")'''

#exceptional handling using "except alias as e" for multiple errors
'''try:
    n=10
    print(n)
    print(11+12)
    print(int(input("Enter a number:")))
    d={1:2,2:3,3:4}
    print(d[2])
    l=[23,67,98]
    print(l[12])
    print(1/9)
          
except (NameError,TypeError,ValueError,KeyError,IndexError,ZeroDivisionError)as e:
    print("Error occured",e)
else:
    print("No errors occured")
finally:
    print("End of the program")'''

#instead of multiple list of exception we can use "Exception " to handle all errors

'''try:
    n=10
    print(n)
    print(11+12)
    print(int(input("Enter a number:")))
    d={1:2,2:3,3:4}
    print(d[2])
    l=[23,67,98]
    print(l[12])
    print(1/9)
          
except Exception as e:
    print("Error occured:",e)
else:
    print("No errors occured")
finally:
    print("End of the program")'''

#The raise keyword is used to manually generate (throw) an exception

'''try:
    n=-10
    if n<0:
        raise Exception("Amount needs to be >0")
          
except Exception as e:
    print("Error occured:",e)
else:
    print("No errors occured")
finally:
    print("End of the program")'''






















































