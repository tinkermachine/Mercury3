import requests
import json
import numpy as np

x_pred = np.loadtxt(".\\x_pred.csv",delimiter=",")
x_list = x_pred.tolist()
payload={
    "instances":[{'dense_input':x_list}]
}

r = requests.post('http://localhost:8501/v1/models/mercury:predict',json = payload)
x = r.content
print(x)


