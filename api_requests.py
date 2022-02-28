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
        print(payload)
        r = requests.get('https://dev.to/api/articles', params=payload)
        if r.status_code == 200:
            return r.json()

    def tags(self, **kwargs):
        valid_quaries = ('page', 'per_page')
        payload = self._payload(valid_quaries, **kwargs)

    def videos(self, **kwargs):
        valid_quaries = ('page', 'per_page')
        payload = self._payload(valid_quaries, **kwargs)

    def profile_images(self, **kwargs):
        valid_quaries = ('username')
        payload = self._payload(valid_quaries, **kwargs)

if __name__ == '__main__':
    test = Dev_to_api()
    test.articles(page=2)