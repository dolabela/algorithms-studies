"""
Splendor is a card-based board game where players buy cards in exchange for colored gems. In this game, today, we care about two things, gems and cards.

Players can have any number of gems of five different colors: (B)lue, (W)hite, (G)reen, (R)ed, and (Y)ellow.

Players can exchange gems for cards. A card appears as such:

+----------+
| G |
| |
| |
| 3W |
| 2G |
| 1R |
+----------+

This indicates that the card costs 3 (W)hite gems, 2 (G)reen gems, and 1 (R)ed. The “G” in the upper right indicates the color of the card (this will be useful later)

For this entire problem, we want to keep things simple by assuming that there is only one player.

The data model and structure of the program is up to you.

We want to write a function can_purchase() such that, given a particular card and collection of gems for a player, we return true if the player can afford the card, and false if they cannot.

We want to write a function purchase() such that, given a particular card and collection of gems for a player, we add the card to the players hand and subtract the cost from the players gems, if they are able to afford the card. The function should return true if the player can afford the card, and false if they cannot.

We want to introduce a new concept: for each card in a players hand of a given color, we want to reduce the cost of any new purchase by 1 gem for that held cards color. For example, if the player holds 2 (G)reen cards and 1 (R)ed, and we are considering a card that lists its cost as 3 (G)reen, 2 (R)ed, and 1 (B)lue, then the player should be able to purchase it for 1 G, 1 R, and 1 B.
"""



class Player():
    def __init__(self) -> None:
        self.cards = {}
        self.gems = {}

    def can_purchase(self, price: dict):
        for key_gem, gem_price in price.items():
            if gem_price <= self.gems.get(key_gem,0):
                pass
            else:
                return False
        return True

    def purchase(self, price: dict, card_name: str):
        price = self.modify_price(price)
        if self.can_purchase(price = price):
            for key_gem, gem_price in price.items():
                self.gems[key_gem] = self.gems[key_gem] - gem_price
            self.cards[card_name] = self.cards.get(card_name, 0) + 1

    def modify_price(self, price: dict):
        new_price = {}
        for key_gem, gem_price in price.items():
            if key_gem in self.cards:
                new_price[key_gem] = gem_price - self.cards[key_gem]
            else:
                new_price[key_gem] = gem_price
        return new_price


x = Player()
x.gems = {'g': 4, 'y': 3}  
x.purchase(card_name = "y", price = {'g': 1, 'y':2})
print(x.cards)
print(x.gems)