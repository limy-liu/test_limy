import json

def build_login_data():
    with open('./login_data.json', encoding='utf-8') as f:
        data = json.load(f)
        data_list = list()
        for i in data:
            data_list.append((i.get('username'),
                  i.get('password'),
                  i.get('code'),
                  i.get('expect')))
        print(data_list)
        return data_list