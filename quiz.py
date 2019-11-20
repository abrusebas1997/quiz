class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

print("Can You Pass This Basic World History Quiz?")

question_prompts = [
     "1.World War I began in which year?\n(a) 1923\n(b) 1938\n(c) 1917\n(d) 1914\n",
     "2.Adolf Hitler was born in which country?.\n(a) France\n(b) Germany\n(c) Austria\n(d) Hungary\n",
     "3.How many World Wars until now have taken place? Please enter an integer.\n",
     "4.Alaska was the last state to enter the Union, true or false? Please enter 1 for True or 0 for False.\n"
]

questions = [
     Question(question_prompts[0], "d"),
     Question(question_prompts[1], "c"),
     Question(question_prompts[2], "2"),
     Question(question_prompts[3], "1"),

]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)

          running = True
          while running:
              if answer == 'a' or answer =='b' or answer =='c' or answer =='d' or answer =='1' or answer == '0' or answer =='2' or answer =='3':
                  running = False
                  break
              if answer != 'a' or answer !='b' or answer !='c' or answer !='d' or answer !='1' or answer != '0' or answer !='2' or answer !='3':
                  print("Incorrect syntax")
                  answer = input(question.prompt)

          if answer == question.answer:
               score += 1
               print("Correct!")

          else:
               print("Not Correct!")
               print("The correct answer is", question.answer)
     print("you got", score, "out of", len(questions), )

run_quiz(questions)

print("")
print("")


# question3 = input("How many World Wars until now have taken place? Please enter an integer.\n")
# def numeric_response(question3):
#
#     if question3 == 2:
#         print("Correct!")
#     else:
#         print("Not Correct!")
#
# numeric_response(question3)
