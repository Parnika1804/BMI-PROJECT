from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# View for Signup
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_dashboard')  # Redirect to user dashboard after signup
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# View for Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_dashboard')  # Redirect to user dashboard after login
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# View for Logout
def logout_view(request):
    logout(request)
    return redirect('login')
# View for the Index (Home) page
def index_view(request):
    return render(request, 'accounts/index.html')

# View for User Dashboard (Page1)
def user_dashboard(request):
    return render(request, 'accounts/page1.html')  # Update with the template you want

def mentor_directory(request):
    # You can fetch mentor data from a database or define it statically
    mentors = [
        {
            'name': 'Sarah Lee',
            'domain': 'Mental Wellness',
            'details': 'Specializing in stress management, mindfulness, and mental wellness.',
            'full_name': 'Dr. Sarah Lee',
            'college': 'Harvard University',
            'experience': '10+ years of experience in counseling and coaching',
            'sbt': 'SBTs: Stress Management Bootcamp, Mindfulness Retreat',
            'feedback': 'Rating: 4.8/5',
            'waiting_time': 5,
            'image_url': 'mentor1.jpg',
        },
        {
            'name': 'John Doe',
            'domain': 'Life Coaching',
            'details': 'Expert in career growth, personal development, and life balance.',
            'full_name': 'John Doe',
            'college': 'Stanford University',
            'experience': '8 years as a certified life coach',
            'sbt': 'SBTs: Life Coaching Workshop, Leadership Training',
            'feedback': 'Rating: 4.5/5',
            'waiting_time': 10,
            'image_url': 'mentor2.jpg',
        },
        {
            'name': 'Emma Watson',
            'domain': 'Financial Advice',
            'details': 'Guiding women towards financial independence with actionable tips on budgeting, saving, and investing.',
            'full_name': 'Emma Watson',
            'college': 'Oxford University',
            'experience': '12 years in financial planning',
            'sbt': 'SBTs: Investment Bootcamp, Financial Independence Training',
            'feedback': 'Rating: 4.9/5',
            'waiting_time': 3,
            'image_url': 'mentor3.jpg',
        },
        {
            'name': 'Michael Brown',
            'domain': 'Career Guidance',
            'details': 'Providing mentorship on navigating career paths, improving skills, and securing job opportunities.',
            'full_name': 'Michael Brown',
            'college': 'MIT',
            'experience': '15+ years as a career coach',
            'sbt': 'SBTs: Career Growth Workshops, Skill Building Bootcamp',
            'feedback': 'Rating: 5/5',
            'waiting_time': 8,
            'image_url': 'mentor4.jpg',
        },
    ]

    return render(request, 'accounts/mentor-directory.html')

@login_required
def chat_view(request):
    return render(request, 'accounts/chat.html')
def report(request):
    # You may pass context here, if needed
    return render(request, 'accounts/report.html')


def fat_percentage_estimator(request):
    # Handle the fat percentage estimator view
     return render(request, 'accounts/fat-percentage-estimator.html')

def health_risks(request):
    # Handle the health risks view
    return render(request, 'accounts/health-risks.html')

def your_nutrition_plan(request):
    # Handle the nutrition plan view
    return render(request, 'accounts/your-nutrition-plan.html')

def next_steps(request):
    # Handle the next steps view
    return render(request, 'accounts/next-steps.html')

def resource_library(request):
    # Handle the resource library view
    return render(request, 'accounts/resource-library.html')
def mentor_registration(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        university = request.POST.get('university')
        year = request.POST.get('year')
        experience = request.POST.get('experience')

        # For now, just returning the data as a response
        # You can replace this with actual saving to database logic
        return HttpResponse(f"Mentor Registered! <br> Name: {name} <br> Email: {email} <br> University: {university} <br> Year: {year} <br> Experience: {experience}")
    
    return render(request, 'accounts/mentor_registration.html')
def sbt_leaderboard(request):
    return render(request,'accounts/sbt-leaderboard.html')