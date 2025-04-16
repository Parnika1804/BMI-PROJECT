from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.index_view, name='index'),
    path('page1/', views.user_dashboard, name='page1'),  # Corrected name for page1
    path('mentor_directory/', views.mentor_directory, name='mentor_directory'),  # Updated as 'mentor-directory'
    path('chat/', views.chat_view, name='chat'),
    path('report/', views.report, name='report'),
    path('fat-percentage-estimator/', views.fat_percentage_estimator, name='fat-percentage-estimator'),
    path('health-risks/', views.health_risks, name='health-risks'),
    path('your-nutrition-plan/', views.your_nutrition_plan, name='your-nutrition-plan'),
    path('next-steps/', views.next_steps, name='next-steps'),
    path('resource-library/', views.resource_library, name='resource-library'),
    path('mentor-registration/', views.mentor_registration, name='mentor_registration'),
    path('sbt-leaderboard/',views.sbt_leaderboard, name = "sbt-leaderboard"),
]
