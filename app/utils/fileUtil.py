import os
import sys

import pandas as pd


def loadData(dataframes, dataPath, datetimeFormat, separator):

    # Try importing data file
    # We should code a widget that ask for options as : separators, date format, and so on...
    try:
        fileName = os.path.basename(dataPath)

        # Python contains
        if not dataPath in dataframes:
            dataframes[fileName] = pd.read_csv(dataPath,
                                               sep=separator,
                                               parse_dates=[0],
                                               date_parser=lambda x: pd.to_datetime(x, format=datetimeFormat),
                                               skiprows=0,
                                               header=0,
                                               names=["Time", "Open", "High", "Low", "Close", "Volume"],
                                               index_col=0)

    except ValueError as err:
        return False, "ValueError error:" + str(err)
    except AttributeError as err:
        return False, "AttributeError error:" + str(err)
    except IndexError as err:
        return False, "IndexError error:" + str(err)
    except:
        return False, "Unexpected error:" + str(sys.exc_info()[0])

    return True, ""