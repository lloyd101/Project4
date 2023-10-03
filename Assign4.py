# Import Airport and Flight classes
from Flight import *
from Airport import *

# opens airportFile and flightFile
airportFile = ("/Users/lloydngaindjo/Downloads/airports.txt")
flightFile = ("/Users/lloydngaindjo/PycharmProjects/Assignment4/flights.txt")
# Create containers to store Airport and Flight objects
allAirports = set()
allFlights = {}

def loadData(airportFile, flightFile):
  try:   # Try to open the airportFile and read its lines
    airportFile = open(airportFile)
    lines = airportFile.readlines()
    for line in lines:     # Iterate over the lines in the file
        # Remove whitespace, newline characters, and tabs from the line
        line = line.strip("\n").strip(" ").strip("\t").split(",")
        code = line[0].rstrip("\t").lstrip("\t").rstrip(" ").lstrip(" ").strip("\n")
        country=line[1].rstrip("\t").lstrip("\t").rstrip(" ").lstrip(" ").strip("\n")
        city = line[2].rstrip("\t").lstrip("\t").rstrip(" ").lstrip(" ").strip("\n")
        airport = Airport(code, city, country)
        allAirports.add(airport)


    flightFile = open(flightFile)   # Try to open the flightFile and read its lines
    lines = flightFile.readlines()
    for line in lines:
        splitFile = line.split(',')         # Split the line by commas
        # Initialize the origin and destination airport objects to None
        orig = None
        dest =  None
        for x in allAirports: # If the code of the current Airport matches the origin or destination code from the line,
        # set the corresponding variable to the Airport object
            if x.getCode() == splitFile[1].strip():
                orig = x
            if x.getCode() == splitFile[2].strip():
                dest = x

        # Use the data from the line to create a Flight object
        flight = Flight(splitFile[0].strip(), origin=orig, destination=dest)
        # Add the Flight object to the allFlights dictionary, using the origin airport code as the key
        if orig.getCode() not in allFlights:
            allFlights[orig.getCode()] = [flight]
        else:
            allFlights[orig.getCode()].append(flight)
  except:
      return False   # If there is an error, return False
  return True   # If the function completes successfully, return True


# getAirportByCode is a function that takes in an airport code, and returns the Airport object with that code, if it
# exists.If the airport code is not found, the function returns -1.
def getAirportByCode(code):
  for airport in allAirports:   # Iterate over the Airport objects in allAirports
       #If the code of the current Airport matches the input code, return airport
    if airport.getCode() == code:
      return airport

  return -1


# findAllCityFlights is a function that takes in a city name,
def findAllCityFlights(city):
  cityFlights = []   # Initialize an empty list to store the matching flights
  for key in allFlights:
      for flight in allFlights[key]:
          # If the origin city or destination city of the current flight matches the input city, append the flight to
          # the cityFlights list
          if flight.getOrigin().getCity() == city or flight.getDestination().getCity()==city:
              cityFlights.append(flight)
  return cityFlights


def findAllCountryFlights(country): # findAllCountryFlights is a function that takes in a country name
  countryFlights = []
  for key in allFlights:
      for flight in allFlights[key]:
          # If the origin country or destination country of the current flight matches the input country, append the
          # flight to the countryFlights list
          if flight.getOrigin().getCountry() == country or flight.getDestination().getCountry()==country:
              countryFlights.append(flight)
  return countryFlights


# findFlightBetween is a function that takes in two Airport objects, origAirport and destAirport, and returns a string
# indicating whether there is a direct flight between these airports.
def findFlightBetween(origAirport, destAirport):
  for key in  allFlights:
      for flight in allFlights[key]:
          # If the origin and destination of the current flight match the input airports, return a string indicating
          # that there is a direct flight between these airports
          if flight.getOrigin()== origAirport and flight.getDestination()==destAirport:
            return "Direct Flight: " + origAirport.getCode() + " to " + destAirport.getCode()
  else:
    connectingAirports = set()   # Initialize an empty set to store the codes of connecting airports
    for flight in allFlights[origAirport.getCode()]:
      for flight2 in allFlights[flight.getDestination().getCode()]:
        # If the destination of the current flight is the destAirport,add the destination code of the current flight to
      # the connectingAirports set
        if flight2.getDestination() == destAirport:
          connectingAirports.add(flight.getDestination().getCode())

    if len(connectingAirports) > 0:
      return connectingAirports
    else:
      return -1


# findReturnFlight is a function that takes in a Flight object and returns the Flight object with the same destination
# as the input Flight's origin
def findReturnFlight(firstFlight):
  for flight in allFlights[firstFlight.getDestination().getCode()]:
      # If the destination of the current flight is the same as the origin of the input Flight, return the current
      # Flight object
    if flight.getDestination() == firstFlight.getOrigin():
      return flight

  return -1





