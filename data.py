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
    def session(cls, year, house):
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

        Returns
        -------
        pd.DataFrame
        """

        fname = DATADR
        if 'sen' in house.lower():
            fname += '/ca%d-%dvotes_senate.csv'%(year,year+1)
        elif 'ass' in house.lower():
            fname += '/ca%d-%dvotes_house.csv'%(year,year+1)
        else:
            raise Exception("Unrecognized house type.")
        
        try:
            df = pd.read_csv(fname).iloc[:,1:]
        except FileNotFoundError:
            raise Exception("Invalid year.")

        df = df.transpose()
        return df

