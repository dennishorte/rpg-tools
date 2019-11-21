"""
The Big Five peronsality traits are a widely accepted taxonomy of personality. See this article at
wikipedia for more details. https://en.wikipedia.org/wiki/Big_Five_personality_traits
"""

import numpy as np


class Personality(object):
    def __init__(self):
        self.openness = 0
        self.neuroticism = 0
        self.extraversion = 0
        self.agreeableness = 0
        self.conscientiousness = 0

    def __str__(self):
        return 'Personality(o{:1.1f} c{:1.1f} e{:1.1f} a{:1.1f} n{:1.1f})'.format(
            self.openness,
            self.conscientiousness,
            self.extraversion,
            self.agreeableness,
            self.neuroticism,
        )


class RandomPersonality(Personality):
    def __init__(self):
        self.openness = np.random.normal(0, 1)
        self.neuroticism = np.random.normal(0, 1)
        self.extraversion = np.random.normal(0, 1)
        self.agreeableness = np.random.normal(0, 1)
        self.conscientiousness = np.random.normal(0, 1)


class ExtremeRandomPersonality(RandomPersonality):
    def __init__(self):
        self.openness = np.random.normal(0, 3)
        self.neuroticism = np.random.normal(0, 3)
        self.extraversion = np.random.normal(0, 3)
        self.agreeableness = np.random.normal(0, 3)
        self.conscientiousness = np.random.normal(0, 3)
    
                

if __name__ == "__main__":
    print(ExtremeRandomPersonality())
