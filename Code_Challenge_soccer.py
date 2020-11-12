#define a function to read the data from the file as a list of dictionaries
def fileToList(fileName, headers=None):
  file = open(fileName) # open the file
  readingHeader = file.readline().split() # get headers from file as list
  headers = readingHeader if headers is None else headers # get headers ignoring the blanks on the headers
  return[dict(zip(headers, r.split())) for r in file.readlines()] # get data as list of dicts width headers as keys

#define a function to read the smallest difference of the list when applying the function "fntn"
def smallestDifference(listOfDisc, fntn, teamNm=None):
  return (
    teamNm if listOfDisc == [] # check to see if file reached the end
    else (
      smallestDifference(listOfDisc[1:], fntn, listOfDisc[0]) if fntn(listOfDisc[0]) is not None and (
        teamNm is None or fntn(listOfDisc[0]) < fntn(teamNm)) else (
          smallestDifference(listOfDisc[1:], fntn, teamNm))
          ) # reads the data and returns the day number with the smallest spread after sorting
        )

#define function to read the file and apply the previous functions and the lambda function
def englishPremierLeagueData():
  listOfDisc = fileToList("soccer.dat", headers=["Nr","Team","P","W","L","D","F","-","A","Pts"]) # reads and converts the file as list of dictionaries., passing extra headers to fill the blank ones
  teamNm = smallestDifference(
    listOfDisc, lambda item: abs( # lambda function to get the difference in ‘for’ and ‘against’ goals
    int(item['F']) - int(item['A']))
    if 'Team' in item else None) # ignoring the invalid rows
  return(teamNm['Team']) # returns the name of the team with the smallest difference

print( 'The name of the team with the smallest difference in "for" and "against" goals is: \n' + englishPremierLeagueData() )
