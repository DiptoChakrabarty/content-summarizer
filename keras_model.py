import pandas as pd 
from sklearn.model_selection import train_test_split
from keras_text_summarization.library.utility.plot_utils import plot_and_save_history
from keras_text_summarization.library.seq2seq import Seq2SeqSummarizer
from keras_text_summarization.library.applications.fake_news_loader import fit_text
import numpy as np

data=pd.read_csv("/home/chuck/Downloads/fake_or_real_news.csv")

data.head()