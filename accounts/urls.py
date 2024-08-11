from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView




urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    # path('destinations', views.destinations, name='destinations')
    path('user_dashboard', views.user_dashboard, name='user_dashboard'),
    
    
    path('template', views.template, name='template'),
    
    path('dhaka_hotel', views.dhaka_hotel, name='dhaka_hotel'),
    path('dhaka_restaurant', views.dhaka_restaurant, name='dhaka_restaurant'),
    
    path('chittagong_hotel', views.chittagong_hotel, name='chittagong_hotel'),
    path('chittagong_bus', views.chittagong_bus, name='chittagong_bus'),
    path('chittagong_restaurant', views.chittagong_restaurant, name='chittagong_restaurant'),
    
    
    path('cosx_bazar_hotel', views.cosx_bazar_hotel, name='cosx_bazar_hotel'),
    path('cosx_bazar_bus', views.cosx_bazar_bus, name='cosx_bazar_bus'),
    path('cosx_bazar_restaurant', views.cosx_bazar_restaurant, name='cosx_bazar_restaurant'),
    
    path('barishal_hotel', views.barishal_hotel, name='barishal_hotel'),
    path('barishal_bus', views.barishal_bus, name='barishal_bus'),
    path('barishal_restaurant', views.cosx_bazar_restaurant, name='barishal_restaurant'),
    
    
    path('bandarban_hotel', views.bandarban_hotel, name='bandarban_hotel'),
    path('bandarban_bus', views.bandarban_bus, name='bandarban_bus'),
    path('bandarban_restaurant', views.bandarban_restaurant, name='bandarban_restaurant'),
    
    path('bogura_hotel', views.bogura_hotel, name='bogura_hotel'),
    path('bogura_bus', views.bogura_bus, name='bogura_bus'),
    path('bogura_restaurant', views.bogura_restaurant, name='bogura_restaurant'),
    
    path('jessore_hotel', views.jessore_hotel, name='jessore_hotel'),
    path('jessore_bus', views.jessore_bus, name='jessore_bus'),
    path('jessore_restaurant', views.jessore_restaurant, name='jessore_restaurant'),
    
    path('khulna_hotel', views.khulna_hotel, name='khulna_hotel'),
    path('khulna_bus', views.khulna_bus, name='khulna_bus'),
    path('khulna_restaurant', views.khulna_restaurant, name='khulna_restaurant'),
    
    path('rajshahi_hotel', views.rajshahi_hotel, name='rajshahi_hotel'),
    path('rajshahi_bus', views.rajshahi_bus, name='rajshahi_bus'),
    path('rajshahi_restaurant', views.rajshahi_restaurant, name='rajshahi_restaurant'),
    
    path('mouluvibazar_hotel', views.mouluvibazar_hotel, name='mouluvibazar_hotel'),
    path('mouluvibazar_bus', views.mouluvibazar_bus, name='mouluvibazar_bus'),
    path('mouluvibazar_restaurant', views.mouluvibazar_restaurant, name='mouluvibazar_restaurant'),
    
    path('rangamati_hotel', views.rangamati_hotel, name='rangamati_hotel'),
    path('rangamati_bus', views.rangamati_bus, name='rangamati_bus'),
    path('rangamati_restaurant', views.rangamati_restaurant, name='rangamati_restaurant'),
    
    path('rangpur_hotel', views.rangpur_hotel, name='rangpur_hotel'),
    path('rangpur_bus', views.rangpur_bus, name='rangpur_bus'),
    path('rangpur_restaurant', views.rangpur_restaurant, name='rangpur_restaurant'),
    
    path('sylhet_hotel', views.sylhet_hotel, name='sylhet_hotel'),
    path('sylhet_bus', views.sylhet_bus, name='sylhet_bus'),
    path('sylhet_restaurant', views.sylhet_restaurant, name='sylhet_restaurant'),
   

   # path('index/', views.index, name='index'),
    path('dhaka/', views.dhaka, name='dhaka'),
    path('chittagong/', views.chittagong, name='chittagong'),
    path('barishal/', views.barishal, name='barishal'),
    path('coxs_bazar/', views.coxs_bazar, name='coxs_bazar'),
    path('bandarban/', views.bandarban, name='bandarban'),
    path('bogura/', views.bogura, name='bogura'),
    path('jessore/', views.jessore, name='jessore'),
    path('khulna/', views.khulna, name='khulna'),
    path('rajshahi/', views.rajshahi, name='rajshahi'),
    path('mouluvibazar/', views.mouluvibazar, name='mouluvibazar'),
    path('rangamati/', views.rangamati, name='rangamati'),
    path('rangpur/', views.rangpur, name='rangpur'),
    path('sylhet/', views.sylhet, name='sylhet'),
    
    
    
    
    

    
    
    # path('add-to-wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    # path('wishlist/', views.view_wishlist, name='wishlist'),
    # path('accounts/wishlist/', TemplateView.as_view(template_name='wishlist.html'), name='wishlist'),

    
    # path('add_bookmark/<int:row_id>/', views.add_bookmark, name='add_bookmark'),
    # path('remove_bookmark/<int:row_id>/', views.remove_bookmark, name='remove_bookmark'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    # path('show_data/', views.show_data, name='show_data'),
     path('add_favorite/', views.add_favorite, name='add_favorite'),
     path('remove_favorite/', views.remove_favorite, name='remove_favorite'),
     
     
     
     
   

    

   #forgot password
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
