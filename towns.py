#colors 1-5, will 
import sys
import ai
from cards import Card
from cards import Deck
from cards import Color
from strategy import *

def printGameBoard(communityDecks):
  P1Deck = communityDecks['P1']
  P2Deck = communityDecks['P2']
  for number in range(10,0,-1):
    for color in range (1,6):
      card = Card(Color(color).value,number)
      if P1Deck.hasCard(card):
        #pass
      #  print Color(color).name
        value = number
        if value==1:
          value="HS*"+str(P1Deck.countCard(card))
        print str(value).ljust(7,' '),
      else:
        print ''.ljust(7,' '),

    print ""
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
  print "" #just need a newline
 # deck = communityDecks['DISCARD']
 # if len(deck)>0:
 #   card = deck.cards[len(deck.cards)-1]
 #   value = card.value
 #   colorname = Color(card.color).name
 # else:
 #   value = ''
 # if value == '':
 #   output="Discard:Empty"
 # else:
 #   if value == 1:
 #     value = 'HS'
 #   output="Discard:"+colorname[0]+str(value)
 # print output
  #now need to print out P2Deck...upside down from how we did P1
  for number in range(1,11,1):
    for color in range (1,6):
      card = Card(Color(color).value,number)
      if P2Deck.hasCard(card):
        value = number
        if value==1:
          value="HS*"+str(P2Deck.countCard(card))
        print str(value).ljust(7,' '),
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
  community['mainDeck'] = Deck()
  community['mainDeck'].build()
  #mainDeck.revealAll()
  community['mainDeck'].shuffle()
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
    try:
      value = int(raw_input())
    except:
      value = 0
    if value >10 or value < 1:
      print "get card invalid selection, try again"
  card = Card(color.value,value)
  return card
#def getPlayMove(playerHand):
 # return ""

#this hould prompt player where they want to draw form, add it to their hand and remove it from wherever it is at

def getDraw(playerName,playerHand,communityDeck,lastColor,discard):
  color = None
  print "Enter the color you want to draw from or D to draw"
  while color == None:
    row = raw_input()
    color = mapinputtocolor(row)
    if color == None:
      continue
    if color == Color(0):
      #this means they're drawing from the main deck
      if len(communityDeck['mainDeck'])==0:
        raise Exception("no cards left to draw from")
      card = communityDeck['mainDeck'].cards.pop()
      playerHand.insertCard(card)
    else:
      if color == lastColor and discard==True:
        print "you can't pick up from the pile you just discarded to!"
        color = None
        continue
      #they're picking up from the community card pile
      
      if len(communityDeck[color.name])==0:
        print "no cards to pick up from that pile!"
        color=None#force ot got through the loop again
      else:
        card=communityDeck[color.name].cards.pop()
        playerHand.insertCard(card)
   # if communityDeck['DISCARD']
    if color == None:
      print "Invalid, selection, try again"
  
def isValidMove(card,playerHand,communityDeck,playerName,discard):
  #check if the card 
  if discard == True:
    return playerHand.hasCard(card)
  if not playerHand.hasCard(card):
    return False
  for x in communityDeck[playerName].cards:
    if x.color == card.color and x.value>card.value:
      return False
  return True
def  getFullMove(playerName,playerHand,communityDeck):
  validMove= False
  discard = False
  while not validMove:
    fullmove = raw_input()
    if len(fullmove)<2:
      print "Please enter a valid move (move text too short)"
      continue
    else:
      if fullmove[0] == "D":
        discard = True
        row = fullmove[1]
        color = mapinputtocolor(row)
        if color == None or color == Color(0):
          print "Invalid color selection, try again"
          continue
        else:
          try:
            value = int(fullmove[2:])
          except:
            print "couldn't parse out value non-int encountered"
            continue
        validMove=True
      else:
        discard= False
        row = fullmove[0]
        color = mapinputtocolor(row)
        if color == None or color == Color(0):
          print "invalid color section try again"
          continue
        else:
          try:
            value = int(fullmove[1:])
          except:
            print "coudln't parse out value, non-int encountered"
            continue
          validMove=True
    #at this point we should have discard,color and int
      card = Card(color.value,value)
    if not isValidMove(card,playerHand,communityDeck,playerName,discard):
      validMove=False
      if not playerHand.hasCard(card):
        print "You don't have that card"
      else:
        print "That card is not ascending, please try again"
  if discard==True:
    playerHand.deleteCard(card)
    communityDeck[color.name].insertCard(card)
  elif discard == False:
    print "playing card: {}".format(card)
    communityDeck[playerName].insertCard(card)
    playerHand.deleteCard(card)
  return color,discard
def getMove(playerName,playerHand,communityDeck):
  print "{} it is your move.  Enter the color to play on and the card value, or enter D and the card color and value to play".format(playerName)
  color,discard=getFullMove(playerName,playerHand,communityDeck)
  getDraw(playerName,playerHand,communityDeck,color,discard)
  return


def scoreDeck(deck):
  scores = dict()
  for color in range (1,6):
    scores[Color(color).name] = 0
    multiplier=1
    total=0
    cardcount=0
    for number in range(1,11,1):
      card = Card(Color(color).value,number)
      if number == 1:
        multiplier+=deck.countCard(card)
        if deck.countCard(card)>0:
          if cardcount==0:
            total=-20
            cardcount+=deck.countCard(card)
      else:
        if deck.hasCard(card):
          if cardcount==0:
            cardcount+=1
            total=-20
          total+=card.value
      scores[Color(color).name] = total*multiplier
      if cardcount>=8:
        scores[Color(color).name] +=20 #20 point bonus for having 8 cards in an expedition
  totalScore = 0
  for color in range (1,6):
    totalScore+=scores[Color(color).name]
  print scores
  return totalScore

def printGameSummary(deck):
  P1Score=scoreDeck(deck['P1'])
  P2Score = scoreDeck(deck['P2'])
  print P1Score
  print P2Score
  if P1Score>P2Score:
    print "Player 1 won!!"
  elif P1Score<P2Score:
    print "Player 2 won!!"
  else:
    print "It's a tie!"

  return P1Score,P2Score
  #P1Deck = deck['P1']
  #P2Deck = deck['P2']

  #need to score both players hands
 # deck['P1']
 # deck['P2']
#game is over when 0 cards left in the main deck
def gameOver(deck):
  return len(deck)==0

def simulateAGame():
  P1Hand = Deck()
  P2Hand = Deck()
  community = buildCommunityDeck()
  for i in range(0,8):
    P1Hand.insertCard(community['mainDeck'].cards.pop())
    P2Hand.insertCard(community['mainDeck'].cards.pop())
#  print "player 2 cards"
#  P2Hand.revealSorted()
  print "Remaining:"
 # mainDeck.revealAll()
  b = Card(Color.RED.value,10)
  computer = ai.DumbAI()
  computer2=ai.AlwaysDraw()
  while True:
    if len(P2Hand)<8:
      raise Exception("P2 doesn't have 8 cards")
    if len(P1Hand)<8:
      raise Exception("P1 doesn't have 8 cards")
    print "Cards remaining: {}".format(len(community['mainDeck']))
    print "Player 1 cards"
    P1Hand.revealSorted()
    printGameBoard(community)
#    getMove("P1",P1Hand,community)
    computer.computerMakeMove("P1",P1Hand,community)
    if gameOver(community['mainDeck']):
      break
    print "Cards remaining: {}".format(len(community['mainDeck']))
   # P2Hand.revealSorted()
    printGameBoard(community)
   # getMove("P2",P2Hand,community)
    computer2.computerMakeMove("P2",P2Hand,community)
    if gameOver(community['mainDeck']):
      break
  return printGameSummary(community)

def main():
  P1 = Deck()
  for x in range(1,10):
    card = Card(2,x)
    P1.insertCard(card)
  for x in range(1,8):
    P1.insertCard(Card(3,x))
  for x in range(7,10):
    P1.insertCard(Card(4,x))  
  print getColorDict(P1)
  return
  P1Wins = 0
  P2Wins = 0
  P1CumulativeScore = 0
  P2CumulativeScore = 0
  for i in range(0,100):
    P1Score,P2Score = simulateAGame()
    P1CumulativeScore+=P1Score
    P2CumulativeScore+=P2Score
    if P1Score>P2Score:
      P1Wins+=1
    elif P2Score>P1Score:
      P2Wins+=1
    print  "P1 is dumb P2 is always draw!"
    print "After 100 rounds, P1Wins: {} P2Wins: {}\nP1 Total:{}, P2 Total: {}".format(P1Wins,P2Wins,P1CumulativeScore,P2CumulativeScore)

if __name__=="__main__":
  main()