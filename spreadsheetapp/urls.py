# from django.urls import path
# from .views import save_spreadsheet, load_spreadsheet
#
# urlpatterns = [
#     path('api/save/', save_spreadsheet, name='save_spreadsheet'),
#     path('api/load/<str:name>/', load_spreadsheet, name='load_spreadsheet'),
# ]
# from django.urls import path
# from .views import save_spreadsheet, load_spreadsheet
#
# urlpatterns = [
#     path('api/save/', save_spreadsheet, name='save_spreadsheet'),
#     path('api/load/<str:name>/', load_spreadsheet, name='load_spreadsheet'),
# ]
# from django.urls import path
# from .views import save_spreadsheet, load_spreadsheet
#
# urlpatterns = [
#     path('save/', save_spreadsheet, name='save_spreadsheet'),
#     path('load/<str:name>/', load_spreadsheet, name='load_spreadsheet'),
# ]
# from django.urls import path
# from .views import save_spreadsheet, load_spreadsheet
# from django.http import JsonResponse  # For API home response
#
# # def api_home(request):
# #     return JsonResponse({"message": "Welcome to the Spreadsheet API!"})
#
# urlpatterns = [
#     # path("", api_home, name="api_home"),  # ✅ Default `/api/` route
#     path("save/", save_spreadsheet, name="save_spreadsheet"),
#     path("load/<str:name>/", load_spreadsheet, name="load_spreadsheet"),
# ]
from django.urls import path
from .views import save_spreadsheet, load_spreadsheet, index,perform_operation

urlpatterns = [
    path('', index, name='index'),  # Home page with the spreadsheet UI
    path('save/', save_spreadsheet, name='save_spreadsheet'),  # Save spreadsheet
    path('load/<int:id>/', load_spreadsheet, name='load_spreadsheet'),  # Load spreadsheet
    path('operation/', perform_operation, name='perform_operation'),
    # # Calculation functions
    # path('<int:id>/sum/', calculate_sum, name='calculate_sum'),
    # path('<int:id>/average/', calculate_average, name='calculate_average'),
    # path('<int:id>/max/', calculate_max, name='calculate_max'),
    # path('<int:id>/min/', calculate_min, name='calculate_min'),
    # path('<int:id>/count/', calculate_count, name='calculate_count'),
]
