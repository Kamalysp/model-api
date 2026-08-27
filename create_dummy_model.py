from sklearn.linear_model import LogisticRegression
import numpy as np
import joblib

X_fake = np.random.rand(100, 3)
y_fake = np.random.randint(0, 2, 100)

dummy_model = LogisticRegression()
dummy_model.fit(X_fake, y_fake)

joblib.dump(dummy_model, "model/model.pkl")
print("Dummy model saved.")