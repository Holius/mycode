#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
successHTTP = 0
# open the file for reading
with open("/home/student/mycode/attemptLogin/keystone.common.wsgi") as kfile:
    
    # loop over the file
    for line in kfile:
        #must be uppercase GET/POST because the uppercase is the actuall sucess attempts
        if "GET" in line or "POST" in line: successHTTP += 1
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line: 
            loginfail += 1
            get_ip = line.split(" ")
            print(f"Naughty IP address is {get_ip[-1]}")
print("The number of failed log in attempts is", loginfail)
print("The number of GET/POST successful attempts is", successHTTP)
