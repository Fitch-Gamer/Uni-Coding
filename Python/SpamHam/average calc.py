import math
import numpy as np
class SpamClassifier:
        
    def train(self,TrainingData):
        self.Averages = np.zeros((2,54))
        for i in range(1,54):
            zeros = 0
            ones = 0
            tot = 0
            for j in TrainingData:
                if(j[0] == 1):
                    if(j[i] == 1):
                        ones+=1
                    else:
                        zeros +=1
                tot+=1
            self.Averages[0][i-1] = zeros/tot
            self.Averages[1][i-1] = ones/tot
        #print(self.Averages)
    
    
    def predict(self, new_data):
        limit = 0.70
        class_predictions= np.zeros(len(new_data))
        l = 0
        for j in new_data:
            tmp = 0
            for i in range (0,53):
                if(j[i] == 1):
                    tmp+=self.Averages[1][i]
                else:
                    tmp+= self.Averages[0][i]
            #print(tmp/54)
            if(tmp/54 > limit):
                class_predictions[l] = tmp/54#1
            else:
                class_predictions[l] = tmp/54#0
            
            l+=1
    
        return class_predictions
    

def create_classifier():
    classifier = SpamClassifier()
    return classifier

classifier = create_classifier()

training_spam = np.loadtxt(open("C:\\Users\\fitch\\Downloads\\spamclassifier\\data\\training_spam.csv"), delimiter=",").astype(int)
testing_spam = np.loadtxt(open("C:\\Users\\fitch\\Downloads\\spamclassifier\\data\\testing_spam.csv"), delimiter=",").astype(int)[:, 1:]
print("Shape of the spam training data set:", training_spam.shape)
print(training_spam)

print("")
print("")
print("")

classifier.train(training_spam)
split = [[],[]]

tmp = classifier.predict(testing_spam)

i = 0
for j in tmp:
    if (testing_spam[i][0] == 1):
        split[1].append(j)
    else:
        split[0].append(j)
    i+=1

print(split)