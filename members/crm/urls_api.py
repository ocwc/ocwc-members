from django.conf.urls import url

from .views import (
    address_geo_list_view,
    country_list_view,
    OrganizationByCountryListViewApi,
    organization_group_by_membership_view,
    OrganizationViewApi,
    OrganizationRssFeedsApi,
    organization_group_by_consortium_view,
    OrganizationListViewApi,
)

app_name = "crmapi"
urlpatterns = [
    url(r"^address/list/geo/$", address_geo_list_view, name="address-list-geo"),
    url(
        r"^address/list/geo/consortium/(?P<consortium>[\w|\W]+)/$",
        address_geo_list_view,
        name="address-list-geo",
    ),
    url(r"^country/list/$", country_list_view, name="country-list"),
    url(
        r"^organization/view/(?P<pk>\d+)/$",
        OrganizationViewApi.as_view(),
        name="organization-view",
    ),
    url(
        r"^organization/list/$",
        OrganizationListViewApi.as_view(),
        name="organization-by_country-list",
    ),
    url(
        r"^organization/by_country/(?P<country>[\w|\W]+)/list/$",
        OrganizationByCountryListViewApi.as_view(lookup_field="country"),
        name="organization-by_country-list",
    ),
    url(
        r"^organization/group_by/membership_type/list/$",
        organization_group_by_membership_view,
        name="organization-group_by_membership_type-list",
    ),
    url(
        r"^organization/group_by/consortium/(?P<consortium>[\w|\W]+)/list/$",
        organization_group_by_consortium_view,
        name="organization-group_by_membership_type-list",
    ),
    url(
        r"^organization/feeds/$",
        OrganizationRssFeedsApi.as_view(),
        name="organization-feeds",
    ),
]
