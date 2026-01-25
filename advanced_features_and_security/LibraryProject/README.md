# Advanced Features and Security - Django Project

## Overview
This Django project demonstrates advanced features including:

1. **Custom User Model**: A user model with additional fields:
   - `date_of_birth` (DateField)
   - `profile_photo` (ImageField)

2. **Permissions and Groups**: Custom permissions and groups to control access:
   - Permissions: `can_view`, `can_create`, `can_edit`, `can_delete`
   - Groups: `Admins`, `Editors`, `Viewers`
   - Enforced via `@permission_required` decorators in views.

3. **Security Best Practices**: Includes settings to enhance security:
   - CSRF protection, secure cookies
   - HTTPS and secure redirects
   - XSS, clickjacking, and content-type protections

## Project Structure




## Custom User Model

- Location: `bookshelf/models.py`
- Class: `CustomUser`
- Manager: `CustomUserManager`
- Fields: `username`, `email`, `date_of_birth`, `profile_photo`, plus standard Django fields

## Permissions and Groups

- Defined in `Book` model (or other models as needed)
- Groups:
  - **Admins**: all permissions
  - **Editors**: can_create, can_edit
  - **Viewers**: can_view

- Enforced in views using `@permission_required('bookshelf.can_edit', raise_exception=True)`

## Security Settings

- `DEBUG=False` in production
- `SECURE_SSL_REDIRECT=True`
- `SESSION_COOKIE_SECURE=True`, `CSRF_COOKIE_SECURE=True`
- `X_FRAME_OPTIONS='DENY'`
- `SECURE_CONTENT_TYPE_NOSNIFF=True`
- `SECURE_BROWSER_XSS_FILTER=True`

## Setup Instructions

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
