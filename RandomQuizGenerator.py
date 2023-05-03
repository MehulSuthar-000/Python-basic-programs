#!C:\Users\mehul\AppData\Local\Programs\Python\Python310\python.exe
# random quiz generator.py - Creates quizzes with question and answers in random order,along with the answer key

import random

# The quiz dataset for generating questions and answer
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


for quizNum in range(5):
    quizFile = open('quiz%s.txt'%(quizNum+1) , 'w')
    answerFile = open('answerKey%s.txt'%(quizNum+1),'w')

# write the header
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    #shuffle the states values
    states = list(capitals.keys())
    random.shuffle(states)

    # generating 10 question of all states
    for questionNum in range(10):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)] #deleting the correct answer from the list of wrong answers
        wrongAnswer = random.sample(wrongAnswer,3)  #taking 3 random smaples from the wrongAnswer list
        answerOptions = wrongAnswer + [correctAnswer]
        random.shuffle(answerOptions)
    
    #create question for each question number
        quizFile.write( ' %s  What is the capital of state %s'%(questionNum +1 , states[questionNum]))

        #generating answer options in a proper format
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')

        # Write the answer key to a file.
        answerFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

answerFile.close()
quizFile.close()
