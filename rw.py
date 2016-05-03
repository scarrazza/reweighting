#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" A PDF reweighting tool """

__author__ = 'Stefano Carrazza & Zahari Kassabov'
__license__ = 'GPL'
__version__ = '1.0.0'
__email__ = 'stefano.carrazza@cern.ch'

from tools import Data, Predictions

def main():

    # load data, invcovmat and predictions
    dt = Data('data/data.csv.tgz', 'data/invcovmat.csv.tgz')
    th = Predictions('data/predictions.csv.tgz')

    # retreive cv and invcovmat as numpy arrays
    cv    = dt.get_data()
    sigma = dt.get_invcovmat()
    predictions     = th.get_predictions()

    """The chi² function is

    v = (w@P) - cv
    chi² = v@sigma@v

    Therefore we need to minimize 1/2*w@A@W + B@w as a function of w
    """

    P = predictions@sigma@predictions.T/2
    q = cv@sigma@predictions.T

    #For interactive testing
    return P, q




def splash():
    print("\n 8888888b.  888       888 ")
    print(" 888   Y88b 888   o   888 ")
    print(" 888    888 888  d8b  888 ")
    print(" 888   d88P 888 d888b 888 ")
    print(" 8888888P\"  888d88888b888 ")
    print(" 888 T88b   88888P Y88888 ")
    print(" 888  T88b  8888P   Y8888 ")
    print(" 888   T88b 888P     Y888 ")
    print("\n  __v%s__" % __version__)
    print(" Authors: S.Carrazza & Z.Kassabov\n")

if __name__ == "__main__":
    splash()
    P,q = main()
