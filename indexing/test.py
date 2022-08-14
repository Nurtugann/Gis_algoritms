
import matplotlib.pyplot as plt
import pickle as pkl
figx = pkl.load(open('data-master/mydcel.pickle',  'rb'))
# Load figure from disk and display
figx.show()   # show the figure, edit it etc.!