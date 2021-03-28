import random
def main():
  score = float(input("Enter score: "))
  print(level_of_score(score))

def level_of_score(score):
 """Determine level of score"""
 if 0<= score< 50:
     return "Bad score"
 elif 50<= score <90:
     return "Passable"
 elif 90<= score <=100:
     return "Excellent"
 else:
     return "Invalid score"
main()


def main():
 random_score = randint(0,101)
 print(level_of_score2(random_score))

 def level_of_score2(score) :
  """Determine level of score"""
    if 0 <= score < 50 :
         return "Bad score"
    elif 50 <= score < 90 :
         return "Passable"
    elif 90 <= score <= 100 :
         return "Excellent"
    else :
         return "Invalid score"
