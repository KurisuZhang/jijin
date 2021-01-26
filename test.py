import numpy as np
import requests
import json
import os
import re

x = np.array([1,2,3,4,5,6])

print(np.exp(x))

env_dist = os.environ

data = {"text": "今天基金结果","desp":"hahahahahah"}
url = "https://sc.ftqq.com/" + env_dist["SERVERJIANG"] + ".send"
requests.post(url,params=data)
