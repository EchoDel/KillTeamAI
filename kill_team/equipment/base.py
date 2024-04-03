

class BaseEquipment:
    def __init__(self,
                 A: int,
                 BS: int,
                 D: int,
                 D_crit: int,
                 special_rules: tuple):
        self.A = A
        self.BS = BS
        self.D = D
        self.D_crit = D_crit
        self.special_rules = special_rules


class BaseRangedWeapon(BaseEquipment):
    def __init__(self,
                 A: int,
                 BS: int,
                 D: int,
                 D_crit: int,
                 special_rules: tuple):
        super(BaseRangedWeapon).__init__(A, BS, D, D_crit, special_rules)


class BaseMeleeWeapon(BaseEquipment):
    def __init__(self,
                 A: int,
                 BS: int,
                 D: int,
                 D_crit: int,
                 special_rules: tuple):
        super(BaseMeleeWeapon).__init__(A, BS, D, D_crit, special_rules)
