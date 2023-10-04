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
