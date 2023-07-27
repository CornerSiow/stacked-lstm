from sklearn.metrics import *
import pickle
from torch.utils.data import Dataset
import numpy as np

def showScore(y_true, y_pred):
  print("mean absolute error:","{:.5f}".format(mean_absolute_error(y_true, y_pred)))
  print("r2 score:","{:.5f}".format(r2_score(y_true, y_pred)))
  print("explained variance score:","{:.5f}".format(explained_variance_score(y_true, y_pred)))

class CustomDataset(Dataset):
    def __init__(self, pickle_file, window_size = 40, window_offset = 40):
        self.x = []
        self.y = []
        with open(pickle_file, 'rb') as handle:
            data = pickle.load(handle)
        start_i = 0
        end_i = len(data[0]) - window_size
        while start_i < end_i:
            self.x.append(data[0][start_i: start_i + window_size])
            self.y.append(data[1][start_i: start_i + window_size])
            start_i += window_offset
        self.x = np.asarray(self.x)
        self.y = np.asarray(self.y)
    def __len__(self):
        return len(self.x)
    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        return self.x[idx], self.y[idx]
