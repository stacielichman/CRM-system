from django.urls import path

from .views import (
    AdvertsListView,
    AdvertCreateView,
    AdvertDetailView,
    AdvertDeleteView,
    AdvertUpdateView,

    ContractsListView,
    ContractCreateView,
    ContractDetailView,
    ContractDeleteView,
    ContractUpdateView,

    ServicesListView,
    ServiceCreateView,
    ServiceDetailView,
    ServiceDeleteView,
    ServiceUpdateView,

    PotentialClientListView,
    PotentialClientUpdateView,
    PotentialClientCreateView,
    PotentialClientDetailView,

    ActiveClientDetailView,
    ActiveClientListView,
    ActiveClientCreateView,
    ActiveClientUpdateView,
    ClientDeleteView,
    MakeClientActiveView,

    StatisticsView,
)

app_name = 'app'

urlpatterns = [
    path("adverts/", AdvertsListView.as_view(), name="adverts_list"),
    path("advert_create/", AdvertCreateView.as_view(), name="create_advert"),
    path("adverts/<int:pk>/", AdvertDetailView.as_view(), name="advert_details"),
    path("adverts/<int:pk>/confirm-delete/", AdvertDeleteView.as_view(), name="delete_advert"),
    path("adverts/<int:pk>/update/", AdvertUpdateView.as_view(), name="update_advert"),

    path("contracts/", ContractsListView.as_view(), name="contracts_list"),
    path("contract_create/", ContractCreateView.as_view(), name="create_contract"),
    path("contracts/<int:pk>/", ContractDetailView.as_view(), name="contract_details"),
    path("contracts/<int:pk>/confirm-delete/", ContractDeleteView.as_view(), name="delete_contract"),
    path("contracts/<int:pk>/update/", ContractUpdateView.as_view(), name="update_contract"),

    path("services/", ServicesListView.as_view(), name="services_list"),
    path("service_create/", ServiceCreateView.as_view(), name="create_service"),
    path("services/<int:pk>/", ServiceDetailView.as_view(), name="service_details"),
    path("services/<int:pk>/confirm-delete/", ServiceDeleteView.as_view(), name="delete_service"),
    path("services/<int:pk>/update/", ServiceUpdateView.as_view(), name="update_service"),

    path("potential/", PotentialClientListView.as_view(), name="potential_list"),
    path("potential/create/", PotentialClientCreateView.as_view(), name="potential_create"),
    path("potential/<int:pk>/", PotentialClientDetailView.as_view(), name="potential_details"),
    path("potential/<int:pk>/update/", PotentialClientUpdateView.as_view(), name="update_potential"),
    path("potential/<int:pk>/confirm-active/", MakeClientActiveView.as_view(), name="confirm_active"),

    path("active/", ActiveClientListView.as_view(), name="active_list"),
    path("active/create/", ActiveClientCreateView.as_view(), name="create_active"),
    path("active/<int:pk>/update/", ActiveClientUpdateView.as_view(), name="update_active"),
    path("active/<int:pk>/", ActiveClientDetailView.as_view(), name="active_details"),
    path("active/<int:pk>/confirm-delete/", ClientDeleteView.as_view(), name="delete_client"),

    path("statistics/", StatisticsView.as_view(), name="statistics"),
]
