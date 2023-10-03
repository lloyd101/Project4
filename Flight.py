from Airport import *

class Flight:

    def __init__(self,flightNo,origin,destination):
        if isinstance(origin, Airport) and isinstance(destination, Airport):
            self._flightNo = flightNo
            self._origin = origin
            self._destination = destination
        else:
            raise TypeError ("the origin and destination must be airport objects")

    def isDomesticFlight(self):
        x = self._origin
        y = self._destination
        if x.getCountry() == y.getCountry():
            return True
        else:
            return False

    def __repr__(self):
        if self.isDomesticFlight() == True:
            return f'{"Flight: " + str(self._flightNo) + " from " + str(self._origin.getCity()) + " to " + str(self._destination.getCity()) + " {domestic}"}'
        if self.isDomesticFlight() == False:
            return f'{"Flight: " + str(self._flightNo) + " from " + str(self._origin.getCity()) + " to " + str(self._destination.getCity()) + " {international}"}'


    def __eq__(self,other):
        if isinstance(other,Flight):
            return self._origin == other._origin and self._destination == other._destination
        else:
            return False

    def getFlightNumber(self):
        return self._flightNo

    def getOrigin(self):
        return self._origin

    def getDestination(self):
        return self._destination

    def setOrigin(self,origin):
        self._setOrigin = origin

    def setDestination(self,destination):
        self._setDestination = destination
