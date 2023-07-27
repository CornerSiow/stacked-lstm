from sklearn.metrics import *
def showScore(y_true, y_pred):
  print("mean_absolute_error",mean_absolute_error(y_true, y_pred))
  print("r2_score",r2_score(y_true, y_pred))
  print("explained_variance_score",explained_variance_score(y_true, y_pred))
