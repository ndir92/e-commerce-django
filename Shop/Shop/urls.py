
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from Shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/',views.Master,name='master'),
    path('',views.Index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    #add cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
#addcontact
    path('contact_us/',views.Contact_Page,name='contact_page'),
    #Checkout
    path('checkout/',views.CheckOut,name="checkout"),
    #order
    path('order/',views.Your_Order,name="order"),

#produc_page
    path('product/',views.Product_Page,name='product_page'),

#produc_detail
   path('product/<str:id>',views.Product_Detail, name='product_detail'),

   path('search/', views.Search, name='search'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
