import spacy
import pandas as pd
import numpy as np
import zipfile,nltk
from nltk.corpus import PlaintextCorpusReader 
import string
from nltk.tokenize import word_tokenize
nltk.download('punkt')
import re
from nltk.corpus import stopwords
import heapq as hq
import sys
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

import pandas as pd
import csv
import os
import string
import re

from ast import literal_eval

from collections import Counter
import math


def initialProcess():
    from nltk.corpus import stopwords
    nltk.download('stopwords')
    stopwords = set(stopwords.words('english'))
    stopwords.add("places")
    stopwords.add("place")

    df=pd.read_csv("Project_data_mid_final.csv")
    print(df)
    return "val"
