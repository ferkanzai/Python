class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return "{0}. \"{1}\". {2}, {3}. {4}, {5}.".format(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location)

class Marketplace:
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, listing):
        self.listings.remove(listing)

    def show_listings(self):
        for listing in self.listings:
            print(listing)

class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        self.location = location
        self.is_museum = is_museum

    def sell_artwork(self, artwork, price):
        if artwork.owner.name == self.name:
            listing = Listing(artwork, price, artwork.owner)
            veneer.add_listing(listing)

    def buy_artwork(self, artwork):
        if artwork.owner.name != self.name:
            for listing in veneer.listings:
                if listing.art.title == artwork.title:
                    art_listing = listing
                artwork.owner = self
                veneer.remove_listing(listing)

class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return "{0} is selling \"{1}\" for ${2}M (USD)".format(self.seller.name, self.art.title, self.price)

veneer = Marketplace()
print(veneer.show_listings())
edytta = Client('Edytta Halpirt', 'Private Collection', False)
girl_with_mandolin = Art('Picasso, Pablo', 'Girl with a Mandolin (Fanny Tellier)', 'oil on canvas', 1910, edytta)
print(girl_with_mandolin)
moma = Client('The MOMA', 'New York', True)
prado = Client('Museo del Prado', 'Madrid', True)
edytta.sell_artwork(girl_with_mandolin, 6)
veneer.show_listings()
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
veneer.show_listings()
maja_desnuda = Art('Goya, Francisco de', 'La Maja Desnuda', 'oil on canvas', 1797, prado)
print(maja_desnuda)
prado.sell_artwork(maja_desnuda, 50)
veneer.show_listings()
moma.buy_artwork(maja_desnuda)
print(maja_desnuda)
moma.sell_artwork(maja_desnuda, 40)
veneer.show_listings()
prado.buy_artwork(maja_desnuda)
print(maja_desnuda)

#Here are some more things you could try:
#Add a wallet instance variable to clients, update the buying and selling of artworks to also exchange dollar amounts.
#Create a wishlist for your clients, things that are listed but they’re not sure if they should purchase just yet.
#Create expiration dates for listings! Have out of date listings automatically removed from the marketplace.
