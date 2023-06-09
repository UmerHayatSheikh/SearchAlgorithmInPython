import copy

import networkx as nx
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
import sys
from BFS import *
from DFS import *
from UCS import *
from DLS import *
from IDS import *
from BestFS import *
from Astar import *
from BiDirectional import *
from SimulatedAnnealing import *
from AlphaBetaPruning import *
import scipy as sp

graph = {}
weights = {}
heuristic = {}

graphUnDir = {}
weightsUnDir = {}

# heuristic = {
#     '1': 2,
#     '2': 3,
#     '3': 1,
#     '4': 4,
#     '5': 0,
#     '6': 3,
#     '7': 2,
#     '8': 1,
#     '9': 4,
#     '10': 0
# }

# graphUnDir = {
#     '1': ['2', '3', '5'],
#     '2': ['1', '4', '6'],
#     '3': ['1', '7', '8'],
#     '4': ['2', '9', '10'],
#     '5': ['1', '6', '10'],
#     '6': ['2', '5', '7'],
#     '7': ['3', '6', '8'],
#     '8': ['3', '7', '9'],
#     '9': ['4', '8', '10'],
#     '10': ['4', '5', '9'],
# }
#
# weightsUnDir = {
#     ('1', '2'): 9,
#     ('1', '3'): 10,
#     ('1', '5'): 11,
#     ('2', '1'): 9,
#     ('2', '4'): 12,
#     ('2', '6'): 13,
#     ('3', '1'): 10,
#     ('3', '7'): 14,
#     ('3', '8'): 15,
#     ('4', '2'): 12,
#     ('4', '9'): 16,
#     ('4', '10'): 17,
#     ('5', '1'): 11,
#     ('5', '6'): 18,
#     ('5', '10'): 19,
#     ('6', '2'): 13,
#     ('6', '5'): 18,
#     ('6', '7'): 20,
#     ('7', '3'): 14,
#     ('7', '6'): 20,
#     ('7', '8'): 21,
#     ('8', '3'): 15,
#     ('8', '7'): 21,
#     ('8', '9'): 22,
#     ('9', '4'): 16,
#     ('9', '8'): 22,
#     ('9', '10'): 23,
#     ('10', '4'): 17,
#     ('10', '5'): 19,
#     ('10', '9'): 23,
# }

# heuristic = {
# '1': 4,
# '2': 3,
# '3': 2,
# '4': 1,
# '5': 0
# }
#
# graphUnDir = {
# '1': ['2', '3', '5'],
# '2': ['1', '3'],
# '3': ['1', '2', '4'],
# '4': ['3', '5'],
# '5': ['1', '4']
# }
#
# weightsUnDir = {
# ('1', '2'): 2,
# ('2', '1'): 2,
# ('1', '3'): 3,
# ('3', '1'): 3,
# ('1', '5'): 1,
# ('5', '1'): 1,
# ('2', '3'): 1,
# ('3', '2'): 1,
# ('3', '4'): 2,
# ('4', '3'): 2,
# ('4', '5'): 3,
# ('5', '4'): 3
# }
# graph = {
#     'a': ['c'],
#     'b': ['d'],
#     'c': ['e'],
#     'd': ['a', 'b'],
#     'e': ['b', 'c'],
# }
#
# weights = {
#     ('a', 'c'): 1,
#     ('b', 'd'): 1,
#     ('c', 'e'): 1,
#     ('d', 'a'): 1,
#     ('d', 'b'): 1,
#     ('e', 'b'): 1,
#     ('e', 'c'): 1,
# }
#
# graphUnDir = {
#     '1': ['2', '3'],
#     '2': ['4', '5', '1'],
#     '3': ['6', '7', '1'],
#     '4': ['2', '7'],
#     '5': ['2'],
#     '6': ['3'],
#     '7': ['3', '4'],
# }
#
# weightsUnDir = {
#     ('1', '2'): 1,
#     ('1', '3'): 1,
#     ('2', '4'): 7,
#     ('2', '5'): 1,
#     ('6', '3'): 1,
#     ('7', '3'): 1,
#     ('7', '4'): 1,
#
#     ('2', '1'): 1,
#     ('3', '1'): 1,
#     ('4', '2'): 7,
#     ('5', '2'): 1,
#     ('3', '6'): 1,
#     ('3', '7'): 1,
#     ('4', '7'): 1,
# }
#
# heuristicUndir = {
#     '1': 1,
#     '2': 2,
#     '3': 2,
#     '4': 4,
#     '5': 0,
#     '6': 1,
#     '7': 3
# }
#
# heuristic = {
#     'a': 1,
#     'b': 2,
#     'c': 2,
#     'd': 4,
#     'e': 0,
# }

#
# graphUnDir = {
#     '1': ['2', '3', '5'],
#     '2': ['1', '4', '6'],
#     '3': ['1', '7', '8'],
#     '4': ['2', '9', '10'],
#     '5': ['1', '6', '10'],
#     '6': ['2', '5', '7'],
#     '7': ['3', '6', '8'],
#     '8': ['3', '7', '9'],
#     '9': ['4', '8', '10'],
#     '10': ['4', '5', '9'],
# }
#
# weightsUnDir = {
#     ('1', '2'): 9,
#     ('1', '3'): 10,
#     ('1', '5'): 11,
#     ('2', '1'): 9,
#     ('2', '4'): 12,
#     ('2', '6'): 13,
#     ('3', '1'): 10,
#     ('3', '7'): 14,
#     ('3', '8'): 15,
#     ('4', '2'): 12,
#     ('4', '9'): 16,
#     ('4', '10'): 17,
#     ('5', '1'): 11,
#     ('5', '6'): 18,
#     ('5', '10'): 19,
#     ('6', '2'): 13,
#     ('6', '5'): 18,
#     ('6', '7'): 20,
#     ('7', '3'): 14,
#     ('7', '6'): 20,
#     ('7', '8'): 21,
#     ('8', '3'): 15,
#     ('8', '7'): 21,
#     ('8', '9'): 22,
#     ('9', '4'): 16,
#     ('9', '8'): 22,
#     ('9', '10'): 23,
#     ('10', '4'): 17,
#     ('10', '5'): 19,
#     ('10', '9'): 23,
# }
# heuristic = {
#     '1': 0,
#     '2': 1,
#     '3': 2,
#     '4': 3,
#     '5': 4,
#     '6': 5,
#     '7': 6,
#     '8': 7,
#     '9': 8,
#     '10': 9,
# }


class AILabProject:
    def showerror(self, error):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(error)
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def load_gui(self, window):
        # to add nodes
        height = 20

        node1_label = QLabel('Node1:', window)
        node1_label.move(20, height)
        self.node1_input = QLineEdit(window)
        self.node1_input.move(130, height)

        node2_label = QLabel('Node2:', window)
        node2_label.move(240, height)
        self.node2_input = QLineEdit(window)
        self.node2_input.move(350, height)

        weight_label = QLabel('Edge Weight:', window)
        weight_label.move(460, height)
        self.weight_input = QLineEdit(window)
        self.weight_input.move(580, height)

        add_button = QPushButton('Add Nodes', window)
        add_button.move(750, height)
        add_button.clicked.connect(self.add_nodes)

        height = 100
        # to add heuristic
        node1_label = QLabel('Node:', window)
        node1_label.move(20, height)
        self.node = QLineEdit(window)
        self.node.move(130, height)

        node2_label = QLabel('Node Heuristic:', window)
        node2_label.move(240, height)
        self.nodeHeuristic = QLineEdit(window)
        self.nodeHeuristic.move(350, height)

        add_button = QPushButton('Add Node Heuristic', window)
        button_size = add_button.sizeHint()
        add_button.resize(button_size)
        add_button.move(750, height)
        add_button.clicked.connect(self.add_node_heuristic)

        height = 180
        # apply algo
        node1_label = QLabel('Start Node:', window)
        node1_label.move(20, height)
        self.start = QLineEdit(window)
        self.start.move(130, height)

        node2_label = QLabel('Goal Node:', window)
        node2_label.move(240, height)
        self.goal = QLineEdit(window)
        self.goal.move(350, height)

        node2_label = QLabel('Depth Limit:', window)
        node2_label.move(460, height)
        self.depth_limit = QLineEdit(window)
        self.depth_limit.move(580, height)

        add_button = QPushButton('Submit', window)
        button_size = add_button.sizeHint()
        add_button.resize(button_size)
        add_button.move(750, height)
        add_button.clicked.connect(self.apply_algorithm)

        height = 260
        # Algo DropDown
        self.algorithms = QComboBox(window)
        self.algorithms.addItems(['BFS', 'UCS', 'DFS', 'DLS', 'IDS', 'BDS', 'BestFS', 'A*', 'SA', "ABPruning"])
        self.algorithms.setGeometry(20, height, 100, 30)

        # Graph Type DropDown
        self.graphtype = QComboBox(window)
        self.graphtype.addItems(['Undirected Graph', 'Directed Graph'])
        self.graphtype.setGeometry(350, height, 200, 30)

        add_button = QPushButton('Show Graph', window)
        button_size = add_button.sizeHint()
        add_button.resize(button_size)
        add_button.move(750, height)
        add_button.clicked.connect(self.drawGraph)

    def drawPath(self, path, graph_type):
        edgeList = []
        heuristicDict = {}

        for i in range(0, len(path) - 1):
            edgeList.append((path[i], path[i + 1]))

        pathWeights = {}
        graphType = graph_type
        pos = self.drawGraph(path=True)
        if graphType == "Directed Graph":

            for i in edgeList:
                pathWeights[i] = weights[i]

            temp_node_list = []
            for i in path:
                tempStr = ""
                tempStr = f"{i}\nh={heuristic[i]}"
                temp_node_list.append(tempStr)

            temp_weight_dict = {}
            for i in pathWeights.keys():
                temp_tuple = (f"{i[0]}\nh={heuristic[i[0]]}", f"{i[1]}\nh={heuristic[i[1]]}")
                temp_weight_dict[temp_tuple] = pathWeights[i]


            weightList = temp_weight_dict.keys()
            nodeList = temp_node_list
            G = nx.DiGraph()
            G.add_nodes_from(nodeList)
            G.add_edges_from(weightList)

            # pos1 = nx.spring_layout(G)
            pos1 = {}
            pos_attrs = {}
            for node, coords in pos.items():
                if node in nodeList:
                    pos1[node]=coords

            nx.draw(G, pos1, with_labels=True, node_color="red", node_size=2000, font_color="black", font_size=20,
                    font_family="Times New Roman", font_weight="bold", width=5, edge_color="red")
            nx.draw_networkx_edge_labels(G, pos1, font_size=26, edge_labels=temp_weight_dict, font_color='black')

        else:

            for i in edgeList:
                pathWeights[i] = weightsUnDir[i]

            temp_node_list = []
            for i in path:
                tempStr = ""
                tempStr = f"{i}\nh={heuristic[i]}"
                temp_node_list.append(tempStr)

            temp_weight_dict = {}
            for i in pathWeights.keys():
                temp_tuple = (f"{i[0]}\nh={heuristic[i[0]]}", f"{i[1]}\nh={heuristic[i[1]]}")
                temp_weight_dict[temp_tuple] = pathWeights[i]

            weightList = temp_weight_dict.keys()
            nodeList = temp_node_list
            G = nx.Graph()
            G.add_nodes_from(nodeList)
            G.add_edges_from(weightList)
            # pos = nx.spring_layout(G)

            pos1 = {}
            pos_attrs = {}
            for node, coords in pos.items():
                if node in nodeList:
                    pos1[node]=coords

            nx.draw(G, pos1, with_labels=True, node_color="red", node_size=2000, font_color="black", font_size=20,
                    font_family="Times New Roman", font_weight="bold", width=5, edge_color="red")
            nx.draw_networkx_edge_labels(G, pos1, font_size=26, edge_labels=temp_weight_dict, font_color='black')

        plt.margins(0.2)
        plt.show()

    def apply_algorithm(self):

        algo = self.algorithms.currentText()
        start = self.start.text()
        goal = self.goal.text()

        if start == '':
            self.showerror("Enter a starting node")
            return

        if goal == '':
            self.showerror("Enter a goal node")
            return

        if goal == start:
            self.showerror("Start node and goal node can't be equal")
            self.start.clear()
            self.goal.clear()
            return

        if self.depth_limit.text() == "" and (algo == 'DLS'):
            self.showerror("Enter depth limit for DLS")
            return

        limit = 0

        if self.depth_limit.text() != "":
            limit = int(self.depth_limit.text())

        graphType = self.graphtype.currentText()

        if graphType == "Directed Graph" and algo == "BDS":
            self.showerror("Bidirectional Algorithm doesn't work on directed graph properly")
            return
        # nodesList = graph.keys()

        if graphType == "Directed Graph":
            if start not in graph or goal not in graph:
                self.showerror("select valid nodes")
                return
        else:
            if start not in graphUnDir or goal not in graphUnDir:
                self.showerror("select valid nodes")
                return

        self.start.clear()
        self.goal.clear()
        output = (0, "No output")
        if graphType == 'Undirected Graph':
            if algo == 'BFS':
                output = BFS(start, goal, graphUnDir)
                print(output)
            elif algo == 'DFS':
                output = DFS(start, goal, graphUnDir)
            elif algo == 'UCS':
                output = UCS(graphUnDir, weightsUnDir, start, goal)
            elif algo == 'BestFS':
                output = BestFS(graphUnDir, heuristic, start, goal)
            elif algo == 'DLS':
                output = DLS(graphUnDir, limit, start, goal)
            elif algo == 'IDS':
                output = IDS(graphUnDir, start, goal)
            elif algo == 'A*':
                output = Astar(graphUnDir, weightsUnDir, heuristic, start, goal)
            elif algo == 'BDS':
                output = biDirectionalSearch(graphUnDir, start, goal)
            elif algo == 'SA':
                output = simulated_annealing(start, goal, graphUnDir, weightsUnDir)
            elif algo == 'ABPruning':
                output = alphaBetaPruning(start, goal, graphUnDir, weightsUnDir)


        else:
            if algo == 'BFS':
                output = BFS(start, goal, graph)
            elif algo == 'DFS':
                output = DFS(start, goal, graph)
            elif algo == 'UCS':
                output = UCS(graph, weights, start, goal)
            elif algo == 'BestFS':
                output = BestFS(graph, heuristic, start, goal)
            elif algo == 'DLS':
                output = DLS(graph, limit, start, goal)
            elif algo == 'IDS':
                output = IDS(graph, start, goal)
            elif algo == 'A*':
                output = Astar(graph, weights, heuristic, start, goal)
            elif algo == 'BDS':
                output = biDirectionalSearch(graph, start, goal)
            elif algo == 'SA':
                output = simulated_annealing(start, goal, graph, weights)
            elif algo == 'ABPruning':
                output = alphaBetaPruning(start, goal, graph, weights)

        if output[0] == 0:
            self.showerror(output[1])
        else:
            self.drawPath(output[1], graphType)

    def add_nodes(self):
        node1 = self.node1_input.text()
        node2 = self.node2_input.text()
        weight = self.weight_input.text()

        if node1 == '' or node2 == '':
            self.showerror("Enter value for both nodes")
            return
        if weight == '':
            self.showerror("Enter weight for the nodes")
            return

        if node1 == node2:
            self.showerror("Value of Node1 and Node2 cannot be same")
            self.node1_input.clear()
            self.node2_input.clear()
            return

        graphType = self.graphtype.currentText()
        self.node1_input.clear()
        self.node2_input.clear()
        self.weight_input.clear()

        print(graphType)

        if node1 not in graphUnDir:
            graph[node1] = []
            graphUnDir[node1] = []

        if node2 not in graphUnDir:
            graph[node2] = []
            graphUnDir[node2] = []

        if node2 not in graph[node1]:
            graph[node1].append(node2)
            graphUnDir[node1].append(node2)

        # if node1 not in graphUnDir[node2]:
        #     graphUnDir[node2].append(node1)

        # if graphType == "Undirected Graph":

        if node1 not in graphUnDir[node2]:
            graphUnDir[node2].append(node1)

        weightsUnDir[(node2, node1)] = int(weight)
        weightsUnDir[(node1, node2)] = int(weight)

        weights[(node1, node2)] = int(weight)

        print(graphUnDir)
        print(weightsUnDir)
        print(f"Node1: {node1}, Node2: {node2}, Weight: {weight}")

    def add_node_heuristic(self):
        node = self.node.text()
        nodeHeuristic = self.nodeHeuristic.text()

        if node=='':
            self.showerror("Enter the node whose heuristic you're entering")
            return
        if nodeHeuristic =='':
            self.showerror("Enter heuristic of the node")
            return
        if node not in graph:
            self.showerror("The node you entered doesn't exist in the graph")
            self.node.clear()
            self.nodeHeuristic.clear()
            return


        self.node.clear()
        self.nodeHeuristic.clear()

        if node in graph and nodeHeuristic != '':
            heuristic[node] = int(nodeHeuristic)
            print(heuristic)

    def drawGraph(self, path=False):
        graphType = self.graphtype.currentText()

        if graphType == "Directed Graph":
            if len(graph.keys()) == 0:
                self.showerror("Enter nodes")
                return

            if len(weights.keys()) == 0:
                self.showerror("Weights not entered")
                return

            if len(heuristic.keys()) == 0:
                self.showerror("Heuristic of nodes in the graph are not entered")
                return

            if len(heuristic.keys()) != len(graph.keys()):
                self.showerror("Heuristic of all nodes is not entered")
                return

            temp_node_list = []
            for i in graph.keys():
                tempStr = ""
                tempStr = f"{i}\nh={heuristic[i]}"
                temp_node_list.append(tempStr)

            temp_weight_dict = {}
            for i in weights.keys():
                temp_tuple = (f"{i[0]}\nh={heuristic[i[0]]}", f"{i[1]}\nh={heuristic[i[1]]}")
                temp_weight_dict[temp_tuple] = weights[i]

            nodesList = copy.deepcopy(temp_node_list)
            weightList = copy.deepcopy(temp_weight_dict)
            G = nx.DiGraph()
            G.add_nodes_from(nodesList)
            G.add_edges_from(weightList)
            #pos = nx.spring_layout(G)
            pos = nx.kamada_kawai_layout(G)

            pos_attrs = {}
            for node, coords in pos.items():
                pos_attrs[node] = (coords[0], coords[1] + abs(coords[1])/3*1.2)

            nx.draw(G, pos, with_labels=True, node_color="blue", node_size=2000, font_color="white", font_size=20,
                    font_family="Times New Roman", font_weight="bold", width=5, edge_color="black")
            nx.draw_networkx_edge_labels(G, pos, font_size=26, edge_labels=temp_weight_dict, font_color='black')

            # nx.draw_networkx_labels(G, pos_attrs, labels=heuristic, font_size=12, font_color='k',
            #                         font_family='sans-serif', font_weight='normal', alpha=None, bbox=None,
            #                         horizontalalignment='center', verticalalignment='center', ax=None, clip_on=True)

        else:
            if len(graphUnDir.keys()) == 0:
                self.showerror("Enter nodes")
                return

            if len(weightsUnDir.keys()) == 0:
                self.showerror("Weights not entered")
                return

            if len(heuristic.keys()) == 0:
                self.showerror("Heuristic of nodes in the graph are not entered")
                return

            if len(heuristic.keys()) != len(graphUnDir.keys()):
                self.showerror("Heuristic of all nodes is not entered")
                return

            temp_node_list = []
            for i in graphUnDir.keys():
                tempStr = ""
                tempStr = f"{i}\nh={heuristic[i]}"
                temp_node_list.append(tempStr)

            temp_weight_dict = {}
            for i in weightsUnDir.keys():
                temp_tuple = (f"{i[0]}\nh={heuristic[i[0]]}", f"{i[1]}\nh={heuristic[i[1]]}")
                temp_weight_dict[temp_tuple] = weightsUnDir[i]

            nodesList = copy.deepcopy(temp_node_list)
            weightList = temp_weight_dict.keys()
            G = nx.Graph()
            G.add_nodes_from(nodesList)
            G.add_edges_from(weightList)
            #pos = nx.spring_layout(G)
            pos = nx.kamada_kawai_layout(G)

            pos_attrs = {}
            for node, coords in pos.items():
                pos_attrs[node] = (coords[0], coords[1] + abs(coords[1])/3*1.2)

            nx.draw(G, pos, with_labels=True, node_color="blue", node_size=2000, font_color="white", font_size=20,
                    font_family="Times New Roman", font_weight="bold", width=5, edge_color="black")
            nx.draw_networkx_edge_labels(G, pos, font_size=26, edge_labels=temp_weight_dict, font_color='black')

            # nx.draw_networkx_labels(G, pos_attrs, labels=heuristic, font_size=12, font_color='k',
            #                         font_family='sans-serif', font_weight='normal', alpha=None, bbox=None,
            #                         horizontalalignment='center', verticalalignment='center', ax=None, clip_on=True)

        if path:
            return pos

        plt.margins(0.2)
        plt.show()


if __name__ == "__main__":
    from PyQt5.QtGui import QFont

    app = QApplication(sys.argv)
    #
    # font = QFont()
    # font.setPointSize(10)
    # app.setFont(font)

    window = QMainWindow()
    window.setWindowTitle('Input Field Example')
    window.resize(900, 400)
    ui = AILabProject()
    ui.load_gui(window)
    window.show()
    sys.exit(app.exec_())
