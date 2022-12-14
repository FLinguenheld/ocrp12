import pytest

from epic_crm.users.models import User
from epic_crm.clients.models import Client
from epic_crm.contracts.models import Contract


@pytest.mark.django_db
class TestContractsWithSalespeople:

    def test_technical_support_can_list_contracts(self, api_client_technical_support):

        client_0 = Client.objects.create(name='Client name', salesperson=None)
        contract_0 = Contract.objects.create(client=client_0, amount=1000, date_signed='2015-05-15T00:00:00Z')

        # --
        response = api_client_technical_support.get('/contracts/')
        data = response.json()

        assert response.status_code == 200
        assert data[0]['client'] == contract_0.client.pk
        assert data[0]['amount'] == 1000

    def test_salesperson_can_get_client_details(self, api_client_technical_support):

        client_0 = Client.objects.create(name='Client name', salesperson=None)
        contract_0 = Contract.objects.create(client=client_0, amount=1000)

        # --
        response = api_client_technical_support.get('/contracts/')
        data = response.json()

        assert response.status_code == 200
        assert data[0]['client'] == contract_0.client.pk
        assert data[0]['amount'] == 1000

    def test_technical_support_cannot_create_a_new_contract(self, api_client_technical_support):

        salesperson = User.objects.create_user(email='as@test.com', password='0000', role='Salesperson')
        client = Client.objects.create(name='Client name', salesperson=salesperson)

        # --
        body = {'date_signed': '2015-05-15',
                'client': client.pk,
                'amount': 1000}

        response = api_client_technical_support.post('/contracts/', data=body)
        data = response.json()

        assert response.status_code == 403
        assert 'Only the assigned salesperson or managers are authorized to do this request' in data['detail']

    def test_technical_support_cannot_update_a_contract(self, api_client_technical_support):

        salesperson = User.objects.create_user(email='as@test.com', password='0000', role='Salesperson')
        client = Client.objects.create(name='Client name', salesperson=salesperson)
        contract = Contract.objects.create(client=client, amount=1000, date_signed='2022-01-22T00:00:00Z')

        # --
        body = {'date_signed': '2015-05-15',
                'client': client.pk,
                'amount': 1000}

        response = api_client_technical_support.put(f'/contracts/{contract.pk}/', data=body)
        data = response.json()

        assert response.status_code == 403
        assert 'Only the assigned salesperson or managers are authorized to do this request' in data['detail']

    def test_salesperson_cannot_delete_a_contract(self, api_client_technical_support):

        salesperson = User.objects.create_user(email='as@test.com', password='0000', role='Salesperson')
        client = Client.objects.create(name='Client name', salesperson=salesperson)
        contract_to_delete = Contract.objects.create(client=client, amount=1000, date_signed='2022-01-22T00:00:00Z')

        # --
        response = api_client_technical_support.delete(f'/contracts/{contract_to_delete.pk}/')
        data = response.json()

        assert response.status_code == 403
        assert 'Only managers are authorized to do this request' in data['detail']
