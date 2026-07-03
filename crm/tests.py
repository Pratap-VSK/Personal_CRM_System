from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Contact, Interaction


class CRMAppTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='secure123')

    def test_contact_and_interaction_creation(self):
        contact = Contact.objects.create(
            user=self.user,
            name='Jane Doe',
            email='jane@example.com',
            phone='123456789',
            category='Client',
            notes='Met at the conference.',
        )
        interaction = Interaction.objects.create(
            contact=contact,
            date='2024-01-15',
            interaction_type='Call',
            summary='Discussed onboarding timeline.',
        )

        self.assertEqual(contact.name, 'Jane Doe')
        self.assertEqual(interaction.summary, 'Discussed onboarding timeline.')
        self.assertEqual(contact.interactions.count(), 1)

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('crm:dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_registration_page_loads(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
