# -*-coding : utf-8 -*-
from pygraph.classes.digraph import digraph
import os
class PRIterator:
    __doc__ = '''计算一张图中的Pr值'''

    def __init__(self, dg):
        self.damping_factor = 0.85 # α
        self.max_iterations = 100 #最大迭代次数
        self.min_delta = 0.00001 #|pn+1-pn|<delta
        self.graph = dg

    def page_rank(self):
        #对没有出连的节点改为对所有节点都有出连
        for node in self.graph.nodes():
            if len(self.graph.neighbors(node)) == 0:
                for node2 in self.graph.nodes():
                    digraph.add_edge(self.graph,(node, node2))

        nodes = self.graph.nodes()
        graph_size = len(nodes)

        if graph_size == 0:
            return {}
        page_rank = dict.fromkeys(nodes, 1.0/graph_size)
        damping_value = (1.0 - self.damping_factor)/graph_size#(1-α)/N

        flag = False
        for i in range(self.max_iterations):
            change = 0
            for node in nodes:
                rank = 0
                for incident_page in self.graph.incidents(node):
                    rank += self.damping_factor * (page_rank[incident_page] / len(self.graph.neighbors(incident_page)))
                rank += damping_value
                change += abs(page_rank[node]-rank)
                page_rank[node] = rank

            print("This is No.%s iteration" % (i+1))
            print(page_rank)

            if change < self.min_delta:
                flag = True
                break
        if flag:
            print('Finished in %s iterations!' % node)
        else:
            print('Finished out of 100 iterations!')
        return page_rank

if __name__ == '__main__':

    dg = digraph()
    dg.add_nodes(["A", "B", "C", "D", "E"])
    dg.add_edge(("A", "B"))
    dg.add_edge(("A", "C"))
    dg.add_edge(("A", "D"))
    dg.add_edge(("B", "D"))
    dg.add_edge(("C", "E"))
    dg.add_edge(("D", "E"))
    dg.add_edge(("B", "E"))
    dg.add_edge(("E", "A"))

    pr = PRIterator(dg)
    page_ranks = pr.page_rank()
    print("The final page rank is \n", page_ranks)
