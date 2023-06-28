import requests
BaseUrl = 'https://www.tabnews.com.br/api/v1/'


class Client:
    def __init__(self, email=None, password=None) -> None:
        payload = {
            "email": email,
            "password": password
        }
        if email != None:
            login = requests.post('https://www.tabnews.com.br/api/v1/sessions', payload)
            if login.status_code == 201:
                self.token = login.json()['token']
                return
            raise Exception('Error during login. Maybe your credentials are invalid.')
    
    class Analytics:
        def users_created():
            return requests.get(f'{BaseUrl}/analytics/users-created')
    
        def created_posts_per_day():
            return requests.get(f'{BaseUrl}/analytics/root-content-published')
        def new_users_per_day():
            return requests.get(f'{BaseUrl}/analytics/child-content-published')
        


    def publish(self, title:str, body, source_url=None, slug=None):
        auth = {'session_id': self.token} 
        payload = {
            "title":title,
            "body":body,
            "source_url":source_url,
            "slug":slug,
            "status":"published"
        }
        return requests.post('https://www.tabnews.com.br/api/v1/contents', payload, cookies=auth)
    
    def get_posts(self, pagina:int, porPagina:int, estrategia:str):
        '''Retorna os posts da tela inicial. estrategia pode ser "new", "old" ou "relevant"'''
        return requests.get(f'https://www.tabnews.com.br/api/v1/contents?page={pagina}&per_page={porPagina}&strategy={estrategia}')

    def get_posts_user(self, pagina:int, porPagina:int, estrategia:str, username:str):
        '''Retorna os posts de um user. estrategia pode ser "new", "old" ou "relevant"'''
        return requests.get(f'https://www.tabnews.com.br/api/v1/{username}?page={pagina}&per_page={porPagina}&strategy={estrategia}')

    def get_post(self, username:str, slug:str):
        return requests.get(f'https://www.tabnews.com.br/api/v1/{username}/{slug}')

    def get_post_comments(self, username:str, slug:str):
        return requests.get(f'https://www.tabnews.com.br/api/v1/{username}/{slug}/children')

    def get_post_thumbnail(self, username:str, slug:str):
        return requests.get(f'https://www.tabnews.com.br/api/v1/{username}/{slug}/thumbnail')