# 计算网络的统计特征
import networkx as nx

# 储存图数据的类
class Gdata:
    def __int__(self):
        self.N = 0
        self.E = 0
        self.D = 0.0
        self.SD = 0.0
        self.CC = 0.0
        self.AC = 0.0
        self.DH = 0.0
    def show(self):
        print("节点数：",self.N)
        print("边数：",self.E)
        print("平均度：",self.D)
        print("平均最短距离：",self.SD)
        print("平均聚类系数：",self.CC)
        print("同配系数：",self.AC)
        print("度异质性：",self.DH)
# 计算统计特征
def acc(path:str)->Gdata:
    # 读取的文件数据如下储存：
    # 1,2
    # 2,3
    # 3,6
    with open(path) as f:
        data = []
        lines = f.read().split("\n")
    for line in lines:
        # 注意，这里边的分割是按照","
        edge = line.split(",")
        if len(edge) == 2:
            data.append((edge[0],edge[1]))
    G = nx.Graph()
    G.add_edges_from(data) 
    gdata = Gdata()
    gdata.N = len(G.nodes())
    gdata.E = len(G.edges())
    gdata.D = 2 * gdata.E / gdata.N
    gdata.CC = nx.average_clustering(G)
    gdata.AC = nx.degree_assortativity_coefficient(G)
    temp = 0
    degree = nx.degree(G)
    for i in degree:
        temp = temp + i[1] * i[1] / gdata.D / gdata.D
    gdata.DH = temp / gdata.N
    gdata.SD = 0
    # 计算网络的平均最短距离,开销比较大,耐心等待,10万条边大概30分钟
    largest = max(nx.connected_components(G),key=len)
    largest_connected_subgraph = G.subgraph(largest)
    gdata.SD = nx.average_shortest_path_length(largest_connected_subgraph)
    gdata.show()
    return gdata
# 从路径中获取数据集的名字
def getDataset(path:str)->str:
    index = path.rfind("/") + 1
    res = path[index: len(path) - 4]
    return res

if __name__ == "__main__":
    test_dir = ["./dataset/LNBL3DataSet/S. pombe/S. pombe.txt"]
    paths = ["./dataset/LNBL3DataSet/A. thaliana/A. thaliana.txt",
        "./dataset/LNBL3DataSet/C. elegans/C. elegans.txt",
        "./dataset/LNBL3DataSet/D. Melanogaster/D. Melanogaster.txt",
        "./dataset/LNBL3DataSet/H. sapiens/H. sapiens.txt",
        "./dataset/LNBL3DataSet/HuRI/HuRI.txt",
        "./dataset/LNBL3DataSet/S. cerevisiae/S. cerevisiae.txt",
        "./dataset/LNBL3DataSet/S. pombe/S. pombe.txt",]
    out_path = "./temp/information.csv"
    out_string = ",节点数,边数,平均度,平均最短距离,平均聚类系数,同配系数,度异质性\n"
    # for path in paths:
    for path in test_dir:
        out_string += getDataset(path) + ","
        data = acc(path)
        out_string += str(data.N) +","+ str(data.E) +","+ str(data.D) +","+ str(data.SD) +","+ str(data.CC) +","+ str(data.AC) +","+ str(data.DH) + "\n"
    with open(out_path,"w") as f:
        f.write(out_string)

    


