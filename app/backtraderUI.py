import traceback

import backtrader as bt

import sys, os

from app.context import Context
from app.data import dataUtil
from app.utils.dateUtil import findTimeFrame

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/observers')
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/strategies')
# sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../finplot')

import pandas as pd

# local files
import userInterface as Ui

from wallet import Wallet

interface = None
wallet = None


class BacktraderUI(Context):

    def __init__(self):
        super(BacktraderUI, self).__init__()
        global interface
        interface = Ui.UserInterface(self)
        self.interface = interface

        global wallet
        wallet = Wallet(self.startingcash)
        self.wallet = wallet

        self.resetCerebro()
        self.interface.initialize()

    def onImportDataSuccess(self, df):
        timeframe = findTimeFrame(df)
        self.interface.createChartDock(timeframe)
        self.interface.drawChart(df, timeframe)
        self.interface.strategyTesterUI.runBacktestPB.setEnabled(True)
        pass

    def importData(self, fileNames, onSuccess):
        try:
            fileNames.sort(key=lambda x: self.timeFrameIndex[findTimeFrame(self.dataframes[x])])

            for fileName in fileNames:
                df = self.dataframes[fileName]
                self.data = bt.feeds.PandasData(dataname=df, timeframe=bt.TimeFrame.Minutes)
                self.cerebro.adddata(self.data)
                onSuccess(df)
            self.interface.strategyTesterUI.runBacktestPB.setEnabled(True)
            return True
        except:
            traceback.print_exc()
            return False
        pass


    def importData(self, fileNames):

        try:

            # Sort data by timeframe
            # For cerebro, we need to add lower timeframes first
            fileNames.sort(key=lambda x: self.timeFrameIndex[findTimeFrame(self.dataframes[x])])

            # Files should be loaded in the good order
            for fileName in fileNames:
                df = self.dataframes[fileName]

                # Datetime first column : 2012-12-28 17:45:00
                # self.dataframe['TimeInt'] = pd.to_datetime(self.dataframe.index).astype('int64') # use finplot's internal representation, which is ns

                # Pass it to the backtrader datafeed and add it to the cerebro
                self.data = bt.feeds.PandasData(dataname=df, timeframe=bt.TimeFrame.Minutes)

                # Add data to cerebro : only add data when all files have been selected for multi-timeframes
                self.cerebro.adddata(self.data)  # Add the data feed

                # Find timeframe
                timeframe = findTimeFrame(df)

                # Create the chart window for the good timeframe (if it does not already exists?)
                self.interface.createChartDock(timeframe)

                # Draw charts based on input data
                self.interface.drawChart(df, timeframe)

            # Enable run button
            self.interface.strategyTesterUI.runBacktestPB.setEnabled(True)

            return True

        except AttributeError as e:
            traceback.print_exc()
            print("AttributeError error:" + str(e))
        except KeyError as e:
            traceback.print_exc()
            print("KeyError error:" + str(e))
        except:
            traceback.print_exc()
            print("Unexpected error:" + str(sys.exc_info()[0]))
            return False
        pass

    def addStrategy(self, strategyName):
        super().addStrategy(strategyName)
        # Add strategy parameters
        self.interface.fillStrategyParameters(self.strategyClass)

        pass

    def strategyParametersChanged(self, lineEdit, parameterName, parameterOldValue):

        # todo something
        if len(lineEdit.text()) > 0:

            param = self.strategyClass.params._get(self.strategyClass.params, parameterName)

            if isinstance(param, int):
                self.strategyParameters[parameterName] = int(lineEdit.text())
            elif isinstance(param, float):
                self.strategyParameters[parameterName] = float(lineEdit.text())
            else:
                self.strategyParameters[parameterName] = lineEdit.text()

        pass

    def strategyParametersSave(self, parameterName, parameterValue):
        self.strategyParameters[parameterName] = parameterValue
        pass

    def onPreExecute(self):
        # UI label
        self.interface.strategyTesterUI.runLabel.setText("Running strategy...")
        self.interface.resetChart()
        self.wallet.reset(self.startingcash)
        pass

    def onPostExecute(self, results):
        # Display results
        self.strat_results = results[0]  # results of the first strategy
        self.displayStrategyResults()

        # UI label
        self.interface.strategyTesterUI.runLabel.setText("Strategy backtest completed.")
        pass

    def displayStrategyResults(self):
        self.interface.fillSummaryUI(self.strat_results.stats.broker.cash[0], self.strat_results.stats.broker.value[0],
                                     self.strat_results.analyzers.ta.get_analysis())
        self.interface.fillTradesUI(self.strat_results._trades.items())
        self.myOrders = []
        for order in self.strat_results._orders:
            if order.status in [order.Completed]:
                self.myOrders.append(order)
        self.interface.setOrders(self.myOrders)

        # Profit and Loss
        pnl_data = {}
        pnl_data['value'] = self.wallet.value_list
        pnl_data['equity'] = self.wallet.equity_list
        pnl_data['cash'] = self.wallet.cash_list

        # really uggly
        pnl_data['time'] = list(self.dataframes.values())[0].index

        # draw charts
        df = pd.DataFrame(pnl_data)
        self.interface.displayPnL(df)
        pass

    def displayUI(self):
        self.interface.show()
        pass

    def cashChanged(self, cashString):
        if len(cashString) > 0:
            self.startingcash = float(cashString)
            self.cerebro.broker.setcash(self.startingcash)
        pass


    def loadData(self, kwargs):
        code = kwargs["code"]
        dataframe = dataUtil.get_stock_data(kwargs)
        self.dataframes[code] = dataframe
        df = self.dataframes[code]
        self.data = bt.feeds.PandasData(dataname=df, timeframe=bt.TimeFrame.Minutes)
        self.cerebro.adddata(self.data)
        self.onImportDataSuccess(df)
        pass