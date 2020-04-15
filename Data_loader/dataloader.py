import os
import numpy as np
import torch
from torch.utils.data import Dataset
import nltk


class TextCorpus(Dataset):
    def __init__(self, path='./corpus/The_Tempest.txt'):
        # choose device where the data will reside
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

        # read the corpus
        with open(path,'r') as corpus:
            self.data = corpus.read()

        # tokenize the text
        self.word_token = nltk.word_tokenize(self.data)

        # generate the vocabulary
        self.vocab = set(self.word_token)
        self.num_vocab = len(self.vocab)

        # generate a mapping from words to indices in a dictionary (and vice-versa)
        self.word_to_ix = {word: i for i, word in enumerate(self.vocab)}
        self.ix_to_word = {str(i):word for i,word in enumerate(self.vocab)}


    def __getitem__(self, idx):
        x = torch.tensor([self.word_to_ix[self.word_token[idx]]],dtype=torch.long,device=self.device)
        y = torch.tensor([self.word_to_ix[self.word_token[idx+1]]],dtype=torch.long,device=self.device)
        return (x,y)

    def __len__(self):
        return len(self.word_token)-1