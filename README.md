# Stacked-LSTM Multivariate Regression Model
This model is make for muscle estimation.
The input are the joints' angle, and the output is the muscle activation value from our laboratory works below:<br/>
<a target="_blank" href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10185016">Saputra, Azhar Aulia, Chin Wei Hong, Tadamitsu Matsuda, and Naoyuki Kubota. "A Real-time Control System of Upper-limb Human Musculoskeletal Model with Environmental Integration." IEEE Access (2023)</a>.
<hr/>
We compare the Stacked-LSTM model with:
<ol>
<li>Sequence-to-Sequence Regression Model</li>
<li><a target="_blank" href="https://colab.research.google.com/drive/1wNYPuS9aUC5deLNgvvvObgfD4ED1JBFh">Random Forest Regression</a></li>
<li><a target="_blank" href="https://colab.research.google.com/drive/1wNYPuS9aUC5deLNgvvvObgfD4ED1JBFh">Linear Regression</a></li>
<li>Sequence-to-sequence with Bahdanau Attention Regression Model</li>
<li>Multi-layer Perceptron Regression Model</li>
<li>Stacked Residual LSTM Regression Model</li>
<li>Transformer Regression Model</li>
</ol>

All these models can found in the models directory.
<hr/>
Two sample data are provided in data directory:<br/>
train.pickle and test.pickle<br/>
One for training, one for testing.
<hr/>
Please Feel free to cite our paper:





