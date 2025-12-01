'''from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
import numpy as n
import pandas as p
import pickle as pi

data=p.read_csv("data set/Phishing_Email.csv")
X = data['Email Text'].astype(str)
y=data['Email Type'].astype(str)



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


pipe=Pipeline([("tfidf", TfidfVectorizer(stop_words="english", max_features=5000)),("clf", RandomForestClassifier(random_state=42)),])

pipe.fit(X_train,y_train)

y_pred=pipe.predict(X_test)

print("Training Modle......")
print("\nAccuracy:", accuracy_score(y_test, y_pred))'''

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
import numpy as n
import pandas as p
import pickle as pi

data=p.read_csv("data set/Phishing_Email.csv")
X = data['Email Text'].astype(str)
y=data['Email Type'].astype(str)



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


pipe=Pipeline([("tfidf", TfidfVectorizer(stop_words="english", max_features=5000)),("clf", LogisticRegression()),])

pipe.fit(X_train,y_train)

y_pred=pipe.predict(X_test)

with open('phishing detector.pkl','wb') as f:
    pi.dump(pipe, f)