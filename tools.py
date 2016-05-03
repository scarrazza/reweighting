#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path as osp

import tarfile
import pandas as pd

__author__ = 'Stefano Carrazza & Zahari Kassabov'
__license__ = 'GPL'
__version__ = '1.0.0'
__email__ = 'stefano.carrazza@cern.ch'



class Data:
    def __init__(self, datafile, invcovfile):

        print(' Opening data file: %s' % datafile)

        self.data = pd.read_table(maybe_untar(datafile), header=[0,1]).dropna(axis=1)

        print(' Opening data file: %s' % invcovfile)


        self.invcovmat = pd.read_table(maybe_untar(invcovfile), header=[0,1]).dropna(axis=1)

    def get_data(self):
        return self.data.ix[0].as_matrix()

    def get_invcovmat(self):
        return self.invcovmat.as_matrix()

tarext = ('.tgz', '.gz')

def maybe_untar(path):
    """Return the unmodified path if it doesn't look like a tar file, or the
    file handle from."""
    #path = getattr(path, 'path', path)
    if osp.splitext(path)[-1] in tarext:
        return tarfile.open(path).fileobj
    return path





class Predictions:

    def __init__(self, predfile):

        print(' Opening predictions file: %s' % predfile)
        self.pred = pd.read_table(maybe_untar(predfile), header=[0,1],
                                  ).dropna(axis=1)

    def get_predictions(self):
        return self.pred.as_matrix()