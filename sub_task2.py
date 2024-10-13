import requests
import json


# headers = {
#     'Authorization': f'token {my_token}',
#     'Connection': 'close'
# }
def get_default_branch(repo_full_name):
    """这里要先获取一下默认分支，方便后面读文件"""
    url = f"https://api.github.com/repos/{repo_full_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("default_branch", "main")  # Return "main" branch if not found
    return "main"

def is_cpython_cooperation(repo_full_name):
    # url=f"https://api.github.com/repos/{repo_full_name}/contents/"

    default_branch = get_default_branch(repo_full_name)
    url=f"https://api.github.com/repos/{repo_full_name}/git/trees/{default_branch}?recursive=1"
    response=requests.get(url)
    data=response.json()

    for item in data["tree"]:
        if item["type"] == "blob":
           if item["path"].endswith((".cpp", ".c")):
                #print(item["path"])
                url=f"http://raw.githubusercontent.com/{repo_full_name}/{default_branch}/{item['path']}"
                download_response=requests.get(url)
                if download_response.status_code == 200:
                    if "#include <Python.h>" in download_response.text:
                        #print(download_response.text)
                        return "Y"

    # output_string=json.dumps(data,indent=4)

    return "N"



    # out_string = json.dumps(data, indent=4)
    # print (out_string)

urls=["python-pillow/Pillow","giampaolo/psutil","scipy/scipy","encode/httpcore"]

def out_put(url_list):
    for item in url_list:
        print(f"{item}  {is_cpython_cooperation(item)}")

if __name__ == "__main__":
    out_put(urls)
