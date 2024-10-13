import requests


def get_first_n_repo(n):
    # headers={
    #     'Authorization': f'token {my_token}',
    # 'Connection':'close'
    # }
    list_n=[]
    url = "http://api.github.com/search/repositories"
    # 参数构造参考：https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#search-repositories
    payload = {
        "q": "Python",
        "sort": "stars",
        "order": "desc",
        "per_page": n,
        "page": 1
    }

    response = requests.get(url, params=payload)
    data = response.json()
    for item in data['items']:
        list_n.append({item['full_name']:item['stargazers_count']})

    return list_n


if __name__ == "__main__":

    list1 = get_first_n_repo(10)
    for item in list1:
        for key, value in item.items():
            print(f"{key}: stars {value}")





