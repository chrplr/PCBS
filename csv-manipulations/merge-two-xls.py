#! /usr/bin/env python
# Time-stamp: <2019-08-30 14:37:32 christophe@pallier.org>

import sys
import pandas as pd

if __name__ == '__main__':
    DB1_NAME = sys.argv[1]
    DB2_NAME = sys.argv[2]

    db1 = pd.read_csv(DB1_NAME)
    db2 = pd.read_csv(DB2_NAME)

    # Left outer join: To include all the rows of your data frame x and only those from y that match
    db3 = pd.merge(db1, db2, how='left') 
    print(db3)






