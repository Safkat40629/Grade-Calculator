


def calcAverage(score1, score2, score3,score4,score5 ):
   average= (score1+score2+score3+score4+score5)/5
   return average

def determineGrade( userscore ):
    if( userscore < 60 ):
        return "F"
    elif( userscore <70 ):
        return "D"
    elif( userscore <80 ):
        return "C"
    elif (userscore < 90):
        return "B"
    elif (userscore <= 101):
        return "A"


def askForScore():
   score1 = float (input("please Enter Score 1 : " ))
   score2 = float(input("please Enter Score 2 : "))
   score3 = float (input("please Enter Score 3 : " ))
   score4 = float (input("please Enter Score 4 : " ))
   score5 = float (input("please Enter Score 5 : " ))

   return score1,score2,score3,score4,score5


def tableofResult(score1,score2,score3,score4,score5):
    print("\nScore\tLetter Grade\n")
    print(str(score1) + "\t"+ determineGrade(score1))
    print(str(score2) + "\t" + determineGrade(score2))
    print(str(score3) + "\t" + determineGrade(score3))
    print(str(score4) + "\t" + determineGrade(score4))
    print(str(score5) + "\t" + determineGrade(score5))



def main():
    score1, score2, score3, score4, score5 = askForScore()

    tableofResult(score1,score2,score3,score4,score5)

    print("\nYour average is", calcAverage(score1, score2, score3, score4,score5))



main()




