import json
import os
import sys

import pandas as pd

from app import constants


class FileUtil:
    rel_path = constants.CONFIG_PATH

    @staticmethod
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

    @staticmethod
    def load_sys_settings(filename):
        with open(FileUtil.rel_path + filename, 'r', encoding='utf-8') as load_f:
            para_dict = json.load(load_f)
        return para_dict

    @staticmethod
    def save_sys_settings(filename, para_dict):
        with open(FileUtil.rel_path + filename, "w", encoding='utf-8') as save_f:
            json.dump(para_dict, save_f, ensure_ascii=False, indent=4)
