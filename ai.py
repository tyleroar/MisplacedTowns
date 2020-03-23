from towns import *

class AlwaysDraw:
  #this method is just for the decision of which card to play
  #will put the decision of what card to draw in separate func
  def computerMakePlayMove(self,playerName,playerHand,communityDeck):
    playerHand.sortDeck()
    print "beep boop, thinking"

    #just have him play the first available card that he can?
    for x in playerHand.cards:
      if isValidMove(x,playerHand,communityDeck,playerName,False):
        #make this move....
        print "computer playing card: {}".format(x)
        communityDeck[playerName].insertCard(x)
        playerHand.deleteCard(x)
        #card = communityDeck['mainDeck'].cards.pop()
    #   print "computer drew from main deck and got:{}".format(card)
        #playerHand.insertCard(card)     
        return x.color,False
    for x in playerHand.cards:
      if isValidMove(x,playerHand,communityDeck,playerName,True):
        #make this discard move
        playerHand.deleteCard(x)
        print "computer discarded card {}".format(x)
        communityDeck[Color(x.color).name].insertCard(x)
        return x.color,True
      #  card = communityDeck['mainDeck'].cards.pop()
    #    print "computer drew from main deck and got:{}".format(card)
      # playerHand.insertCard(card)
    raise exception("Computer coulnd't find a move to make :(")
  def computerMakeDraw(self,playerName,playerHand,communityDeck,lastColor,discard):
  #lets have the computer always just draw from the board if there is anything there!
    for color in range(1,6):
      if color == lastColor and discard == True:
        continue#can't pick up from where they just discarded!
      # card = Card(Color(color).value,number)
      colorname = Color(color).name
      deck = communityDeck[colorname]
      if len(deck)>0:
        card = deck.cards.pop()
        playerHand.insertCard(card)
        print "Computer picked up card: {} from discard".format(card)
        return
        #have the player take this card
    print "computer drew from the deck"
    card = communityDeck['mainDeck'].cards.pop()
    playerHand.insertCard(card)

  def computerMakeMove(self,playerName,playerHand,communityDeck):
    color,discard = self.computerMakePlayMove(playerName,playerHand,communityDeck)
    self.computerMakeDraw(playerName,playerHand,communityDeck,color,discard)

class DumbAI:
  #this method is just for the decision of which card to play
  #will put the decision of what card to draw in separate func
  def computerMakePlayMove(self,playerName,playerHand,communityDeck):
    playerHand.sortDeck()
    print "beep boop, thinking"

    #just have him play the first available card that he can?
    for x in playerHand.cards:
      if isValidMove(x,playerHand,communityDeck,playerName,False):
        #make this move....
        print "computer playing card: {}".format(x)
        communityDeck[playerName].insertCard(x)
        playerHand.deleteCard(x)
        #card = communityDeck['mainDeck'].cards.pop()
    #   print "computer drew from main deck and got:{}".format(card)
        #playerHand.insertCard(card)     
        return x.color,False
    for x in playerHand.cards:
      if isValidMove(x,playerHand,communityDeck,playerName,True):
        #make this discard move
        playerHand.deleteCard(x)
        print "computer discarded card {}".format(x)
        communityDeck[Color(x.color).name].insertCard(x)
        return x.color,True
      #  card = communityDeck['mainDeck'].cards.pop()
    #    print "computer drew from main deck and got:{}".format(card)
      # playerHand.insertCard(card)
    raise exception("Computer coulnd't find a move to make :(")
  def computerMakeDraw(self,playerName,playerHand,communityDeck,lastColor,discard):
    #lets have computer always draw new card
    print "computer drew from the deck"
    card = communityDeck['mainDeck'].cards.pop()
    playerHand.insertCard(card)
    return
  #lets have the computer always just draw from the board if there is anything there!
    for color in range(1,6):
      if color == lastColor and discard == True:
        continue#can't pick up from where they just discarded!
      # card = Card(Color(color).value,number)
      colorname = Color(color).name
      deck = communityDeck[colorname]
      if len(deck)>0:
        card = deck.cards.pop()
        playerHand.insertCard(card)
        print "Computer picked up card: {} from discard".format(card)
        return
        #have the player take this card


  def computerMakeMove(self,playerName,playerHand,communityDeck):
    color,discard = self.computerMakePlayMove(playerName,playerHand,communityDeck)
    self.computerMakeDraw(playerName,playerHand,communityDeck,color,discard)


if __name__=="__main__":
  pass