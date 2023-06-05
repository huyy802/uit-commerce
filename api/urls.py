from django.urls import path
from .views import auth, item, shop
urlpatterns = [
    # Region create auth routers
    path('auth/create_user', auth.create_user, name='create_user'),
    path('auth/login_user', auth.login_user, name='login_user'),
    path('auth/update_user/<str:id>', auth.update_user, name='update_user'),

    # Region create item routers
    path('items/create_item', item.create_item, name='create_item'),
    path('items/update_item', item.update_item, name='update_item'),
    path('items/delete_item/<str:id>', item.delete_item, name='delete_item'),

    # Region create shop routers
    path('shops/create_shop', shop.create_shop, name='create_shop'),
    path('shops/login_shop', shop.login_shop, name='login_shop'),
    path('shops/update_shop', shop.update_shop, name='update_shop'),
    path('shops/delete_shop/<str:id>', shop.delete_shop, name='delete_shop'),

]
