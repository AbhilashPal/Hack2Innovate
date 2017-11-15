# Hack2Innovate
Python Code for SMS Classification.

This is the code we wrote for the Chennai edition of Hack2Innovate's SMS classification Challenge from Samsung.
Link(https://t-hub.co/hack2innovate/)

# Main Problem

The main objective was to train a model on the TRAIN_SMS.csv file on 30,000 SMSes as either spam, information or informal(ham). Then we had to use it to successfully classify 7500 messages in DEV_SMS.csv . We used a bag of words model created using Scikit-Learn to create sparse matrices from the total 37500 examples. Then training was done on the 30,000 examples and after that we used the model to classify the given 7500 SMSes and write the results to the file TEST_RESULT.csv.
The Models used were DecisionTree and MLPClassifier(we tried an SVM but the model gave around 81% accuracy compared to 98 and 99% on the Tree and MLPC.). We trained several models on the MLPC varying alpha and took the best model.

Dependencies:
- Scikit-Learn
- CSV

# Bonus Problem

The bonus problem was to further subdivide the info type messages into several different classes as given. We tried several models but could not deliver a feasible solution within the stipulated time.

.
.
.
.
.
.
(I am a beginner/Noob at ML, please don't judge me. :3 )
