# -*- coding: utf-8 -*-
"""
    The MIT License (MIT)

    Copyright (c) 2023 pkjmesra

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

"""
from PKDevTools.classes.Singleton import SingletonType, SingletonMixin
from PKDevTools.classes.PKPickler import PKPicklerDB

class NSEStockMFIDB(SingletonMixin, metaclass=SingletonType):
    def __init__(self):
        super(NSEStockMFIDB, self).__init__()
        self.pickler = PKPicklerDB(fileName=f"{self.__class__.__name__}.pkl")

    def searchCache(self, ticker:str=None, name:str=None):
        return self.pickler.searchCache(ticker=ticker, name=name)
    
    def saveCache(self, ticker:str=None, name:str=None, stockDict:dict=None):
        self.pickler.saveCache(ticker=ticker, name=name, stockDict=stockDict)
