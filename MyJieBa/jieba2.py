import jieba
import pandas as pd
from wordcloud import WordCloud
import numpy as np
from PIL import Image


font = r'C:\Windows\Fonts\FZSTK.TTF'
STOPWORDS = {"回复", }


def wordcloud(file, name, pic=None):
    df = pd.read_csv(file, usecols=[1])
    df_copy = df.copy()
    df_copy['comment'] = df_copy['comment'].apply(lambda x: str(x).split())  # 去掉空格
    df_list = df_copy.values.tolist()
    comment = jieba.cut(str(df_list), cut_all=False)
    words = ' '.join(comment)
    img = Image.open(pic)
    img_array = np.array(img)
    wc = WordCloud(width=2000, height=1800, background_color='white', font_path=font, mask=img_array,
                   stopwords=STOPWORDS, contour_width=3, contour_color='steelblue')
    wc.generate(words)
    wc.to_file(name + '.png')


if __name__ == '__main__':
    wordcloud("1572486436comment.csv", "lixiaolu2", 'xinsui.jpg')
