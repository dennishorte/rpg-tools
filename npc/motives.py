import random

class Motive(object):
    def __init__(self, name, description, v, w, x, y, z):
        self.name = name
        self.description = description
        self.v = v
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return self.description

    def dump(self):
        return '\n'.join([
            self.description,
            '...' + self.v,
            '...' + self.w,
            '...' + self.x,
            '...' + self.y,
            '...' + self.z
        ])


_FLAT_MOTIVES = []
_MOTIVE_HIERARCHY = {}
    

def initialize_datastructures():
    with open('./res/motives.csv', 'r') as fin:
        for line in fin:
            tokens = line.strip().split(',', 7)
            if len(tokens) >= 7:
                motive = Motive(
                    tokens[5],
                    tokens[6],
                    tokens[4],
                    tokens[3],
                    tokens[2],
                    tokens[1],
                    tokens[0]
                )
                _FLAT_MOTIVES.append(motive)
                _MOTIVE_HIERARCHY.setdefault(motive.z, {})
                _MOTIVE_HIERARCHY[motive.z].setdefault(motive.y, {})
                _MOTIVE_HIERARCHY[motive.z][motive.y].setdefault(motive.x, {})
                _MOTIVE_HIERARCHY[motive.z][motive.y][motive.x].setdefault(motive.w, {})
                _MOTIVE_HIERARCHY[motive.z][motive.y][motive.x][motive.w].setdefault(motive.v, [])
                _MOTIVE_HIERARCHY[motive.z][motive.y][motive.x][motive.w][motive.v].append(motive)


class RandomMotive(Motive):
    def __init__(self):
        if not _FLAT_MOTIVES:
            initialize_datastructures()
        base = random.choice(_FLAT_MOTIVES)
        super().__init__(
            base.name,
            base.description,
            base.v,
            base.w,
            base.x,
            base.y,
            base.z
        )
        

if __name__ == "__main__":
    print(RandomMotive().dump())
