import time
import datetime
import pandas as pd

from app.data.database import db_interface
from app.utils.fileUtil import FileUtil


def get_stock_data(kwargs):
    baost_para = {"5分钟": "5", "60分钟": "60", "30分钟": "30", "日线": "d", "周线": "w",
                  "后复权": "1", "前复权": "2", "不复权": "3"}

    # 传递参数
    st_code = kwargs["code"]
    sdate_obj = kwargs["start_date"]
    edate_obj = kwargs["end_date"]

    # sdate_val = datetime.datetime(sdate_obj.year, sdate_obj.month + 1, sdate_obj.day)
    # edate_val = datetime.datetime(edate_obj.year, edate_obj.month + 1, edate_obj.day)
    sdate_val = sdate_obj
    edate_val = edate_obj
    sql_columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'change_rate']
    table_name = 'hsc_stocks_d'
    sql = '''
            SELECT `{}` FROM `{}` WHERE code = '{}' AND date BETWEEN '{}' AND '{}';
            '''.format('`,`'.join(sql_columns),
                       table_name,
                       st_code,
                       sdate_val,
                       edate_val)
    data = db_interface.read_data_from_sql(sql)

    data.rename(columns={'date': 'Date', 'open': 'Open', 'high': 'High', 'low': 'Low',
                         'close': 'Close', 'volume': 'Volume', 'change_rate': 'ChgPct'},
                inplace=True)
    data.reset_index()
    data.Date = pd.DatetimeIndex(data.Date)
    data.set_index("Date", drop=True, inplace=True)
    data.index.set_names('Date', inplace=True)
    return data

def get_stock_info(self, **kwargs):
    baost_para = {"5分钟": "5", "60分钟": "60", "30分钟": "30", "日线": "d", "周线": "w",
                  "后复权": "1", "前复权": "2", "不复权": "3"}

    # 传递参数
    st_code = kwargs["st_code"]
    sdate_obj = kwargs["sdate_obj"]
    edate_obj = kwargs["edate_obj"]
    period_val = baost_para[kwargs["st_period"]]
    auth_val = baost_para[kwargs["st_auth"]]

    sdate_val = datetime.datetime(sdate_obj.year, sdate_obj.month + 1, sdate_obj.day)
    edate_val = datetime.datetime(edate_obj.year, edate_obj.month + 1, edate_obj.day)
    sql_columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'change_rate']
    table_name = 'hsc_stocks_d'
    sql = '''
            SELECT `{}` FROM `{}` WHERE code = '{}' AND date BETWEEN '{}' AND '{}';
            '''.format('`,`'.join(sql_columns),
                       table_name,
                       st_code,
                       sdate_val,
                       edate_val)
    data = db_interface.read_data_from_sql(sql)

    data.rename(columns={'date': 'Date', 'open': 'Open', 'high': 'High', 'low': 'Low',
                         'close': 'Close', 'volume': 'Volume', 'change_rate': 'ChgPct'},
                inplace=True)
    data.reset_index()
    data.Date = pd.DatetimeIndex(data.Date)
    data.set_index("Date", drop=True, inplace=True)
    data.index.set_names('Date', inplace=True)
    return data


    def load_stock_pool(self):
        # 加载自选股票池
        self_pool = FileUtil.load_sys_settings("stock_self_pool.json")
        self.syslog.re_print("从Json文件获取自选股票池成功...\n")
        return self_pool