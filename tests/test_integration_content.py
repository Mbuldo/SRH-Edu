from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_create_read_update_delete_sti():
    sti_data = {
        'name': 'TestSTI',
        'description': 'desc',
        'symptoms': 'symp',
        'prevention': 'prev',
        'treatment': 'treat'
    }
    # Create
    create_resp = client.post('/api/content/', json=sti_data)
    assert create_resp.status_code == 200
    sti_id = create_resp.json()['id']

    # Read
    get_resp = client.get(f'/api/content/{sti_id}')
    assert get_resp.status_code == 200
    # Update
    sti_data_update = sti_data.copy()
    sti_data_update['name'] = 'UpdatedSTI'
    update_resp = client.put(f'/api/content/{sti_id}', json=sti_data_update)
    assert update_resp.status_code == 200
    # Delete
    del_resp = client.delete(f'/api/content/{sti_id}')
    assert del_resp.status_code == 200


def test_faq_crud():
    # Create
    faq_resp = client.post('/api/content/faqs/', params={'question': 'Q1', 'answer': 'A1'})
    assert faq_resp.status_code == 200
    faqid = faq_resp.json()['id']
    # Read all
    getall = client.get('/api/content/faqs/')
    assert getall.status_code == 200
    # Read one
    one = client.get(f'/api/content/faqs/{faqid}')
    assert one.status_code == 200
    # Update
    up = client.put(f'/api/content/faqs/{faqid}', params={'question': 'Q2', 'answer': 'A2'})
    assert up.status_code == 200
    # Delete
    d = client.delete(f'/api/content/faqs/{faqid}')
    assert d.status_code == 200


def test_healthtip_crud():
    # Create
    tip_resp = client.post('/api/content/healthtips/', params={'tip': 'Drink water', 'created_by': 'System'})
    assert tip_resp.status_code == 200
    tipid = tip_resp.json()['id']
    # Read all
    ga = client.get('/api/content/healthtips/')
    assert ga.status_code == 200
    # Read one
    one_tip = client.get(f'/api/content/healthtips/{tipid}')
    assert one_tip.status_code == 200
    # Update
    utip = client.put(f'/api/content/healthtips/{tipid}', params={'tip': 'Drink more water'})
    assert utip.status_code == 200
    # Delete
    deltip = client.delete(f'/api/content/healthtips/{tipid}')
    assert deltip.status_code == 200
