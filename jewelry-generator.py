import random

class WeightedOption(object):
    def __init__(self, weight, value):
        self.weight = weight
        self.value_func = value if callable(value) else lambda: value

    def get(self):
        return self.value_func()

    def __str__(self):
        return 'WeightedOption({}, {})'.format(
            self.weight,
            self.value_func()
        )


class WeightedSelector(object):
    def __init__(self, *options):
        self.options = options
        self.total_weight = sum(opt.weight for opt in self.options)

    def select(self):
        target = random.random() * self.total_weight
        total = 0
        for opt in self.options:
            total += opt.weight
            if target < total:
                return opt.get()

        raise WeightedSelectionException('Random number ({}) was larger to total weight ({})'.format(
            target,
            self.total_weight
        ))
    

material_selector = WeightedSelector(
    WeightedOption(.5, 'tin'),
    WeightedOption(.5, 'pewter'),
    WeightedOption(1, 'nickel'),
    WeightedOption(.5, 'gemstone'),
    WeightedOption(.5, 'stone'),
    WeightedOption(1, 'iron'),
    WeightedOption(.33, 'bone'),
    WeightedOption(.33, 'ivory'),
    WeightedOption(.33, 'coral'),
    WeightedOption(1, 'wood'),
    WeightedOption(3, 'gold'),
    WeightedOption(1, 'electrum'),
    WeightedOption(3, 'silver'),
    WeightedOption(1, 'copper'),
    WeightedOption(1, 'brass'),
    WeightedOption(1, 'bronze'),
    WeightedOption(.2, 'mithril'),
    WeightedOption(.3, 'platinum'),
    WeightedOption(.1, 'adamantine'),
)
    
style_selector = WeightedSelector(
    WeightedOption(1, 'plain and simple'),
    WeightedOption(1, 'sturdy'),
    WeightedOption(1, 'elaborate and delicate'),
    WeightedOption(1, 'soft, curved elegance'),
    WeightedOption(1, 'gaudy with large embellishments'),
    WeightedOption(1, 'modernistic'),
    WeightedOption(1, 'woven/rope texture'),
    WeightedOption(1, 'symbols and glyphs'),
    WeightedOption(1, 'mosaic'),
    WeightedOption(1, 'floral motifs'),
    WeightedOption(1, 'vine motifs'),
    WeightedOption(1, 'religious motifs'),
    WeightedOption(1, 'industrial geometric motifs'),
    WeightedOption(1, 'winding serpent motifs'),
    WeightedOption(1, 'ribbon and bow motifs'),
    WeightedOption(1, 'bird/feather motifs'),
    WeightedOption(1, 'elemental motifs (ice/fire/water/earth/air)'),
    WeightedOption(1, 'geometric patterns (circles)'),
    WeightedOption(1, 'geometric patterns (squares)'),
    WeightedOption(1, 'geometric patterns (triangles)'),
    WeightedOption(1, 'depiction (roll on figurines table)'),
)

gem_number_selector = WeightedSelector(
    WeightedOption(1000, 0),
    WeightedOption(100, 1),
    WeightedOption(10, 2),
    WeightedOption(4, 3),
    WeightedOption(1, lambda: random.randint(4, 10)),
    WeightedOption(1, lambda: random.randint(11, 50)),
)

def select_material():
    material = { material_selector.select() }
    while random.random() < .05:
        material.add(material_selector.select())
    return ', '.join(material)


def select_number_of_gems():
    return gem_number_selector.select()
    # value = random.random()
    # if value < .25:
    #     return 0
    # elif value < .5:
    #     return 1
    # elif value < .75:
    #     return random.randint(2, 5)
    # else:
    #     return random.randint(6, 20)

def select_appearance_and_style():
    return style_selector.select()


jewelry_types = {
    'fastener': [
        'brooch',
        'buckle',
        'clasp',
        'pin',
        'chain',
        'button',
    ],
    'object': [
        'sconce',
        'music box',
        'clock',
        'painting frame',
        'paper weight',
        'reliquary',
        'mirror',
        'scepter',
        'chest/box',
        'architectural flourish',
        'censor',
        'ceremonial weapon',
        'bell',
        'tool',
        'furniture',
        'book cover',
        'candlestick/chandelier',
        'plate/platter',
        'utensil',
        'goblet/chalice/teacup',
    ],
    'figurine': [
        'humanoid',
        'mammal',
        'reptile',
        'bird',
        'amphibian',
        'fish',
        'invertebrate/insect',
        'dragon',
        'undead',
        'extraplanar creature',
        'egg',
        'building',
        'warrior',
        'priest',
        'mourner',
        'mage',
        'fool',
        'plant',
        'seashell',
        'automaton',
    ],
    'ring': [
        'signet ring',
        'beaded ring',
        # 'stone ring',
        'carved ring',
        # 'solitaire ring',
        # 'trinity ring',
        # 'cluster ring',
        'cocktail ring',
        # 'ring band',
        'rosary ring',
        'puzzle ring',
        'ecclesiastical ring',
        'key ring',
        # 'mourning ring',
        # 'curative ring',
        # 'wedding ring',
        'memento mori ring',
        'thumb ring',
        'armor ring',
        'poison ring',
    ],
    'clothing': [
        'dress/robe',
        'blouse/shirt',
        'hat/helm',
        'tunic',
        'cape',
        'bracer',
        'glove',
        'scarf',
        'belt/girdle',
        'pants',
        'skirt/kilt',
        'stockings/breeches',
        'shoes',
        'boots',
        # 'pauldrons',
        # 'breastplate',
        # 'gauntlet',
        'surcoat/tabard',
        'cowl/hood',
        'undergarments',
    ],
    'neckwear': [
        'torc',
        'pectoral necklace',
        'collar',
        'choker',
        'princess necklace',
        'matinee necklace',
        'opera necklace',
        'rope/lariat necklace',
        'rosary (y-shaped) necklace',
        'gorget',
        'carcanet',
        'pendant/amulet',
    ],
    'hair accessory': [
        'hairpin',
        'headband',
        'headdress',
        'hair ring',
        'hair pipe',
        'barrette',
        'decorative comb',
        'hair beads',
        'ferronniere', # A thin headband encircling the forehead, usually with a gemstone suspended at the center of the forehead.
        'crown/tiara',
    ],
    'other': [
        'arm band',
        'bracelet',
        'anklet',
        'body piercing',
        'facial piercing',
        'chatelaine',  # A piece of jewelry that is hooked onto a belt. It has chains holding household items like scissors, thimbles, keys, smelling salts, or signets. Basically the most 'extra' that a fanny pack can be.
        'locket',
        'medallion',
    ],
}

def select_type():
    return random.choice(
        random.choice(jewelry_types.values())
    )


class Jewelry(object):
    def __init__(self):
        self.material = select_material()
        self.num_gems = select_number_of_gems()
        self.style = select_appearance_and_style()
        self.kind = select_type()

    def __str__(self):
        return 'A {style} {kind} made of {material} with {num_gems} gems'.format(
            style=self.style,
            kind=self.kind,
            material=self.material,
            num_gems=self.num_gems,
        )


if __name__ == "__main__":
    for i in range(10):
        print(Jewelry())
