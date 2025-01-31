import pytest
from django.urls import reverse
from .models import FAQ

@pytest.mark.django_db
def test_faq_translation():
    faq = FAQ.objects.create(question_en='Hello', answer_en='World')
    assert faq.get_translated_question('hi') != 'Hello'

@pytest.mark.django_db
def test_api(client):
    FAQ.objects.create(question_en='Q', answer_en='A', question_hi='Q_hi', answer_hi='A_hi')
    response = client.get(reverse('faq-list') + '?lang=hi')
    assert response.json()[0]['question'] == 'Q_hi'