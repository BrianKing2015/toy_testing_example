import random

import faker
from locust import HttpUser, task, between

URL = "http://127.0.0.1:5000/artists"


class ArtistSpawn(HttpUser):
    wait_time = between(10, 30)

    def on_start(self):
        fake = faker.Faker()
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.birth_year = random.randint(1850, 2022)

    @task(1)
    def insert_artist_for_load_test(self):
        payload = {"first_name": self.first_name, "last_name": self.last_name, "birth_year": self.birth_year}
        headers = {'Content-Type': 'application/json'}
        self.client.post(
            url=URL,
            json=payload,
            headers=headers
        )

    @task(3)
    def list_all_artist_for_load_test(self):
        self.client.get(url=URL)
