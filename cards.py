import random
from enum import Enum
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
  
  def sortDeck(self):
    self.cards.sort()
  def build(self):
    for color in range(1,6):
      for value in range(1,11):  #we're using 1 as the special handshake value
        self.cards.append(Card(color,value))
        if value==1: ##need 3 handshakes
          self.cards.append(Card(color,value))
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
 #get the sum of the values for a specific color (count HS as 0)
  def getColorSum(self,color):
    thesum = 0
    for x in self.cards:
      if x.color == color:
        if x.value != 1:
          thesum+=x.value
    return thesum
  def revealAll(self):
    for j in self.cards:
      j.show()
  def revealSorted(self):
    for color in range (1,6):
      for number in range(1,11,1):
        card = Card(Color(color).value,number)
        if self.hasCard(card):
          card.show()
  def shuffle(self):
    for i in range(len(self.cards)-1,0,-1):
      r = random.randint(0,i)
      self.cards[i],self.cards[r] = self.cards[r],self.cards[i]
  def hasCard(self,card):
    for x in self.cards:
      if x == card:
        return True
    return False
    #used for counting number of handshakes
  def countCard(self,card):
    count=0
    for x in self.cards:
      if x == card:
        count+=1
    return count
  def __len__(self):
    return len(self.cards)
