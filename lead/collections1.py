import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'lapai bugnai kryziai sirdys'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')


symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

colors = ['black', 'white']
sizes = ["S", 'M', "L"]

tshirts =  [(color, size) for color in colors for size in sizes]
print(tshirts)

for color in colors:
    for size in sizes:
        print((color,size))


tshirts2 = [(color,size) for size in sizes
                         for color in colors]

print(tshirts2)