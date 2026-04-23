class TrackedValue:
    def __init__(self, value, stats):
        self.value = value
        self.stats = stats  # Ein Dictionary für den Zähler

    def __lt__(self, other):
        self.stats['comparisons'] += 1
        return self.value < other.value

    def __gt__(self, other):
        self.stats['comparisons'] += 1
        return self.value > other.value
    
    def __le__(self, other):
        self.stats['comparisons'] += 1
        return self.value <= other.value
    
    def __ge__(self, other):
        self.stats['comparisons'] += 1
        return self.value >= other.value
    
    def __eq__(self, other):
        self.stats['comparisons'] += 1
        return self.value == other.value   
     
    def __ne__(self, other):
        self.stats['comparisons'] += 1
        return self.value != other.value
       
    def __repr__(self):
        return repr(self.value) 