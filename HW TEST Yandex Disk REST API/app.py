import requests

URL= 'https://cloud-api.yandex.net/v1/disk/resources'
token = 'Your token'
HEADERS = {'Authorization': 'OAuth {}'.format(token)}

def get_status_folder(folder):
    """Метод проверяет наличие папки на яндекс диск"""
    params = {'path': f'disk:/{folder}'}
    response = requests.get(url=URL, headers=HEADERS, params=params)
    return response.status_code

def create_new_folder(folder_name):
    """Метод создает папку на яндекс диск"""
    params = {'path': folder_name}
    response = requests.put(url=URL, headers=HEADERS, params=params)
    return response.status_code


def delete_folder(folder_name):
    """Метод удаляет папку на яндекс диск"""
    params = {'path': folder_name, 'permamently': True}
    response = requests.delete(URL, headers=HEADERS, params=params)
    return response.status_code


if __name__ == '__main__':
   create_new_folder('Test_folder')
   print(get_status_folder('Test_folder'))
   print(delete_folder('Test_folder'))
   print('====',get_status_folder('Test_folder'))