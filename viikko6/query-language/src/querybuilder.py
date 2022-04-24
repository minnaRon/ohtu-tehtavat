from matchers import *

class QueryBuilder:
    def __init__(self, matcher=None):
        self.matcher = matcher or All()
    
    def build(self):
        return self.matcher

    def playsIn(self, team):
        return QueryBuilder(And(self.matcher, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.matcher, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.matcher, HasFewerThan(value, attr)))

    def oneOf(self, matcher1, matcher2):
        return QueryBuilder(Or(And(self.matcher, matcher1), And(self.matcher, matcher2)))
