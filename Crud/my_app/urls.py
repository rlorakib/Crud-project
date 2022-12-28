from django.urls import path
from my_app import views

app_name = 'first_app'

urlpatterns = [
   path('', views.index, name='index'),
   path('students/', views.students, name='students'),
   path('student_info/<int:student_id>/', views.student_info, name='student_info'),
   path('student_update/<int:x_id>/', views.student_update, name='student_update'),
   path('student_delete/<int:x_id>/', views.student_delete, name='student_delete'),
]
