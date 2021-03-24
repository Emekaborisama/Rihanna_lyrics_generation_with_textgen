
from text_gen import ten_textgen as ttg

#load train data
data = './data/data.txt'
dataset = ttg.loaddata(data)

def prediction(text):
    lyric = ttg.load_model_predict(corpus = dataset, padding_method = 'pre', modelname = './model/model2textgen.h5', sample_text = text, word_length = 100)
    return lyric


