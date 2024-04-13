

class BaseOperative:
    def __init__(self,
                 M: int,
                 M_length: int,
                 APL: int,
                 GA: int,
                 DF: int,
                 SV: int,
                 W: int,
                 base: int,
                 keywords: tuple):
        self.M = M
        self.M_length = M_length
        self.APL = APL
        self.GA = GA
        self.DF = DF
        self.SV = SV
        self.W = W
        self.base = base
        self.keywords = keywords

        self.x = 0
        self.y = 0


class BaseTeam:
    def __init__(self):
        self.operatives = []

    def add_operative(self, operative: BaseOperative):
        self.operatives.append(operative)
