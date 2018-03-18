# -*- coding: utf-8 -*-
"""
Simple example using BarGraphItem
"""

import pyqtgraph
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

class GraphPresentor():
    def __init__(self):
        self.is_running = False
        self.app = None
        self.pyqtgraph = pyqtgraph.plot()

        self.pyqtgraph.setWindowTitle('pyqtgraph example: BarGraphItem')
        self.pyqtgraph.resize(1300, 600)

        x = np.arange(10)
        y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.bar_graph = pyqtgraph.BarGraphItem(x0=range(10), x=x, height=y, width=2, brush='r')
        self.pyqtgraph.addItem(self.bar_graph)

    def update(self, data):
        if self.is_running is False:
            pass
        if (not hasattr(self, "bar_graph")) or \
                (not hasattr(self, "pyqtgraph")):
            return

        labels = [datum[0] for datum in data]

        counts = [datum[1][0] for datum in data]

        if len(counts) < 10:
            counts.extend([0 for _ in range(10 - len(counts))])

        if len(labels) < 10:
            labels.extend(["" for _ in range(10 - len(counts))])

        ticks = [list(zip(range(10), labels))]

        self.pyqtgraph.getAxis('bottom').setTicks(ticks)

        x = np.arange(10)
        y = np.array(counts)
        self.bar_graph.setOpts(x0=range(10), x=x, height=y, width=0.9, brush='r')

    def present(self):
        self.is_running = True
        self.app = QtGui.QApplication.instance()
        self.app.aboutToQuit.connect(self.stop)
        self.app.exec_()

    def stop(self):
        self.is_running = False
        self.app.quit()

