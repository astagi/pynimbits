import requests, json

class NimbitsError(Exception):
  '''Base class for Nimbits errors'''

  @property
  def message(self):
    return self.args[0]

class Nimbits:

    ninbits_url_template = '%s/service/v2/%s'

    def __init__(self, email, key, endpoint='http://cloud.nimbits.com'):
        self.email = email
        self.key = key
        self.endpoint = endpoint

    def set_endpoint(self, endpoint):
        self.endpoint = endpoint

    def get_tree(self):
        query = {'email':self.email,'key':self.key}
        req = self.__send_request('GET', 'tree', query)
        return self.__parse_response(req)

    def get_value(self, id_entity):
        query = {'email':self.email,'key':self.key,'id':id_entity}
        req = self.__send_request('GET', 'value', query)
        return self.__parse_response(req)

    def set_value(self, id_entity, **params):
        query = {'email':self.email,'key':self.key,'action':'update','id':id_entity}
        req = self.__send_request('POST', 'value', query, params)
        return self.__parse_response(req)

    def __parse_response(self, req):
        if req.status_code == 200:
            return req.json()
        elif req.status_code == 401:
            raise NimbitsError('Access denied')
        else:
            raise NimbitsError(req.text)

    def __build_query(self, params):
        query = ''
        for key, value in params.iteritems():
            query = query + '%s=%s&' % (key, value)
        return query

    def __send_request(self, method, service, query=None, params=None):
        url = self.ninbits_url_template % (self.endpoint, service)
        if query:
            url = '%s?%s' % (url, self.__build_query(query))
        headers = {'Content-type': 'application/json', 'Accept': '*/*'}
        if params and not 'owner' in params.keys():    
            params["owner"] = self.email
        if method == 'POST':
            req = requests.post(url=url, data=json.dumps(params), headers=headers)
        elif method == 'GET':
            req = requests.get(url=url, headers=headers)
        return req
