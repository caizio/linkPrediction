# 读取ROCtxt，用于绘制图像
class Data:
    def __init__(self) -> None:
        # 方法的名称
        self.name = ""
        # 横坐标
        self.x = []
        # 纵坐标
        self.y = []
        
class ReadROCTxt:
    def __int__(self):
        pass
    def read(self,dir:str):
        with open(dir) as f:
            datas = []
            datasName = []
            for j in range(6):
                dataName = f.readline().replace("\n","")
                datasName.append(dataName)
                # 一个数据集下有几个方法
                number = int(f.readline())
                vector_data = []
                for i in range(number):
                # for i in range(500):
                    data = Data()
                    data.name = f.readline()
                    data.name = data.name[0:len(data.name)-1]
                    data.x = f.readline().split(",")
                    data.x.pop()
                    data.y = f.readline().split(",")
                    data.y.pop()
                    # 将字符串转成浮点型
                    data.x = [float(p) for p in data.x]
                    data.y = [float(p) for p in data.y]
                    vector_data.append(data)
                datas.append(vector_data)
        return datas,datasName

if __name__ == "__main__":
    dir = "./result/1_12.txt"
    rROCt = ReadROCTxt()
    datas,datasName = rROCt.read(dir)
    print("读取的数据集数量：",len(datas))
    print("数据集名称：",datasName[1])
    print(datas[0][0].name)
    print(datas[0][0].x[0:10])
    print(datas[0][0].y[0:10])