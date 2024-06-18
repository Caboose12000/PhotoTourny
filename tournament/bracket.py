import os
import random

class Bracket:
    def __init__(self, image_dir):
        self.image_dir = image_dir
        self.images = self.load_images()
        self.rounds = []

    def load_images(self):
        return [os.path.join(self.image_dir, f) for f in os.listdir(self.image_dir) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))]

    def create_initial_pairs(self):
        random.shuffle(self.images)
        pairs = [(self.images[i], self.images[i+1]) for i in range(0, len(self.images), 2)]
        if len(self.images) % 2 == 1:
            pairs.append((self.images[-1], None))
        self.rounds.append(pairs)
        return pairs

    def get_next_round_pairs(self, winners):
        pairs = [(winners[i], winners[i+1]) for i in range(0, len(winners), 2)]
        if len(winners) % 2 == 1:
            pairs.append((winners[-1], None))
        self.rounds.append(pairs)
        return pairs
