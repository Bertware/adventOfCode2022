from enum import Enum


class Sign(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @staticmethod
    def from_text(text: str):
        match text:
            case text if text in ['A', 'X']:
                return Sign.ROCK
            case text if text in ['B', 'Y']:
                return Sign.PAPER
            case text if text in ['C', 'Z']:
                return Sign.SCISSORS
            case _:
                print(f"DONT KNOW {text}")

    def score_against(self, other: 'Sign') -> int:
        if self == other:
            # print(f"You play {self} against {other}, equal, {3 + self.value}")
            return 3 + self.value
        if self.wins_against(other):
            # print(f"You play {self} against {other}, win, {6 + self.value}")
            return 6 + self.value
        else:
            # print(f"You play {self} against {other}, loss, {0 + self.value}")
            return 0 + self.value

    def wins_against(self, other: 'Sign') -> bool:
        if self == Sign.SCISSORS and other == Sign.ROCK:
            return False
        if self == Sign.ROCK and other == Sign.SCISSORS:
            return True
        return self.value > other.value

    @staticmethod
    def from_strategy(strategy: str, opponent_sign: 'Sign') -> 'Sign':
        if strategy == 'Y':  # Draw
            return opponent_sign
        if strategy == 'X':  # Lose
            match opponent_sign:
                case Sign.ROCK:
                    return Sign.SCISSORS
                case Sign.PAPER:
                    return Sign.ROCK
                case Sign.SCISSORS:
                    return Sign.PAPER
        if strategy == 'Z':  # Win
            match opponent_sign:
                case Sign.SCISSORS:
                    return Sign.ROCK
                case Sign.ROCK:
                    return Sign.PAPER
                case Sign.PAPER:
                    return Sign.SCISSORS


print(f"{Sign.PAPER.score_against(Sign.ROCK)} == 8")
print(f"{Sign.ROCK.score_against(Sign.PAPER)} == 1")

print(f"{Sign.PAPER.score_against(Sign.SCISSORS)} == 2")
print(f"{Sign.SCISSORS.score_against(Sign.PAPER)} == 9")

print(f"{Sign.SCISSORS.score_against(Sign.ROCK)} == 3")
print(f"{Sign.ROCK.score_against(Sign.SCISSORS)} == 7")

print(f"{Sign.ROCK.score_against(Sign.ROCK)} == 4")
print(f"{Sign.PAPER.score_against(Sign.PAPER)} == 5")
print(f"{Sign.SCISSORS.score_against(Sign.SCISSORS)} == 6")

f = open("advent2.txt", "r")
score = 0
for line in f:
    parts = line.split(' ')
    opponent = Sign.from_text(parts[0].strip())
    you = Sign.from_text(parts[1].strip())
    score += you.score_against(opponent)
print(score)

# Part 2
f = open("advent2.txt", "r")
score = 0
for line in f:
    parts = line.split(' ')
    opponent = Sign.from_text(parts[0].strip())
    you = Sign.from_strategy(parts[1].strip(), opponent)
    score += you.score_against(opponent)
print(score)
