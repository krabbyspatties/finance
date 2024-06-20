from django.urls import path
from . import views

urlpatterns = [
    path('account', views.index_account),
    path('account/create', views.create_account),
    path('account/store', views.store_account),
    path('account/transaction/<int:account_id>/', views.create_transaction),
    path('account/save_transaction/<int:account_id>', views.save_transaction),
    path('account/delete/<int:account_id>', views.delete_account)
]
