from django.urls import path,include
from homeapp import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('About-Us',views.aboutpage,name='aboutpage'),
     path('Patna-property',views.patnapage,name='patnapage'),
     path('biharsharif-property',views.biharpage,name='biharpage'),
     path('service',views.servicepage,name='servicepage'),
     path('technology',views.technologypage,name='technologypage'),
     path('career',views.careerpage,name='careerpage'),
     path('contact-us',views.contactpage,name='contactpage'),
     path('modal-submit',views.modal_submitpage,name='modal_submitpage'),
     path('bihar-property_contact',views.bihar_property_contactpage,name='bihar_property_contactpage'),
     path('patna-property_contact',views.patna_property_contactpage,name='patna_property_contactpage'),
]