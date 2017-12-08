class vector:
    def __init__(self, word, weight):
        self.word = word
        self.weight = float(weight)

    def __eq__(self, other):
        return self.word == other.word

    def __str__(self):
        return '(%s,%.3f)' % (self.word, self.weight)

    def __repr__(self):
        return '(%s,%.3f)' % (self.word, self.weight)

    def __gt__(self, other):
        return self.word>other.word

    def __lt__(self, other):
        return self.word<other.word

    def __ne__(self, other):
        return self.word != other.word

    def __hash__(self):
        return self.word.__hash__()