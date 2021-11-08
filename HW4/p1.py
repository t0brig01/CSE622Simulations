import numpy as np 
import matplotlib.pyplot as plt

class candidate:
    numOfCorrect = 0
    def __init__(self,answers):
        self.answers = answers




epochs = 100
candidateCount = 20
questionCount = 5
epochPerformance1 = []
epochPerformance2 = []

for epoch in range(epochs):
    candidates = []
    HRCorrectAnswers = np.random.randint(1,6,size=questionCount)
    randomQuestion = questionCount - 1
    for x in range(candidateCount):
        answers = []
        for y in range(questionCount):
            answers.append(np.random.randint(1,6))
        answers[randomQuestion] = HRCorrectAnswers[randomQuestion] 
        candidates.append(candidate(answers))

    for cand in candidates:
        for x in range(len(cand.answers)):
            if(cand.answers[x] == HRCorrectAnswers[x]):
                cand.numOfCorrect = cand.numOfCorrect + 1

    totalQuestion = questionCount*candidateCount
    totalCorrect = 0
    for x in candidates:
        totalCorrect += x.numOfCorrect
    print("Epoch {0} performance".format(epoch + 1))
    print("Correct Answers: {0}/{1}".format(totalCorrect,totalQuestion))
    print("Percent: %.2f%% \n" % ((totalCorrect/totalQuestion)*100))
    epochPerformance1.append(((totalCorrect/totalQuestion)*100))

print("Best percent correct: %.2f%%" % (max(epochPerformance1)))
plt.title("Case A")
plt.plot(epochPerformance1)
plt.xlabel("Epoch")
plt.ylabel("Percent Correct")
plt.ylim(0,100)
plt.show()


for epoch in range(epochs):
    candidates = []
    HRCorrectAnswers = np.random.randint(1,6,size=questionCount)
    randomQuestion = np.random.randint(questionCount)
    for x in range(candidateCount):
        answers = []
        for y in range(questionCount):
            answers.append(np.random.randint(1,6))
        answers[randomQuestion] = HRCorrectAnswers[randomQuestion] 
        candidates.append(candidate(answers))

    for cand in candidates:
        for x in range(len(cand.answers)):
            if(cand.answers[x] == HRCorrectAnswers[x]):
                cand.numOfCorrect = cand.numOfCorrect + 1

    totalQuestion = questionCount*candidateCount
    totalCorrect = 0
    for x in candidates:
        totalCorrect += x.numOfCorrect
    print("Epoch {0} performance".format(epoch + 1))
    print("Correct Answers: {0}/{1}".format(totalCorrect,totalQuestion))
    print("Percent: %.2f%% \n" % ((totalCorrect/totalQuestion)*100))
    epochPerformance2.append(((totalCorrect/totalQuestion)*100))

print("Best percent correct:  %.2f%%" % (max(epochPerformance2)))
plt.title("Case B")
plt.plot(epochPerformance2)
plt.xlabel("Epoch")
plt.ylabel("Percent Correct")
plt.ylim(0,100)
plt.show()