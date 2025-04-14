class Band:
    """Band class representing a musical band with musicians."""
    
    def __init__(self, name):
        """Initialize a Band with a name and empty collection of musicians."""
        self.name = name
        self.musicians = []
    
    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)
    
    def play(self):
        """Return a string showing each musician playing their instrument."""
        output = []
        for musician in self.musicians:
            output.append(musician.play())
        return '\n'.join(output)
    
    def __str__(self):
        """Return a string representation of the Band."""
        musician_strings = []
        for musician in self.musicians:
            musician_strings.append(str(musician))
        return f"{self.name} ({', '.join(musician_strings)})"
