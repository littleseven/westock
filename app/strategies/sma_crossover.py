#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2015-2020 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)


import backtrader as bt
import backtrader.indicators as btind

import metaStrategy as mt

class sma_crossover(mt.MetaStrategy):
    '''This is a long-only strategy which operates on a moving average cross

    Note:
      - Although the default

    Buy Logic:
      - No position is open on the data

      - The ``fast`` moving averagecrosses over the ``slow`` strategy to the
        upside.

    Sell Logic:
      - A position exists on the data

      - The ``fast`` moving average crosses over the ``slow`` strategy to the
        downside

    Order Execution Type:
      - Market

    '''
    alias = ('SMA_CrossOver',)

    params = (
        # period for the fast Moving Average
        ('fast', 15),
        # period for the slow moving average
        ('slow', 30),
        # Trade size
        ('tradeSize', 2000)
    )

    def __init__(self, *argv):

        # used to modify parameters
        super().__init__(argv[0])

        sma_fast = btind.MovAv.SMA(period=self.p.fast)
        sma_slow = btind.MovAv.SMA(period=self.p.slow)

        self.buysig = btind.CrossOver(sma_fast, sma_slow)

    def next(self):
        if self.position.size:
            if self.buysig < 0:
                self.sell(size=self.p.tradeSize)

        elif self.buysig > 0:
            self.buy(size=self.p.tradeSize)
