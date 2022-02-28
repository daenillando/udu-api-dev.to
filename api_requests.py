import requests

class Dev_to_api():
    def __init__(self):
        pass

    def _payload(self, valid_quaries, **kwargs):
        payload = {}
        for kwarg in kwargs:
            if kwarg in valid_quaries:
                payload[kwarg] = kwargs[kwarg]
        return payload

    def articles(self, **kwargs):
        valid_quaries = ('page', 'per_page', 'tag', 'tags', 'tags_exclude', 'username', 'state', 'top', 'collection_id')
        payload = self._payload(valid_quaries, **kwargs)
        r = requests.get('https://dev.to/api/articles', params=payload)
        if r.status_code == 200:
            return r.json()

    def tags(self, **kwargs):
        valid_quaries = ('page', 'per_page')
        payload = self._payload(valid_quaries, **kwargs)
        r = requests.get('https://dev.to/api/tags', params=payload)
        if r.status_code == 200:
            return r.json()

    def videos(self, **kwargs):
        valid_quaries = ('page', 'per_page')
        payload = self._payload(valid_quaries, **kwargs)
        r = requests.get('https://dev.to/api/videos', params=payload)
        if r.status_code == 200:
            return r.json()

    def profile_images(self, username):
        r = requests.get('https://dev.to/api/profile_images/{0}'.format(username))
        #if r.status_code == 200:
        return r.json()


if __name__ == '__main__':
    test = Dev_to_api()
    print('articles')
    print('*' * 10)
    print(test.articles(page=1, per_page=2))
    print('*'*10)
    print('tags')
    print('*' * 10)
    print(test.tags(page=1))
    print('*' * 10)
    print('videos')
    print('*' * 10)
    print(test.videos(page=1, per_page=5))
    print('*' * 10)
    print('profile_images')
    print('*' * 10)
    print(test.profile_images(username='iamschulz'))