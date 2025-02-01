class Base:
    def __init__(self, size=10) -> None:
        self.base = [False for _ in range(size)]
        self.attacked = 0

    def attack(self, start) -> None:
        if not self.base[start] :
           self.base[start] = True		# True is attacked
           self.attacked += 1

    def is_game_over(self) -> bool:
        return self.attacked == len(self.base):


