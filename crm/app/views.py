from itertools import chain

from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Count, Sum
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView

from .models import Advert, Contract, Service, Client


class AdvertsListView(ListView):
    def test_func(self):
        return self.request.user.groups\
                   .filter(name="marketer")\
                   .exists() \
               or self.request.user.is_superuser
    template_name = "app/adverts_list.html"
    context_object_name = "adverts"
    queryset = Advert.objects.values("pk", "name").all()


class AdvertDetailView(DetailView):
    def test_func(self):
        return self.request.user.groups\
                   .filter(name="marketer")\
                   .exists() \
               or self.request.user.is_superuser
    template_name = "app/advert_details.html"
    model = Advert
    context_object_name = "advert"


class AdvertCreateView(CreateView):
    def test_func(self):
        return self.request.user.groups\
                   .filter(name="marketer")\
                   .exists() \
               or self.request.user.is_superuser
    model = Advert
    fields = "name", "description", "channel", "budget"
    success_url = reverse_lazy("app:adverts_list")


class AdvertUpdateView(UpdateView):
    def test_func(self):
        return self.request.user.groups\
                   .filter(name="marketer")\
                   .exists() \
               or self.request.user.is_superuser
    model = Advert
    fields = "name", "description"
    template_name = "app/advert_update_form"

    def get_success_url(self):
        return reverse(
            "app:advert_details",
            kwargs={"pk": self.object.pk}
        )


class AdvertDeleteView(DeleteView):
    model = Advert
    success_url = reverse_lazy("app:adverts_list")
    template_name = "app/confirm_advert_delete.html"


class ContractsListView(ListView):
    def test_func(self):
        return self.request.user.groups\
                   .filter(name="manager")\
                   .exists() \
               or self.request.user.is_superuser
    template_name = "app/contracts_list.html"
    context_object_name = "contracts"
    queryset = Contract.objects.values("pk", "name").all()


class ContractDetailView(DetailView):
    def test_func(self):
        return self.request.user.groups\
                   .filter(name="manager")\
                   .exists() \
               or self.request.user.is_superuser
    template_name = "app/contract_details.html"
    model = Contract
    context_object_name = "contract"


class ContractCreateView(CreateView):
    def test_func(self):
        return self.request.user.groups\
                   .filter(name="manager")\
                   .exists() \
               or self.request.user.is_superuser
    model = Contract
    fields = [
        "name",
        "description",
        "document",
        "created_at",
        "validity_period",
        "price"
    ]
    success_url = reverse_lazy("app:contracts_list")


class ContractUpdateView(UpdateView):
    def test_func(self):
        return self.request.user.groups\
                   .filter(name="manager")\
                   .exists() \
               or self.request.user.is_superuser
    model = Contract
    fields = "name", "description"
    template_name = "app/contract_update_form"

    def get_success_url(self):
        return reverse(
            "app:contract_details",
            kwargs={"pk": self.object.pk}
        )


class ContractDeleteView(DeleteView):
    model = Contract
    success_url = reverse_lazy("app:contracts_list")
    template_name = "contracts/confirm_contract_delete.html"


class ServicesListView(ListView):
    def test_func(self):
        return self.request.user.groups\
                   .filter(name="marketer")\
                   .exists() \
               or self.request.user.is_superuser
    template_name = "app/services_list.html"
    context_object_name = "services"
    queryset = Service.objects.values("pk", "name").all()


class ServiceDetailView(DetailView):
    def test_func(self):
        return self.request.user.groups\
                   .filter(name="marketer")\
                   .exists() \
               or self.request.user.is_superuser
    template_name = "app/service_details.html"
    model = Service
    context_object_name = "service"


class ServiceCreateView(CreateView):
    def test_func(self):
        return self.request.user.groups\
                   .filter(name="marketer")\
                   .exists() \
               or self.request.user.is_superuser
    model = Service
    fields = "name", "description", "price"
    success_url = reverse_lazy("app:services_list")


class ServiceUpdateView(UpdateView):
    def test_func(self):
        return self.request.user.groups\
                   .filter(name="marketer")\
                   .exists() \
               or self.request.user.is_superuser
    model = Service
    fields = "name", "description"
    template_name = "app/service_update_form.html"

    def get_success_url(self):
        return reverse(
            "app:service_details",
            kwargs={"pk": self.object.pk}
        )


class ServiceDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy("app:services_list")
    template_name = "app/confirm_service_delete.html"


class PotentialClientListView(UserPassesTestMixin, ListView):
    def test_func(self):
        return self.request.user.groups\
                   .filter(name="manager")\
                   .exists() or self.request.user.groups\
                   .filter(name="manager")\
                   .exists() or self.request.user.is_superuser
    template_name = "app/potential_list.html"
    queryset = (
        Client.objects
        .values("pk", "name", "surname", "middle_name")
        .filter(active=False)
    )
    context_object_name = "clients"


class PotentialClientCreateView(CreateView):
    def test_func(self):
        return self.request.user.groups\
                   .filter(name="operator")\
                   .exists() \
               or self.request.user.is_superuser
    model = Client
    fields = [
        "name",
        "surname",
        "middle_name",
        "phone_num",
        "email",
        "advert",
    ]
    success_url = reverse_lazy("app:potential_list")


class PotentialClientDetailView(DetailView):
    def test_func(self):
        return self.request.user.groups\
                   .filter(name="operator")\
                   .exists() or self.request.user.groups\
                   .filter(name="manager")\
                   .exists() or self.request.user.is_superuser
    template_name = "app/potential_details.html"
    model = Client
    context_object_name = "client"


class PotentialClientUpdateView(UpdateView):
    def test_func(self):
        return self.request.user.groups\
                   .filter(name="operator")\
                   .exists() \
               or self.request.user.is_superuser
    model = Client
    fields = [
        "name",
        "surname",
        "middle_name",
        "phone_num",
        "email",
        "advert",
    ]
    template_name = "app/potential_update_form.html"

    def get_success_url(self):
        return reverse(
            "app:potential_details",
            kwargs={"pk": self.object.pk}
        )


class MakeClientActiveView(UpdateView):
    def test_func(self):
        return self.request.user.groups\
                   .filter(name="manager")\
                   .exists() \
               or self.request.user.is_superuser
    model = Client
    fields = ("active",)
    success_url = reverse_lazy("app:potential_list")
    template_name = "app/confirm_active.html"

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.active = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class ActiveClientListView(ListView):
    template_name = "app/active_list.html"
    queryset = (
        Client.objects
        .values("pk", "name", "surname", "middle_name")
        .filter(active=True)
    )


class ActiveClientCreateView(CreateView):
    model = Client
    fields = [
        "name",
        "surname",
        "middle_name",
        "phone_num",
        "email",
        "advert",
        "contract"
    ]
    success_url = reverse_lazy("app:active_list")


class ActiveClientUpdateView(UpdateView):
    model = Client
    fields = [
        "name",
        "surname",
        "middle_name",
        "phone_num",
        "email",
        "advert",
        "active",
        "contract"
    ]
    template_name = "app/active_update_form.html"

    def get_success_url(self):
        return reverse(
            "app:active_details",
            kwargs={"pk": self.object.pk}
        )


class ActiveClientDetailView(DetailView):
    template_name = "app/active_details.html"
    model = Client
    context_object_name = "client"


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("app:active_list")
    template_name = "app/confirm_delete.html"


class StatisticsView(ListView):
    template_name = "app/statistics.html"
    context_object_name = "adverts"

    def get_queryset(self):
        advert_client_queryset = Advert.objects.annotate(
            client_cnt=Count("client"),
        )
        client_queryset = Client.objects.filter(active=True).count()
        advert_queryset = Advert.objects.aggregate(Sum('budget'))
        contract_queryset = Contract.objects.aggregate(Sum('price'))
        context_queryset = {
            "advert_client": advert_client_queryset,
            "client": client_queryset,
            "advert": advert_queryset,
            "contract": contract_queryset,
        }
        return context_queryset
