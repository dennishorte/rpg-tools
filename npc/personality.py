"""
The Big Five peronsality traits are a widely accepted taxonomy of personality. See this article at
wikipedia for more details. https://en.wikipedia.org/wiki/Big_Five_personality_traits
"""

import numpy as np

class PersonalityTrait(object):
    def __init__(self, name, inverse, description, note, aspects):
        self.name = name
        self.inverse = inverse
        self.description = description
        self.note = note
        self.aspects = aspects


_TRAITS = [
    PersonalityTrait(
        name='openness',
        inverse='closedness',
        description="""Openness is a general appreciation for art, emotion, adventure, unusual ideas, imagination, curiosity, and variety of experience. People who are open to experience are intellectually curious, open to emotion, sensitive to beauty and willing to try new things. They tend to be, when compared to closed people, more creative and more aware of their feelings. They are also more likely to hold unconventional beliefs. High openness can be perceived as unpredictability or lack of focus, and more likely to engage in risky behaviour or drug taking. Moreover, individuals with high openness are said to pursue self-actualization specifically by seeking out intense, euphoric experiences. Conversely, those with low openness seek to gain fulfillment through perseverance and are characterized as pragmatic and data-driven—sometimes even perceived to be dogmatic and closed-minded. Some disagreement remains about how to interpret and contextualize the openness factor.""",
        samples=[
            'I have excellent ideas.',
            'I am quick to understand things.',
            'I use difficult words.',
            'I am full of ideas.',
            'I am not interested in abstractions. (reversed)',
            'I do not have a good imagination. (reversed)',
            'I have difficulty understanding abstract ideas. (reversed)',
        ],
        note='inventive/curious vs. consistent/cautious',
        aspects=['openness', 'intellect'],
    ),
    PersonalityTrait(
        name='neuroticism',
        inverse='emotional stability',
        description="""Neuroticism is the tendency to experience negative emotions, such as anger, anxiety, or depression. It is sometimes called emotional instability, or is reversed and referred to as emotional stability. Neuroticism is interlinked with low tolerance for stress or aversive stimuli. Those who score high in neuroticism are emotionally reactive and vulnerable to stress, also tending to be flippant in the way they express emotion. They are more likely to interpret ordinary situations as threatening, and minor frustrations as hopelessly difficult. Their negative emotional reactions tend to persist for unusually long periods of time, which means they are often in a bad mood. For instance, neuroticism is connected to a pessimistic approach toward work, confidence that work impedes personal relationships, and apparent anxiety linked with work. These problems in emotional regulation can diminish the ability of a person scoring high on neuroticism to think clearly, make decisions, and cope effectively with stress.

At the other end of the scale, individuals who score low in neuroticism are less easily upset and are less emotionally reactive. They tend to be calm, emotionally stable, and free from persistent negative feelings. Freedom from negative feelings does not mean that low-scorers experience a lot of positive feelings.""",
        samples=[
            "I get irritated easily.",
            "I get stressed out easily.",
            "I get upset easily.",
            "I have frequent mood swings.",
            "I worry about things.",
            "I am much more anxious than most people.",
            "I am relaxed most of the time. (reversed)",
            "I seldom feel blue. (reversed)",
        ],
        note='sensitive/nervous vs. secure/confident',
        aspects=['volatility', 'withdrawl'],
    ),
    PersonalityTrait(
        name='extraversion',
        inverse='introversion',
        description="""Extraversion is characterized by breadth of activities (as opposed to depth), surgency from external activity/situations, and energy creation from external means.[39] The trait is marked by pronounced engagement with the external world. Extraverts enjoy interacting with people, and are often perceived as full of energy. They tend to be enthusiastic, action-oriented individuals. They possess high group visibility, like to talk, and assert themselves.[40] Extraverted people may appear more dominant in social settings, as opposed to introverted people in this setting.[41]

Introverts have lower social engagement and energy levels than extraverts. They tend to seem quiet, low-key, deliberate, and less involved in the social world. Their lack of social involvement should not be interpreted as shyness or depression; instead they are more independent of their social world than extraverts. Introverts need less stimulation, and more time alone than extraverts. This does not mean that they are unfriendly or antisocial; rather, they are reserved in social situations.[1]

Generally, people are a combination of extraversion and introversion, with personality psychologist Eysenck suggesting that these traits are connected somehow to our central nervous system.""",
        samples=[
            "I am the life of the party.",
            "I don't mind being the center of attention.",
            "I feel comfortable around people.",
            "I start conversations.",
            "I talk to a lot of different people at parties.",
            "I don't talk a lot. (reversed)",
            "I think a lot before I speak or act. (reversed)",
            "I don't like to draw attention to myself. (reversed)",
            "I am quiet around strangers. (reversed)",
            "I have no intention of talking in large crowds. (reversed)",
        ],
        note='outgoing/energetic vs. solitary/reserved',
        aspects=['enthusiasm', 'assertiveness'],
    ),
    PersonalityTrait(
        name='agreeableness',
        inverse='disagreeableness',
        description="""The agreeableness trait reflects individual differences in general concern for social harmony. Agreeable individuals value getting along with others. They are generally considerate, kind, generous, trusting and trustworthy, helpful, and willing to compromise their interests with others.[1] Agreeable people also have an optimistic view of human nature.

Disagreeable individuals place self-interest above getting along with others. They are generally unconcerned with others' well-being, and are less likely to extend themselves for other people. Sometimes their skepticism about others' motives causes them to be suspicious, unfriendly, and uncooperative.[42] Low agreeableness personalities are often competitive or challenging people, which can be seen as argumentative or untrustworthy.""",
        samples = [
            "I am interested in people.",
            "I sympathize with others' feelings.",
            "I have a soft heart.",
            "I take time out for others.",
            "I feel others' emotions.",
            "I make people feel at ease.",
            "I am not really interested in others. (reversed)",
            "I insult people. (reversed)",
            "I am not interested in other people's problems. (reversed)",
            "I feel little concern for others. (reversed)",
        ],
        note='friendly/compassionate vs. challenging/detached',
        aspects=['compassion', 'politeness'],
    )
    PersonalityTrait(
        name='conscientiousness',
        inverse='carelessness',
        description="""Conscientiousness is a tendency to display self-discipline, act dutifully, and strive for achievement against measures or outside expectations. It is related to the way in which people control, regulate, and direct their impulses. High conscientiousness is often perceived as being stubborn and focused. Low conscientiousness is associated with flexibility and spontaneity, but can also appear as sloppiness and lack of reliability. High scores on conscientiousness indicate a preference for planned rather than spontaneous behavior. The average level of conscientiousness rises among young adults and then declines among older adults""",
        samples=[
            'I am always prepared.',
            'I pay attention to details.',
            'I get chores done right away.',
            'I like order.',
            'I follow a schedule.',
            'I am exacting in my work.',
            'I never forget my belongings.',
            'I always end up being helpful to most things.',
            'I often remember where I last put my things.',
            'I give attention to my duties.',
        ],
        note='efficient/organized vs. easy-going/careless',
        aspects=['industriousness', 'orderliness'],
    )
]

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
