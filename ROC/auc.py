# 通过抽样的方法计算auc
import numpy as np
from sklearn.metrics import roc_auc_score
 
y = np.array([0,1,1,0,0,0,0,0,0])  # 真实值
y_pred = np.array([1,1,1,0,0,0,0,0,0])  # 预测值

auc_score2 = roc_auc_score(y, y_pred)
print(auc_score2) 


