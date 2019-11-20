class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

print("Can You Pass This Basic World History Quiz?")

question_prompts = [
     "World War I began in which year?\n(a) 1923\n(b) 1938\n(c) 1917\n(d) 1914\n",
     "Adolf Hitler was born in which country?.\n(a) France\n(b) Germany\n(c) Austria\n(d) Hungary\n\n",
     "How many World Wars until now have taken place? Please enter an integer.\n"
]

questions = [
     Question(question_prompts[0], "d"),
     Question(question_prompts[1], "c"),
     Question(question_prompts[2], "2"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
               print("Correct!")
     print("you got", score, "out of", len(questions))

run_quiz(questions)

# print("")
# print("")
