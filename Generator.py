from random import seed


class Generator:

    def __init__(self,a,c,m,seed):
        self.a = a
        self.c = c
        self.m = m
        self.previous = seed

    def next_random(self):
        """Generates the next normalized pseudo-random number between 0 and 1."""
        self.previous = ((self.a * self.previous ) + self.c) % self.m
        return self.previous / self.m

        