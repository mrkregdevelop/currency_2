from currency.models import ContactUs


def test_get_contact_us(client):
    response = client.get('/currency/contactus/create/')
    assert response.status_code == 200


def test_post_contact_us_empty_form_200(client):
    response = client.post('/currency/contactus/create/')
    assert response.status_code == 200


def test_post_contact_us_empty_form_errors(client):
    response = client.post('/currency/contactus/create/')
    assert response.context_data['form'].errors == {
        'name': ['This field is required.'],
        'reply_to': ['This field is required.'],
        'subject': ['This field is required.'],
        'body': ['This field is required.']
    }


def test_post_contact_us_invalid_reply_to_200(client):
    payload = {
        'name': 'Name',
        'reply_to': 'INVALID_EMAIL',
        'subject': 'Subject',
        'body': 'Body'
    }
    response = client.post('/currency/contactus/create/', data=payload)
    assert response.status_code == 200


def test_post_contact_us_invalid_reply_to_errors(client):
    payload = {
        'name': 'Name',
        'reply_to': 'INVALID_EMAIL',
        'subject': 'Subject',
        'body': 'Body'
    }
    response = client.post('/currency/contactus/create/', data=payload)
    assert response.context_data['form'].errors == {
        'reply_to': ['Enter a valid email address.']
    }


def test_post_contact_us_valid_data_302(client, mailoutbox, settings):
    before = ContactUs.objects.count()
    payload = {
        'name': 'Name',
        'reply_to': 'email@example.com',
        'subject': 'Subject',
        'body': 'Body'
    }
    response = client.post('/currency/contactus/create/', data=payload)
    assert response.status_code == 302
    assert response.headers['Location'] == '/'
    assert len(mailoutbox) == 1
    assert mailoutbox[0].from_email == settings.DEFAULT_FROM_EMAIL
    assert ContactUs.objects.count() == before + 1
