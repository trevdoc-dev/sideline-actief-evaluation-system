## **Overview**

This guide provides a step-by-step process to set up a Django project, create a main page, login page, and edit profile page, and configure the application for proper functionality.

---

## **Prerequisites**

1. **Python**: Ensure Python (3.8 or higher) is installed. [Download Python](https://www.python.org/downloads/)
2. **Pip**: Comes pre-installed with Python.
3. **Virtual Environment Tool**: Use `venv` or an equivalent.

---

## **Installation Steps**

### **1. Set Up a Virtual Environment**

```bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
# Windows
env\Scripts\activate

# macOS/Linux
source env/bin/activate
```

---

### **2. Install Django**

```bash
pip install django
```

---

### **3. Create a Django Project**

```bash
django-admin startproject django_project
cd django_project
```

---

### **4. Create an App**

```bash
python manage.py startapp main_app
```

Add `main_app` to the `INSTALLED_APPS` list in `django_project/settings.py`.

---

### **5. Configure the URLs**

In `django_project/urls.py`, include the app’s URLs:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),  # Include app URLs
]
```

Create a `urls.py` in the `main_app` folder:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('login/', views.login_view, name='login'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]
```

---

### **6. Create Views**

In `main_app/views.py`:

```python
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Main Page
def main_page(request):
    return render(request, 'main_app/main.html')

# Login Page
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('edit_profile')
        else:
            return render(request, 'main_app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'main_app/login.html')

# Edit Profile Page
@login_required
def edit_profile(request):
    if request.method == 'POST':
        request.user.email = request.POST['email']
        request.user.save()
        return redirect('main_page')
    return render(request, 'main_app/edit_profile.html', {'user': request.user})
```

---

### **7. Create Templates**

In `main_app/templates/main_app/`, create the following HTML files:

**`main.html`**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Main Page</title>
  </head>
  <body>
    <h1>Welcome to the Main Page!</h1>
    <a href="/login/">Login</a>
  </body>
</html>
```

**`login.html`**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Login</title>
  </head>
  <body>
    <h1>Login Page</h1>
    {% if error %}
    <p style="color: red;">{{ error }}</p>
    {% endif %}
    <form method="post">
      {% csrf_token %}
      <input type="text" name="username" placeholder="Username" required />
      <input type="password" name="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
  </body>
</html>
```

**`edit_profile.html`**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Edit Profile</title>
  </head>
  <body>
    <h1>Edit Profile</h1>
    <form method="post">
      {% csrf_token %}
      <input type="email" name="email" value="{{ user.email }}" required />
      <button type="submit">Save</button>
    </form>
  </body>
</html>
```

---

### **8. Set Up the Database**

1. **Use SQLite (default) or MySQL.**  
   To switch to MySQL, update `django_project/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'database_name',
           'USER': 'username',
           'PASSWORD': 'password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```
2. Install the MySQL client:
   ```bash
   pip install mysqlclient
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

---

### **9. Run the Server**

```bash
python manage.py runserver
```

Visit the following pages:

- **Main Page**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Login Page**: [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)
- **Edit Profile Page**: Accessible after login.

---

## **Features**

1. **Main Page**: A simple welcome page with a link to the login page.
2. **Login Page**: Authenticates users using Django's `User` model.
3. **Edit Profile Page**: Allows logged-in users to update their email.

---

## **Next Steps**

- Add CSS for styling to enhance the look and feel.
- Implement unit tests for key functionalities.
- Expand features like user registration, password reset, etc.

Enjoy your Django application! 🎉
