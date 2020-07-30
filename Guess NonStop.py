tryCount=1
while True:
    import random
    answer = random.randint(1, 100)
    userAnswer = input(f'Try to guess a number 0-100!\n Press "q" or "й" to quit\n')

    if userAnswer == 'q' or userAnswer == 'й' :
        print('Bye, Bye!')
        break
    else:
        check = True if userAnswer.isdigit() else False
        if check == False:
            print("Enter the integer")
        else:
            checkUserAnswer = int(userAnswer)
            if checkUserAnswer < answer:
                print(f'Its lower! Urs - {userAnswer}. Correct answer - {answer} !')
                tryCount+=1
            elif checkUserAnswer > answer:
                print(f'Its higher! Correct answer - {answer} !') 
                tryCount+=1
            else:
                print(f'OMG!!!! Congrats!\n Попыток - {tryCount}.')
                break