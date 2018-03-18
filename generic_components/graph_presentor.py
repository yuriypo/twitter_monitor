# -*- coding: utf-8 -*-


import pyqtgraph
from pyqtgraph.Qt import QtGui
import numpy as np

class GraphPresentor():
    """
    Component's responsibility is visualization of top n items, as a Bar chart.
    """

    DEFAULT_NUMBER_OF_TOP_ITEMS_TO_WORK_WITH = 10
    DEFAULT_X_AXIS_SIZE = 1300
    DEFAULT_Y_AXIS_SIZE = 600

    def __init__(self):
        self.is_running = False
        self.app = None
        self.pyqtgraph = pyqtgraph.plot()

        self.pyqtgraph.setWindowTitle('pyqtgraph example: BarGraphItem')
        self.pyqtgraph.resize(GraphPresentor.DEFAULT_X_AXIS_SIZE, \
                              GraphPresentor.DEFAULT_Y_AXIS_SIZE)

        x = np.arange(GraphPresentor.DEFAULT_NUMBER_OF_TOP_ITEMS_TO_WORK_WITH)
        y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.bar_graph = pyqtgraph.BarGraphItem(x0=range(GraphPresentor.\
                                                         DEFAULT_NUMBER_OF_TOP_ITEMS_TO_WORK_WITH),
                                                x=x, height=y, width=2, brush='r')
        self.pyqtgraph.addItem(self.bar_graph)

    def update(self, data):
        if (not hasattr(self, "bar_graph")) or \
                (not hasattr(self, "pyqtgraph")):
            return

        labels = [datum[0] for datum in data]

        counts = [datum[1][0] for datum in data]

        if len(counts) < GraphPresentor.DEFAULT_NUMBER_OF_TOP_ITEMS_TO_WORK_WITH:
            counts.extend([0 for _ in range(GraphPresentor.DEFAULT_NUMBER_OF_TOP_ITEMS_TO_WORK_WITH
                                            - len(counts))])

        if len(labels) < GraphPresentor.DEFAULT_NUMBER_OF_TOP_ITEMS_TO_WORK_WITH:
            labels.extend(["" for _ in range(GraphPresentor.DEFAULT_NUMBER_OF_TOP_ITEMS_TO_WORK_WITH
                                             - len(counts))])

        ticks = [list(zip(range(GraphPresentor.DEFAULT_NUMBER_OF_TOP_ITEMS_TO_WORK_WITH), labels))]

        self.pyqtgraph.getAxis('bottom').setTicks(ticks)

        x = np.arange(GraphPresentor.DEFAULT_NUMBER_OF_TOP_ITEMS_TO_WORK_WITH)
        y = np.array(counts)
        self.bar_graph.setOpts(x0=range(GraphPresentor.\
                                        DEFAULT_NUMBER_OF_TOP_ITEMS_TO_WORK_WITH),
                               x=x,
                               height=y,
                               width=0.9,
                               brush='r')

    def present(self):
        self.app = QtGui.QApplication.instance()
        self.app.aboutToQuit.connect(self.stop)
        self.app.exec_()

    def stop(self):
        self.app.quit()
