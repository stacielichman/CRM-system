from random import choices
from string import ascii_letters

from django.contrib.auth.models import User
from django.test import TestCase

from django.urls import reverse

from .models import Advert, Contract, Service, Client


class AdvertCreateViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

        self.advert_name = "".join(choices(ascii_letters, k=10))
        self.advert_description = "".join(choices(ascii_letters, k=10))
        self.channel = "".join(choices(ascii_letters, k=10))

        Advert.objects\
            .filter(
             name=self.advert_name,
             description=self.advert_description,
             channel=self.channel,
            )\
            .delete()

    def test_create_advert(self):
        response = self.client.post(
            reverse("app:create_advert"),
            {
                "name": self.advert_name,
                "description": self.advert_description,
                "channel": self.channel,
                "budget": 23.45
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/app/adverts/")
        self.assertTrue(
            Advert.objects
            .filter(
                name=self.advert_name,
                description=self.advert_description,
                channel=self.channel
            )
            .exists()
        )


class AdvertListViewTestCase(TestCase):
    fixtures = [
        'advert_app_fixtures.json'
    ]

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_adverts(self):
        response = self.client.get(reverse('app:adverts_list'))
        self.assertQuerySetEqual(
            Advert.objects.values("pk", "name").all(),
            response.context["adverts"]
        )
        self.assertTemplateUsed(response, 'app/adverts_list.html')
        self.assertEqual(response.status_code, 200)


class AdvertDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

        self.advert = Advert.objects.create(
            name="".join(choices(ascii_letters, k=10)),
            description="".join(choices(ascii_letters, k=10)),
            channel="".join(choices(ascii_letters, k=10))
        )

    def teardown(self) -> None:
        self.advert.delete()

    def test_get_advert(self):
        response = self.client.get(
            reverse("app:advert_details", kwargs={"pk": self.advert.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_get_advert_and_check_content(self):
        response = self.client.get(
            reverse("app:advert_details", kwargs={"pk": self.advert.pk})
        )
        self.assertContains(response, self.advert.name)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/advert_details.html')


class AdvertUpdateViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

        self.advert = Advert.objects.create(
            name="".join(choices(ascii_letters, k=10)),
            description="".join(choices(ascii_letters, k=10)),
            channel="".join(choices(ascii_letters, k=10))
        )

    def teardown(self) -> None:
        self.advert.delete()

    def test_update_advert(self):
        update_data = {
                "name": "updated",
                "description": "updated",
                "channel": "updated",
                "budget": 99.76
            }
        Advert.objects.filter(
            name="updated",
            description="updated",
            channel="updated",
            budget=99.76
        )\
            .delete()
        response = self.client.post(
            reverse(
                "app:update_advert",
                kwargs={"pk": self.advert.pk}),
            data=update_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Advert.objects
            .filter(
                name="updated",
            )
            .exists()
        )


class ContractCreateViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

        self.contract_name = "".join(choices(ascii_letters, k=10))
        self.contract_description = "".join(choices(ascii_letters, k=10))

        Contract.objects.filter(
            name=self.contract_name,
            description=self.contract_description
        ).delete()

    def test_create_contract(self):
        response = self.client.post(
            reverse("app:create_contract"),
            {
                "name": self.contract_name,
                "description": self.contract_description,
                "created_at": '2024-12-23',
                "validity_period": 20,
                "price": 23.45
            }
        )
        self.assertRedirects(response, "/app/contracts/")
        self.assertTrue(
            Contract.objects
            .filter(
                name=self.contract_name,
                description=self.contract_description,
            )
            .exists()
        )


class ContractListViewTestCase(TestCase):
    fixtures = [
        'contract_app_fixtures.json'
    ]

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_contracts(self):
        response = self.client.get(reverse('app:contracts_list'))
        self.assertQuerySetEqual(
            Contract.objects.values("pk", "name").all()[0],
            response.context["contracts"][0]
        )
        self.assertTemplateUsed(response, 'app/contracts_list.html')
        self.assertEqual(response.status_code, 200)


class ContractDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

        self.contract = Contract.objects.create(
            name="".join(choices(ascii_letters, k=10)),
            description="".join(choices(ascii_letters, k=10)),
        )

    def teardown(self) -> None:
        self.contract.delete()

    def test_get_advert(self):
        response = self.client.get(
            reverse("app:contract_details", kwargs={"pk": self.contract.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_get_contract_and_check_content(self):
        response = self.client.get(
            reverse("app:contract_details", kwargs={"pk": self.contract.pk})
        )
        self.assertContains(response, self.contract.name)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/contract_details.html')


class ContractUpdateViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

        self.contract = Contract.objects.create(
            name="".join(choices(ascii_letters, k=10)),
            description="".join(choices(ascii_letters, k=10)),
        )

    def teardown(self) -> None:
        self.contract.delete()

    def test_update_contract(self):
        update_data = {
                "name": "updated",
                "description": "updated",
                "validity_period": 100,
                "price": 23.67
            }
        Contract.objects.filter(
            name="updated",
            description="updated",
            validity_period=200,
            price=11.22
        )\
            .delete()
        response = self.client.post(
            reverse(
                "app:update_contract",
                kwargs={"pk": self.contract.pk}),
            data=update_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Contract.objects
            .filter(
                name="updated",
            )
            .exists()
        )


class ServiceCreateViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

        self.service_name = "".join(choices(ascii_letters, k=10))
        self.service_description = "".join(choices(ascii_letters, k=10))

        Service.objects.filter(
            name=self.service_name,
            description=self.service_description
        ).delete()

    def test_create_service(self):
        response = self.client.post(
            reverse("app:create_service"),
            {
                "name": self.service_name,
                "description": self.service_description,
                "price": 11.11
            }
        )
        self.assertRedirects(response, "/app/services/")
        self.assertTrue(
            Service.objects
            .filter(
                name=self.service_name,
                description=self.service_description,
            )
            .exists()
        )


class ServiceListViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_services(self):
        response = self.client.get(reverse('app:services_list'))
        self.assertQuerySetEqual(
            Service.objects.values("pk", "name").all()[0],
            response.context["services"][0]
        )
        self.assertTemplateUsed(response, 'app/services_list.html')
        self.assertEqual(response.status_code, 200)


class ServiceDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

        self.service = Service.objects.create(
            name="".join(choices(ascii_letters, k=10)),
            description="".join(choices(ascii_letters, k=10)),
            price=22.22
        )

    def teardown(self) -> None:
        self.service.delete()

    def test_get_service(self):
        response = self.client.get(
            reverse("app:service_details", kwargs={"pk": self.service.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_get_service_and_check_content(self):
        response = self.client.get(
            reverse("app:service_details", kwargs={"pk": self.service.pk})
        )
        self.assertContains(response, self.service.name)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/service_details.html')


class ServiceUpdateViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

        self.service = Service.objects.create(
            name="".join(choices(ascii_letters, k=10)),
            description="".join(choices(ascii_letters, k=10)),
            price=66.99
        )

    def teardown(self) -> None:
        self.service.delete()

    def test_update_service(self):
        update_data = {
                "name": "updated",
                "description": "updated",
                "price": 33.33
            }
        Service.objects.filter(
            name="updated",
            description="updated",
            price=11.22
        )\
            .delete()
        response = self.client.post(
            reverse(
                "app:update_service",
                kwargs={"pk": self.service.pk}),
            data=update_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Service.objects
            .filter(
                name="updated",
            )
            .exists()
        )


class PotentialCreateViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

        self.name = "".join(choices(ascii_letters, k=10))
        self.surname = "".join(choices(ascii_letters, k=10))
        self.middle_name = "".join(choices(ascii_letters, k=10))
        self.phone_num = "".join(choices(ascii_letters, k=10))
        self.email = "".join(choices(ascii_letters, k=10))
        self.advert = 1
        self.contract = 1

        Client.objects.filter(
            name=self.name,
            surname=self.surname,
            middle_name=self.middle_name,
            phone_num=self.phone_num,
            email=self.email,
            advert=self.advert,
            contract=self.contract
            ).delete()

    def test_create_client(self):
        response = self.client.post(
            reverse("app:potential_create"),
            {
                "name": self.name,
                "surname": self.surname,
                "middle_name": self.middle_name,
                "phone_num": self.phone_num,
                "email": self.advert,
                "contract": self.contract
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/app/potential/')
        self.assertTrue(
            Client.objects
            .filter(
                name=self.name,
                phone_num=self.phone_num
            )
            .exists()
        )


class PotentialListViewTestCase(TestCase):
    fixtures = [
        'client_app_fixtures.json'
    ]

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_potential(self):
        response = self.client.get(reverse('app:potential_list'))
        self.assertQuerySetEqual(
            Client.objects.values("pk", "name").all(),
            response.context["clients"]
        )
        self.assertTemplateUsed(response, 'app/potential_list.html')
        self.assertEqual(response.status_code, 200)


class PotentialDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

        self.potential = Client.objects.create(
            name="".join(choices(ascii_letters, k=10)),
            surname="".join(choices(ascii_letters, k=10)),
            phone_num="".join(choices(ascii_letters, k=10)),
            email="".join(choices(ascii_letters, k=10)),
        )

    def teardown(self) -> None:
        self.potential.delete()

    def test_get_client(self):
        response = self.client.get(
            reverse("app:potential_details", kwargs={"pk": self.potential.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_get_potential_and_check_content(self):
        response = self.client.get(
            reverse("app:potential_details", kwargs={"pk": self.potential.pk})
        )
        self.assertContains(response, self.potential.name)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/potential_details.html')


class PotentialUpdateViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

        self.potential = Client.objects.create(
            name="".join(choices(ascii_letters, k=10)),
            surname="".join(choices(ascii_letters, k=10)),
            phone_num="".join(choices(ascii_letters, k=10)),
            email="".join(choices(ascii_letters, k=10)),
        )

    def teardown(self) -> None:
        self.potential.delete()

    def test_update_potential(self):
        update_data = {
                "name": "updated",
                "surname": "updated",
                "phone_num": "updated",
                "email": "updated"
            }
        Client.objects.filter(
            name="updated",
            surname="updated",
            phone_num="updated",
            email="updated"
        )\
            .delete()
        response = self.client.post(
            reverse(
                "app:update_potential",
                kwargs={"pk": self.potential.pk}),
            data=update_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Client.objects
            .filter(
                name="updated",
            )
            .exists()
        )


class ActiveCreateViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

        self.name = "".join(choices(ascii_letters, k=10))
        self.surname = "".join(choices(ascii_letters, k=10))
        self.middle_name = "".join(choices(ascii_letters, k=10))
        self.phone_num = "".join(choices(ascii_letters, k=10))
        self.email = "".join(choices(ascii_letters, k=10))
        self.advert = 1
        self.contract = 1

        Client.objects.filter(
            name=self.name,
            surname=self.surname,
            middle_name=self.middle_name,
            phone_num=self.phone_num,
            email=self.email,
            advert=self.advert,
            contract=self.contract
            ).delete()

    def test_create_client(self):
        response = self.client.post(
            reverse("app:create_active"),
            {
                "name": self.name,
                "surname": self.surname,
                "middle_name": self.middle_name,
                "phone_num": self.phone_num,
                "email": self.advert,
                "contract": self.contract
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/app/active/')
        self.assertTrue(
            Client.objects
            .filter(
                name=self.name,
                phone_num=self.phone_num
            )
            .exists()
        )


class ActiveListViewTestCase(TestCase):
    fixtures = [
        'client_app_fixtures.json'
    ]

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_active(self):
        response = self.client.get(reverse('app:active_list'))
        self.assertQuerySetEqual(
            Client.objects.values("pk", "name").all(),
            response.context["clients"]
        )
        self.assertTemplateUsed(response, 'app/active_list.html')
        self.assertEqual(response.status_code, 200)


class ActivelDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

        self.active = Client.objects.create(
            name="".join(choices(ascii_letters, k=10)),
            surname="".join(choices(ascii_letters, k=10)),
            phone_num="".join(choices(ascii_letters, k=10)),
            email="".join(choices(ascii_letters, k=10)),
        )

    def teardown(self) -> None:
        self.active.delete()

    def test_get_active(self):
        response = self.client.get(
            reverse("app:active_details", kwargs={"pk": self.active.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_get_active_and_check_content(self):
        response = self.client.get(
            reverse("app:active_details", kwargs={"pk": self.active.pk})
        )
        self.assertContains(response, self.active.name)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/active_details.html')


class ActiveUpdateViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="test", password="test", is_superuser=1)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

        self.active = Client.objects.create(
            name="".join(choices(ascii_letters, k=10)),
            surname="".join(choices(ascii_letters, k=10)),
            phone_num="".join(choices(ascii_letters, k=10)),
            email="".join(choices(ascii_letters, k=10)),
        )

    def teardown(self) -> None:
        self.active.delete()

    def test_update_active(self):
        update_data = {
                "name": "updated",
                "surname": "updated",
                "phone_num": "updated",
                "email": "updated"
            }
        Client.objects.filter(
            name="updated",
            surname="updated",
            phone_num="updated",
            email="updated"
        )\
            .delete()
        response = self.client.post(
            reverse(
                "app:update_active",
                kwargs={"pk": self.active.pk}),
            data=update_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Client.objects
            .filter(
                name="updated",
            )
            .exists()
        )
