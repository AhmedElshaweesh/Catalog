from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Ahmed Sayed Ahmed", email="ahmed_alshaweesh@yahoo.com",
             picture='http://all-best.co/wp-content/'
             'uploads/2017/08/unnamed-file-231.jpg')
session.add(User1)
session.commit()

# Menu for UrbanBurger
category1 = Category(user_id=1, name="Urban Burger")

session.add(category1)
session.commit()


Item1 = Item(user_id=1, name="French Fries",
             description="with garlic and parmesan",
             price="$2.99", created="Entree", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Chicken Burger",
             description="Juicy grilled chicken",
             price="$5.50", created="Entree", category=category1)

session.add(Item2)
session.commit()

# Menu for Super Stir Fry
category2 = Category(user_id=1, name="Super Stir Fry")

session.add(category2)
session.commit()


Item1 = Item(user_id=1, name="Chicken Stir Fry",
             description="With your choice of noodles vegetables and sauces",
             price="$7.99", created="Entree", category=category2)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Peking Duck",
             description=" A famous duck dish from Beijing[1].",
             price="$25", created="Entree", category=category2)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Spicy Tuna Roll",
             description="Seared rare ahi, avocado, edamame ",
             price="15", created="Entree", category=category2)

session.add(Item3)
session.commit()

# Menu for Panda Garden
category1 = Category(user_id=1, name="Panda Garden")

session.add(category1)
session.commit()


Item1 = Item(user_id=1, name="Pho",
             description="a Vietnamese noodle soup consisting,banh pho.",
             price="$8.99", created="Entree", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Chinese Dumplings",
             description="a Chinese dumpling which consists of minced meat.",
             price="$6.99", created="Appetizer", category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Gyoza",
             description="light seasoning of Japanese gyoza with salt",
             price="$9.95", created="Entree", category=category1)

session.add(Item3)
session.commit()

# Menu for Thyme for that
category1 = Category(user_id=1, name="Thyme for That Vegetarian Cuisine ")

session.add(category1)
session.commit()


Item1 = Item(user_id=1, name="Tres Leches Cake",
             description="Rich, luscious sponge cake soaked in sweet milk.",
             price="$2.99", created="Dessert", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Mushroom risotto",
             description="Portabello mushrooms in a creamy risotto",
             price="$5.99", created="Entree", category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Honey Boba Shaved Snow",
             description="Milk snow layered with honey boba",
             price="$4.50", created="Dessert", category=category1)

session.add(Item3)
session.commit()

# Menu for Tony's Bistro
category1 = Category(user_id=1, name="Tony\'s Bistro ")

session.add(category1)
session.commit()


Item1 = Item(user_id=1, name="Shellfish Tower",
             description="Lobster, shrimp, sea snails, crawfish",
             price="$13.95", created="Entree", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Chicken and Rice",
             description="Chicken... and rice",
             price="$4.95", created="Entree", category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Mom's Spaghetti",
             description="Spaghetti with some incredible tomato sauce",
             price="$6.95", created="Entree", category=category1)

session.add(Item3)
session.commit()

# Menu for Andala's
category1 = Category(user_id=1, name="Andala\'s")

session.add(category1)
session.commit()


Item1 = Item(user_id=1, name="Lamb Curry",
             description="Slow cook that thang in a pool of tomatoes.",
             price="$9.95", created="Entree", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Chicken Marsala",
             description="Chicken cooked in Marsala wine sauce with mushrooms",
             price="$7.95", created="Entree", category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Potstickers",
             description="Delicious chicken.",
             price="$6.50", created="Appetizer", category=category1)

session.add(Item3)
session.commit()

print "added menu items!"
