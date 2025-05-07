try:
    file=open("a.txt","r")
    di={"key":"val"}
    print(di["key"])
    
except FileNotFoundError:
    file=open("a.txt","w")

except KeyError as error:
    print(f"the key {error} not there")

else:
    print("all success")

finally:
    file.close()
    print("no matter what file closed")