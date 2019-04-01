# Module for loading US state legislature data.
# Author: Eddie Lee, edlee@alumni.princeton.edu
import numpy as np
import pandas as pd
import os

DATADR = os.path.expanduser('~')+'/Dropbox/Research/py_lib/data_sets/us_state_legislature'

class California():
    """Class for loading Jeff Lewis' roll call voting data on California.
    """

    @classmethod
    def session(cls, year, house, binarize=False):
        """
        1, yea
        6, no
        9, not voting/not present
        0, not in chamber or on committee

        Parameters
        ----------
        year : int
        house : str
            'ass' for Assembly or 'sen' for Senate
        binarize : bool, False
            If True, 1 is yea, -1 is nay, and 0 is any other vote.

        Returns
        -------
        pd.DataFrame
        """

        fname = DATADR
        if 'sen' in house.lower():
            fname += '/ca%02d-%02dvotes_senate.csv'%(year,(year+1)%100)
        elif 'ass' in house.lower():
            fname += '/ca%02d-%02dvotes_assembly.csv'%(year,(year+1)%100)
        else:
            raise Exception("Unrecognized house type.")
        
        try:
            df = pd.read_csv(fname).iloc[:,1:]
        except FileNotFoundError:
            raise Exception("Invalid year.")

        df = df.transpose()
        names = df.iloc[0].values
        df = df.iloc[1:].astype(int)
        df.columns = names

        if binarize:
            df[df==6] = -1
            df[df==9] = 0
            assert set(np.unique(df))<=set((-1,0,1)), np.unique(df)
        return df
#end California
