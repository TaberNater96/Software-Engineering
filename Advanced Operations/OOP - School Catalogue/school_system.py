# Define the parent class School
class School:
    
    # Constructor with three parameters: name, level, and numberOfStudents
    def __init__(self, name, level, numberOfStudents):
        self._name = name  # directly set the underlying attribute
        self._level = level  # directly set the underlying attribute
        self._numberOfStudents = numberOfStudents

    # Getter for the name property
    @property
    def name(self):
        return self._name

    # Getter for the level property
    @property
    def level(self):
        return self._level

    # Getter for the numberOfStudents property
    @property
    def numberOfStudents(self):
        return self._numberOfStudents

    # Setter for the numberOfStudents property
    @numberOfStudents.setter
    def numberOfStudents(self, value):
        self._numberOfStudents = value

    # Representation method to display information about the school
    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.numberOfStudents} students"

# Define the PrimarySchool class that inherits from School
class PrimarySchool(School):
    
    # Constructor with custom pickupPolicy property
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "primary", numberOfStudents)  # call to the superclass constructor
        self._pickupPolicy = pickupPolicy  # set the underlying attribute directly

    # Getter for the pickupPolicy property
    @property
    def pickupPolicy(self):
        return self._pickupPolicy

    # Override the __repr__ method to include pickupPolicy information
    def __repr__(self):
        parent_repr = super().__repr__()
        return f"{parent_repr}. Pickup policy: {self.pickupPolicy}"


# Define the HighSchool class that inherits from School
class HighSchool(School):
    
    # Constructor with an additional sportsTeams property
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, "high", numberOfStudents)  # call to the superclass constructor
        self._sportsTeams = sportsTeams

    # Getter for the sportsTeams property
    @property
    def sportsTeams(self):
        return self._sportsTeams

    # Override the __repr__ method to include sportsTeams information
    def __repr__(self):
        return f"{super().__repr__()}. Sports teams: {', '.join(self.sportsTeams)}"