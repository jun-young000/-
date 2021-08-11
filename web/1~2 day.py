"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""
def is_on_list(week,day):
    if day in week:
        return True
    else:
        return False
        
def get_x(week,day):
    return week[day]

def add_x(week,day):
    return week.append(day)

def remove_x(week,day):
    week.remove(day)
# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)


# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #
### 샘코드
def is_on_list(a_list=[], word=""):
  return word in a_list

def get_x(a_list=[], index=0):
  return a_list[index]

def add_x(a_list=[], word=""):
  a_list.append(word)

def remove_x(a_list=[], word=""):
  a_list.remove(word)