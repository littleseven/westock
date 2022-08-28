import backtrader as bt
from app.CerebroEnhanced import CerebroEnhanced


class Context:
    def __init__(self):
        self.strategyIndex = None
        self.strategyClass = None
        self.strat_results = None

        self.myOrders = []
        self.timeFrameIndex = {"M1": 0, "M5": 10, "M15": 20, "M30": 30, "H1": 40, "H4": 50, "D": 60, "W": 70}
        self.strategyParameters = {}
        self.dataframes = {}
        self.data = None
        self.cerebro = CerebroEnhanced()
        self.startingcash = 10000.0

    def addStrategy(self, strategyName):
        # For now, only one strategy is allowed at a time
        self.cerebro.clearStrategies()

        # Reset strategy parameters
        self.strategyParameters = {}
        # first strategyName is the file name, and second (fromlist) is the class name
        mod = __import__(strategyName, fromlist=[strategyName])
        self.strategyClass = getattr(mod, strategyName)  # class name in the file

        pass

    def run(self):
        # Reset cerebro internal variables
        self.resetCerebro()
        self.onPreExecute()
        results = self.onRun()
        self.onPostExecute(results)
        pass

    def onPreExecute(self):
        pass

    def onPostExecute(self, results):
        pass

    def onRun(self):
        # Add strategy here to get modified parameters
        params = self.strategyParameters
        self.strategyIndex = self.cerebro.addstrategy(self.strategyClass, params)

        # Wallet Management : reset between each run
        self.cerebro.broker.setcash(self.startingcash)
        # Compute strategy results
        results = self.cerebro.run()  # run it all
        return results
        pass

    def resetCerebro(self):
        # create a "Cerebro" engine instance
        self.cerebro = CerebroEnhanced()

        # Then add obersers and analyzers
        self.cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name="ta")
        '''
        self.cerebro.addanalyzer(bt.analyzers.PyFolio, _name='PyFolio')
        self.cerebro.addanalyzer(bt.analyzers.SharpeRatio)
        self.cerebro.addanalyzer(bt.analyzers.Transactions)
        self.cerebro.addanalyzer(bt.analyzers.Returns)
        self.cerebro.addanalyzer(bt.analyzers.Position)

        self.cerebro.addobserver(bt.observers.Broker)
        self.cerebro.addobserver(bt.observers.Trades)
        self.cerebro.addobserver(bt.observers.BuySell)
        self.cerebro.addanalyzer(bt.analyzers.Transactions, _name='Transactions')
        '''
        # Add an observer to watch the strat running and update the progress bar values
        from observers.stockObserver import StockObserver
        self.cerebro.addobserver(StockObserver)

        # Add data to cerebro
        if self.data is not None:
            self.cerebro.adddata(self.data)  # Add the data feed
        pass