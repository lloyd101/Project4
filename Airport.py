class Airport:
    def __init__(self, code, city, country):
        self._code = code
        self._city = city
        self._country = country
    def __repr__(self):
        return self._code + " (" + self._city + ", " + self._country + ")"
    def getCode(self): # Getter that returns airport code
        return self._code
    def getCity(self): # Getter that returns airport city
        return self._city
    def getCountry(self): # Getter that returns airport country
        return self._country
    def setCity(self, city): # Setter that sets the Airport city
        self._city = city
    def setCountry(self, country): # Setter that sets the Airport country
        self._country = country


