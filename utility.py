from sklearn.metrics import *
def showScore(y_true, y_pred):
  print("mean absolute error:","{:.5f}".format(mean_absolute_error(y_true, y_pred)))
  print("r2 score:","{:.5f}".format(r2_score(y_true, y_pred)))
  print("explained variance score","{:.5f}".format(explained_variance_score(y_true, y_pred)))
