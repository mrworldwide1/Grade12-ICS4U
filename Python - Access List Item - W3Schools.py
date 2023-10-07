# Explain in your own words how a programmer can access a range of index in a list.
# Create some examples after seeing the 3 examples given in the link  

# A programmer can access a range of index in a list by first typing the name of the list, followed by the range of index in square brackets. Don't forget to put everything in round brackets.
# if you wish to access a single index in a list, you just need the one index number.
# Example: myList[1] specifies second thing in the list
# myList[0:2] specifies first to third thing in the list

def listRange(list):
  return(list[1:3])

def listRange2(list):
  return(list[:2])

def listRange3(list):
  return(list[-4:-1])

def listRange4(list):
  return(list[3:])

# example 1 list
animes = ["spy x family", "evangelion", "konosuba", "eminence in shadow", "haikuu"]
print(listRange(animes))

# example 2 list
food = ["general tso's chicken", "rice", "noodles", "fried rice", "curry", "ice"]
print(listRange2(food))

# example 3 list
countries = ["canada", "taiwan", "ukraine", "madagascar", "greenland", "philipines"]
print(listRange3(countries))

# example 4 list
diseases = ["ebola", "malaria", "cancer", "aids", "hiv", "lupus"]
print(listRange4(diseases))
