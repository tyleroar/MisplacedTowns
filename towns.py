#colors 1-5, will 
from enum import Enum
import random
class Color(Enum):
  DISCARD = 0
  RED = 1
  WHITE = 2
  YELLOW = 3
  GREEN = 4
  BLUE = 5
class Card:
  def __init__(self,color,value):
    self.color = color
    self.value = value
  #def colorNumToStr(self,Color):
  #  if Color == 1:
  #    return ""
  def show(self):
    if self.value==1:
      print "{}:{}".format(Color(self.color).name,"HS")
    else:
      print "{}:{}".format(Color(self.color).name,self.value)
  def __str__(self):
    if self.value == 1:
      return "{}:{}".format(Color(self.color).name,"HS")
    return "{}:{}".format(Color(self.color).name,self.value)
  def __eq__(self, other):
    """Overrides the default implementation"""
    if isinstance(other, Card):
        return self.color == other.color and self.value == other.value
    return False
  def __ne__(self, other):
    """Overrides the default implementation"""
    return not self.__eq__(other)
class Deck:
  def __init__(self):
    self.cards = []
   # self.build()
  def build(self):
    for color in range(1,6):
      for value in range(1,11):  #we're using 1 as the special handshake value
        self.cards.append(Card(color,value))
  def insertCard(self,card):
    self.cards.append(card)
  def deleteCard(self,card):
    if self.hasCard(card)==False:
      raise Exception("can't delete card i dont have!")
    else:
      for val in self.cards:
        if val == card:
          self.cards.remove(val)
          break
  def revealAll(self):
    for j in self.cards:
      j.show()
  def shuffle(self):
    for i in range(len(self.cards)-1,0,-1):
      r = random.randint(0,i)
      self.cards[i],self.cards[r] = self.cards[r],self.cards[i]
  def hasCard(self,card):
    for x in self.cards:
      if x == card:
        return True
    return False
  def __len__(self):
    return len(self.cards)
def printGameBoard(communityDecks):
  P1Deck = communityDecks['P1']
  P2Deck = communityDecks['P2']
  for number in range(10,0,-1):
    for color in range (1,6):
      card = Card(Color(color).value,number)
      if P1Deck.hasCard(card):
        #pass
      #  print Color(color).name
        print str(number).ljust(7,' '),
      else:
        print ''.ljust(7,' '),

    print "\n"
  for color in range(1,6):
    card = Card(Color(color).value,number)
    colorname = Color(color).name
    deck = communityDecks[colorname]
    if len(deck)>0:
      card = deck.cards[len(deck.cards)-1]
      value = card.value
    else:
      value = ''
    if value == 1:
      value = 'HS'
    output=colorname[0]+str(value)
    print output.ljust(7,' '),
  deck = communityDecks['DISCARD']
  if len(deck)>0:
    card = deck.cards[len(deck.cards)-1]
    value = card.value
    colorname = Color(card.color).name
  else:
    value = ''
  if value == '':
    output="Discard:Empty"
  else:
    if value == 1:
      value = 'HS'
    output="Discard:"+colorname[0]+str(value)
  print output
  #now need to print out P2Deck...upside down from how we did P1
  for number in range(1,11,1):
    for color in range (1,6):
      card = Card(Color(color).value,number)
      if P2Deck.hasCard(card):
        print str(number).ljust(7,' '),
      else:
        print ''.ljust(7,' '),
    print "\n"
def buildCommunityDeck():
  community = dict()#
  for i in range(1,6):
    colorname = Color(i).name
    community[colorname] = Deck()
  community['DISCARD'] = Deck()
  community['P1'] = Deck()
  community['P2'] = Deck()
  #p1 and p2 community are the cards that they have already played!
  return community
def mapinputtocolor(i):
  if len(i)<1:
    return None
  if i[0] == 'R':
    return Color(1)
  if i[0] == 'W':
    return Color(2)
  if i[0] == 'Y':
    return Color(3)
  if i[0] == 'G':
    return Color(4)
  if i[0] == 'B':
    return Color(5)
  if i[0] == 'D':
    return Color(0)
  return None
def getMoveType():
  color = None
  print "It is your turn.  Enter the color you want to play on, or D to discard"
  while color == None:
    row = raw_input()
    color = mapinputtocolor(row)
    if color == None:
      print "Invalid, selection, try again"
  return color
def getMoveColor():
  color = None
  print "Enter the color you want to play on"
  while color == None:
    row = raw_input()
    color = mapinputtocolor(row)
    if color == None or color == Color(0):
      print "Invalid, selection, try again"
  return color
###this method doesn't validate player has the card
def getCardValue(playerHand,color):
  value = None
  print "Enter the card value to play"
  while value == None:
    value = int(raw_input())
    if value >10 or value < 1:
      print "get card invalid selection, try again"
  card = Card(color.value,value)
  return card
#def getPlayMove(playerHand):
 # return ""
def getMove(playerName,playerHand,communityDeck):
  print playerName
  color = getMoveType()
  discard = False
  if color == Color.DISCARD:
    discard = True
    color=getMoveColor()
#  if color == Color.DISCARD:
  card = getCardValue(playerHand,color)
  while not playerHand.hasCard(card):
    print "You do not have that card, please try again"
    color = getMoveType()
    discard = False
    if color == Color.DISCARD:
      discard = True
   #   color = getMoveColor()
    card = getCardValue(playerHand,color)
  if discard==True:
    playerHand.deleteCard(card)
    communityDeck['DISCARD'].insertCard(card)
  elif discard == False:
    print "playing card: {}".format(card)
    communityDeck[playerName].insertCard(card)
    playerHand.deleteCard(card)
      
    
def main():
  mainDeck = Deck()
  mainDeck.build()
  mainDeck.shuffle()
  #a.revealAll()
  P1Hand = Deck()
  P2Hand = Deck()
  community = buildCommunityDeck()
  for i in range(0,8):
    P1Hand.insertCard(mainDeck.cards.pop())
    P2Hand.insertCard(mainDeck.cards.pop())
  print "Player 1 cards"
  P1Hand.revealAll()
  print "player 2 cards"
  P2Hand.revealAll()
  print "Remaining:"
  mainDeck.revealAll()
  b = Card(Color.RED.value,10)
  while True:
    print "Player 1 cards"
    P1Hand.revealAll()
    printGameBoard(community)
    getMove("P1",P1Hand,community)
    P2Hand.revealAll()
    printGameBoard(community)
    getMove("P2",P2Hand,community)
if __name__=="__main__":
  main()