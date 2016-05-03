#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Stefano Carrazza & Zahari Kassabov'
__license__ = 'GPL'
__version__ = '1.0.0'
__email__ = 'stefano.carrazza@cern.ch'

import pandas as pd

class Data:
    def __init__(self, datafile, invcovfile):

        print(' Opening data file: %s' % datafile)
        self.data = pd.read_table(datafile, header=[0,1]).dropna(axis=1)

        print(' Opening data file: %s' % invcovfile)
        self.invcovmat = pd.read_table(invcovfile, header=[0,1]).dropna(axis=1)

    def get_data(self):
        return self.data.ix[0].as_matrix()

    def get_invcovmat(self):
        return self.invcovmat.as_matrix()


class Predictions:

    def __init__(self, predfile):

        print(' Opening predictions file: %s' % predfile)
        self.pred = pd.read_table(predfile, header=[0,1]).dropna(axis=1)

    def get_predictions(self):
        return self.pred.as_matrix()