import requests
import random


class Questions:
    def __init__(self):
        self.response = requests.get("https://opentdb.com/api.php?amount=50&type=boolean")
        self.questions = self.response.json()['results']
        self.guessed_questions = []
        self.score = 0

    def random_question(self):
        if len(self.questions) != 0:
            question = random.choice(self.questions)
            self.guessed_questions.append(question)
            self.questions.remove(question)
            return question

        return False
