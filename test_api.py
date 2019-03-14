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
        assert data['entry'] !=None




def test_post_all_entries():
    with app.test_client() as c:
        
        data={
            "entry":"teaching",
            "date":"12/03/2020",
            "time":"09:00"
        }
        response = c.post('/v1/api/ent', json=data)
        assert type(data) == dict
        assert data['entry'] != None  


def test_put_all_entries():
     with app.test_client() as c:
        data={
                "entry":"travel",
                "date":"05/05/2020",
                "time":"06:00"
        }
        response = c.put('/v1/api/entry', json = data)
        assert type(data) == dict
        assert data['entry'] != None

        