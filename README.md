# Stacked-LSTM Multivariate Regression Model
This model is make for muscle estimation.
The input are the joints' angle, and the output is the muscle activation value from our laboratory works below:<br/>
<a target="_blank" href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10185016">Saputra, Azhar Aulia, Chin Wei Hong, Tadamitsu Matsuda, and Naoyuki Kubota. "A Real-time Control System of Upper-limb Human Musculoskeletal Model with Environmental Integration." IEEE Access (2023)</a>.
<hr/>
We compare the Stacked-LSTM model with:
<ol>
<li><a href="https://colab.research.google.com/drive/1NrnU5kjxIGem1fEmbaRD31ItbRH515Wa">Sequence-to-Sequence Regression Model</a></li>
<li><a target="_blank" href="https://colab.research.google.com/drive/1wNYPuS9aUC5deLNgvvvObgfD4ED1JBFh">Random Forest Regression</a></li>
<li><a target="_blank" href="https://colab.research.google.com/drive/1wNYPuS9aUC5deLNgvvvObgfD4ED1JBFh">Linear Regression</a></li>
<li><a target="_blank" href="https://colab.research.google.com/drive/1HfGNMd37smy9g4QPqTD3vsrJs9poLXNw">Sequence-to-sequence with Bahdanau Attention Regression Model</a></li>
<li><a href="https://colab.research.google.com/drive/1h0pVUcLgSOdcnpr32YqNzQ7-cb4Niok3">Multi-layer Perceptron Regression Model</a></li>
<li><a href="https://colab.research.google.com/drive/1qV9uoniodTZwX_PtrFmgcyYsf9VBHbAm">Stacked Residual LSTM Regression Model</a></li>
<li><a href="https://colab.research.google.com/drive/1nUlUwV55an9qlwqERwScmBXNeHAxZxiv">Transformer Regression Model</a></li>
</ol>

<hr/>
Two sample data are provided in data directory:<br/>
train.pickle and test.pickle<br/>
One for training, one for testing.
<hr/>

## Citing Us
If you find this project useful in your research, please use the following BibTeX entry for citation.
```BibTeX
@inproceedings{siow2023muscle,
  title={Muscle Estimation using Stacked-LSTM Multivariate Regression Model},
  author={Siow, ChyanZheng and Wang, WeiHao and Chuquirachi, Franz and Saputra, Azhar Aulia and Obo, Takenori and Kubota, Naoyuki},
  booktitle={The 31th Symposium~on~Fuzzy, Artificial Intelligence, Neural Networks and Computational~Intelligence},
  year={2023}
}
```



