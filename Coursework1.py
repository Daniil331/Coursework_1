import requests
from pprint import pprint
import time
from tqdm import tqdm

#добавляет в файл список словарей фото по токену вк и имени файла

def vk_photos_get(access_token, file, id_account):

    url = 'https://api.vk.com/method/photos.get'
    params = {'owner_id': id_account,
              'album_id': 'profile',
              'access_token': access_token,
              'v': '5.131',
              'extended': 1,
              'photo_sizes': 1,
              }
    response = requests.get(url, params=params)
    a = (response.json())
    b = (a['response']['items'])
    list_url_photos = []
    list_likes_photos = []
    for c in b:
        list_likes_photos.append(c['likes']['count'])
    for open_list_likes in list_likes_photos:
        op = open_list_likes
    for c in b:
        c3 = (c['sizes'])
        for c4 in c3:
            if c4['type'] in 'z':
                list_url_photos.append(c4)
    for openg in list_url_photos:
        for likes in list_likes_photos:
            openg['file_name'] = likes

    with open(file, 'w') as document:
        document.write(f'{list_url_photos}')
    return list_url_photos


class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href_json = self._get_upload_link(disk_file_path=disk_file_path)
        href = href_json['href']
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
        else:
            print('Failet')


if __name__ == '__main__':
    #вводить без кавычек)
    token_vk = input('Enter the token VK: ')
    #file = input('Enter the file name: ') #в какой файл передавать фото
    token_ya = input('Enter the token YA: ')
    id_account = input('Enter the id account VK: ')
    token = token_ya
    uploader = YaUploader(token)
    disk_file_path = 'photos_vk/file_photos_vk.txt'
    uploader.upload_file_to_disk(disk_file_path, 'file.txt')
print(vk_photos_get(token_vk, 'file.txt', id_account))


mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in tqdm(mylist):
    time.sleep(1)




