#05. n-gram
#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gra

import ngram

text = u'あいうえお'
index = ngram.NGram(N=2)
for term in index.ngrams(index.pad(text)):
    print term
