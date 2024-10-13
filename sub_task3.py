from sub_task1 import get_first_n_repo
from sub_task2 import out_put


list1=get_first_n_repo(100)
url_list=[]
for item in list1:
    for key in item.keys():
        url_list.append(key)

print(url_list)
out_put(url_list)