#define a function to read the data from the file as a list of dictionaries
def fileToList(fileName, headers=None):
  file = open(fileName) # openning and storing the file
  readingHeader = file.readline().split() # reading and storing the headers
  return [dict(zip(readingHeader, r.split())) for r in file.readlines()] # reading the file and getting the data as list of dictionaries

#define a function to read the smallest spread of the list when applying the function "fntn" to the file
def smallestSpread(listOfDisc, fntn, dayNum=None):
  return (
    dayNum if listOfDisc == [] # check to see if file reached the end
    else (
      smallestSpread(listOfDisc[1:], fntn, listOfDisc[0]) if fntn(listOfDisc[0]) is not None and (
        dayNum is None or fntn(listOfDisc[0]) < fntn(dayNum)) else (
          smallestSpread(listOfDisc[1:], fntn, dayNum))
          ) # reads the data and returns the day number with the smallest spread after sorting
        )

#define function to read the file and apply the previous functions and the lambda function
def dailyWeatherData():
  listOfDisc = fileToList("w_data (5).dat") # reads and converts the file as list of dictionaries
  dayNum = smallestSpread(
    listOfDisc, lambda item: abs( # using a lambda function to get the temperature spread
    float(item['MxT'].replace('*','')) - float(item['MnT'].replace('*','')) # removing the '*' char which was causing an error
    ) if 'Dy' in item else None) # ignoring the invalid rows
  return(dayNum['Dy']) # returns the day number with the smallest spread

print( 'The day number with the smallest temperature spread is: \n' + dailyWeatherData())
