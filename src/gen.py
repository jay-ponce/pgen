
import string
import random
import requests
from functools import lru_cache


class Generator:

    def __init__(self):
        self.leet_map = {
            'a': ['@', 'A', 'a'],
            'b': ['8', 'B', 'b'],
            'e': ['3', 'E', 'e'],
            'g': ['9', 'G', 'g'],
            'i': ['1', 'I', 'i', '!'],
            'l': ['1', 'L', 'l'],
            'o': ['0', 'O', 'o'],
            's': ['5', '$', 'S', 's'],
            't': ['7', 'T', 't'],
            'z': ['2', 'Z', 'z'],
        }

    def generate_password(self, length):
        password = ''
        for _ in range(int(length)):
            ascivalu = random.randint(33, 125)
            password += chr(ascivalu)

        return password

    def transform_char(self, char, force_letter=False):
        options = self.leet_map.get(char.lower(), [char.lower(), char.upper()])
        choice = random.choice(options)
        while force_letter and not choice.isalpha():
            choice = random.choice([char.lower(), char.upper()])
        return choice

    @lru_cache(maxsize=32)
    def fetch_words(self, length):
        pattern = '?' * length
        response = requests.get(
            f'https://api.datamuse.com/words?sp={pattern}&max=1000')
        words = [entry['word']
                 for entry in response.json() if entry['word'].isalpha()]
        return [word for word in words if len(word) == length]

    def is_readable(self, username, min_letters=4, max_non_letters=2):
        # Rule 1: Starts and ends with a letter
        if not username[0].isalpha() or not username[-1].isalpha():
            return False

        # Rule 2 & 3: Count letters and non-letters
        letters = sum(c.isalpha() for c in username)
        non_letters = len(username) - letters

        if letters < min_letters or non_letters > max_non_letters:
            return False

        # Rule 4: Avoid repeated special characters
        specials = "!@#$%^&*()_-+=<>?/|\\~`"
        for i in range(1, len(username)):
            if username[i] in specials and username[i] == username[i-1]:
                return False

        return True

    def generate_human_readable_username(self, length):
        words = self.fetch_words(length)
        for _ in range(20):  # Try up to 20 times to find a readable one
            if not words:
                raise ValueError(f"No words of length {length} found.")

            word = random.choice(words)
            transformed = [self.transform_char(c) for c in word]

            # Optionally insert a number
            if random.random() < 0.5:
                pos = random.randint(1, len(transformed) - 2)
                transformed.insert(pos, str(random.randint(0, 9)))

            username = ''.join(transformed)

            if self.is_readable(username):
                return username

        raise RuntimeError(
            "Failed to generate a readable username after 20 tries.")

    def generate_username(self, length):
        username = ''

        for _ in range(int(length)):
            ascivalu = random.randint(
                *random.choice([(48, 57), (65, 90), (97, 122)]))
            username += chr(ascivalu)

        return username

    def generate_pin(self, length):
        # Generate a random number between 0 and 9
        pin = random.choices(range(10), k=int(length))

        # Ensure the first and last digits are not zero.
        pin[0] = random.randint(1, 9)
        pin[-1] = random.randint(1, 9)

        return ''.join(map(str, pin))
