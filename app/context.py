import backtrader as bt
from app.CerebroEnhanced import CerebroEnhanced


class Context:
    def __init__(self):
        self.timeFrameIndex = {"M1": 0, "M5": 10, "M15": 20, "M30": 30, "H1": 40, "H4": 50, "D": 60, "W": 70}
        self.strategyParameters = {}
        self.dataframes = {}
        self.data = None
        self.cerebro = CerebroEnhanced()
        self.startingcash = 10000.0

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
