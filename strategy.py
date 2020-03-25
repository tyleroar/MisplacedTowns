

def getColorDict(deck):
  colorSums = dict()
  for i in range(1,6):
    colorSums[i] = 0
  for x in deck.cards:
    if x.value!=1: #haven't decided how to handle handshakes yet
      colorSums[x.color]+=x.value
  return colorSums
def getBestColor(deck):
  bestColor = 0
  bestValue = -1
  colorSums = getColorDict(deck)
  bestValue = colorSums[1]
  for i in range(2,6):
    if colorSums[i]>bestValue:
      bestValue=colorSums[i]
      bestColor = i
  return bestColor