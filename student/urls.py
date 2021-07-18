from django.urls import path
from student import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('home', views.student_home_view),
path('login', LoginView.as_view(template_name='student/studentlogin.html'),name='studentlogin'),
path('signup', views.student_signup_view,name='studentsignup'),
path('dashboard', views.student_dashboard_view,name='student-dashboard'),
path('exam', views.student_exam_view,name='student-exam'),
path('take-exam/<int:pk>', views.take_exam_view,name='take-exam'),
path('start-exam/<int:pk>', views.start_exam_view,name='start-exam'),

path('calculate-marks', views.calculate_marks_view,name='calculate-marks'),
path('view-result', views.view_result_view,name='view-result'),
path('check-marks/<int:pk>', views.check_marks_view,name='check-marks'),
path('marks', views.student_marks_view,name='student-marks'),
]