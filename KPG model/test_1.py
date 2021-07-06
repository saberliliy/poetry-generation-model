#! /usr/bin/env python
#-*- coding:utf-8 -*-
import codecs
import os
import random
from functools import reduce
import numpy as np
import  jieba
from cnt_words import get_pop_quatrains
from rank_words import get_word_ranks
from segment import Segmenter
from utils import DATA_PROCESSED_DIR, embed_w2v, apply_one_hot, apply_sparse, pad_to, SEP_TOKEN, PAD_TOKEN
from vocab import ch2int, VOCAB_SIZE, sentence_to_ints,ch_to_int
from word2vec import get_word_embedding
import jieba.posseg as peg

for word, flag in peg.cut("疏影正清夜"):
    print(word+flag)