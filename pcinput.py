

def getFloat( prompt ):
  while True:
      try:
          num = float( input( prompt ) )
      except ValueError:
          print( "That is not a number -- please try again" )
          continue
      return num

def getInteger( prompt ):
  while True:
      try:
          num = int( input( prompt ) )
      except ValueError:
          print( "That is not an integer -- please try again" )
          continue
        # solution to keep asking for new num if inputted num is not between 0 and 1000
      if (num < 0) or (num>1000):
          print("The number should be between 0 and 1000")
          continue
      return num

def getString( prompt ):
  line = input( prompt )
  return line.strip()

def getLetter( prompt ):
  while True:
      line = input( prompt )
      line = line.strip()
      line = line.upper()
      if len( line ) != 1:
          print( "Please enter exactly one character" )
          continue
      if line < 'A' or line > 'Z':
          print( "Please enter a letter from the alphabet" )
          continue
      return line