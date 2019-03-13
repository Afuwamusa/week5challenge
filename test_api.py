from api import app
import json
def test_start():
    with app.test_client() as c:
        response = c.get('/')
        data=json.loads(response.data)
        assert data['message']=='my diary'

def test_get_all_entries():

    with app.test_client() as c:
        response = c.get('/v1/api/ent')
        data=json.loads(response.data)
        assert type(data) == dict
        assert response.status_code==200
        assert data['entry'] !=None




       

        