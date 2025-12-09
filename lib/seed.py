# app/seed.py

from models import Game, session  # Make sure your models.py defines Game and session
from faker import Faker
import random

fake = Faker()

print("Seeding games...")

session.query(Game).delete()
session.commit()

specific_games = [
    Game(title="Breath of the Wild", platform="Switch", genre="Adventure", price=60),
    Game(title="Final Fantasy VII", platform="Playstation", genre="RPG", price=30),
    Game(title="Mario Kart 8", platform="Switch", genre="Racing", price=50),
    Game(title="Candy Crush Saga", platform="Mobile", genre="Puzzle", price=0),
]

session.bulk_save_objects(specific_games)
session.commit()


random_games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
    for _ in range(50)
]

session.bulk_save_objects(random_games)
session.commit()

print("Seeding complete! Total games in database:", session.query(Game).count())
