from hashlib import md5
from requests import get
from datetime import datetime

class RestMarvel:
    timestamp = datetime.now().strftime('%Y-%m-%d%H:%M:%S')
    pub_key = 'e255c9e50e7a9db6e759e361daf72c5a'
    priv_key = '9cce20e67cfd205195958c95db8c951bef693487'

    def hash_params(self):
        hash_md5 = md5()
        hash_md5.update(f'{self.timestamp}{self.priv_key}{self.pub_key}'.encode('utf-8'))
        hashed_params = hash_md5.hexdigest()
        return hashed_params
    
    def get_heroes(self):
        params = {'ts': self.timestamp, 'apikey': self.pub_key, 'hash': self.hash_params()}
        results = get('https://gateway.marvel.com:443/v1/public/characters', params=params)

        if results.status_code == 200:
            data = results.json()
            print(data)
            
        else:
            print(f"Error: {results.status_code} - {results.text}")

rm = RestMarvel()
rm.get_heroes()