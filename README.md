# Tennis Members Club (Django)

A small Django web app for a tennis club with a public home page, authentication (signup/login/logout), a protected members directory with photos, and a join-the-club form.

## Features
- Home page with quote and CTAs
- Authentication: Signup, Login, Logout
- Protected pages:
  - Members listing as flip-cards with photos
  - Join form that stores join requests
- Contact page
- Media handling for member photos (served in development)
- Bootstrap 5 styling with a shared, auth-aware navbar

## Tech Stack
- Python 3.x, Django 5.2
- Pillow (image handling for `ImageField`)
- Bootstrap 5 (CDN)
- requests (for fetching a quote; optional)

## Project Structure (high-level)
```
my_tennis_club/
├─ manage.py
├─ db.sqlite3
├─ my_tennis_club/
│  ├─ settings.py      # Media + auth redirect settings
│  ├─ urls.py          # Routes app URLs; serves media when DEBUG=True
│  └─ ...
├─ members/
│  ├─ models.py        # Member, JoinRequest
│  ├─ forms.py         # JoinRequestForm validation
│  ├─ views.py         # home, members, join, join_thanks, contact, signup, logout_view
│  ├─ urls.py          # App routes
│  └─ templates/
│     ├─ navbar.html
│     ├─ home.html
│     ├─ myFirstPage.html
│     ├─ join.html
│     ├─ join_thanks.html
│     ├─ contact.html
│     ├─ login.html
│     └─ signup.html
└─ media/              # Uploaded member photos (created at runtime)
```


### 1) Create and activate an environment
- Using venv (built-in):
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```
- Or using conda:
```powershell
conda create -n jango python=3.11 -y
conda activate jango
```

### 2) Install dependencies
```powershell
pip install django==5.2 pillow requests
```
(Optional) Save them:
```powershell
pip freeze > requirements.txt
```

### 3) Database migrations and admin user
```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4) Run the server
```powershell
python manage.py runserver
```
Open http://127.0.0.1:8000 in your browser.

## Environment & Settings
In `my_tennis_club/settings.py`:
- Development media:
  ```python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / 'media'
  ```
- Auth redirects:
  ```python
  LOGIN_URL = 'login'
  LOGIN_REDIRECT_URL = 'home'
  LOGOUT_REDIRECT_URL = 'home'
  ```
- Keep `DEBUG=True` for development so Django serves media locally.

## Routes
- `/` → Home (public)
- `/members/` → Members list (login required)
- `/join/` → Join form (login required)
- `/join/thanks/` → Thank-you page
- `/contact/` → Contact (public)
- `/signup/` → Create account (public)
- `/login/` → Login (public; redirects if already authenticated)
- `/logout/` → Logout (GET/POST; redirects to home with a message)

## Data Model (brief)
- `Member`: `firstname`, `lastname`, `email`, `phone`, `join_date`, `age`, `photo`
- `JoinRequest`: `firstname`, `lastname`, `email`, `phone (optional)`, `message`, `created_at`

## Media (Member Photos)
- Uploads go under `media/member_photos/`.
- In development (DEBUG=True), media is served via the `static()` helper in `urls.py`.
- Templates prefer `member.photo.url` when present; otherwise a fallback avatar can be used.

## Common Tasks
- Open Django admin: http://127.0.0.1:8000/admin/
- Create initial data via admin or fixtures.
- Dump fixtures (optional):
```powershell
python manage.py dumpdata members.Member --indent 2 > seed_members.json
python manage.py dumpdata members.JoinRequest --indent 2 > seed_join_requests.json
```
- Load fixtures:
```powershell
python manage.py loaddata seed_members.json
python manage.py loaddata seed_join_requests.json
```

## Git Tips
Create a `.gitignore` before your first commit to avoid committing local DB/media:
```gitignore
# Byte-compiled / cache
__pycache__/
*.py[cod]
*.egg-info/

# OS junk
.DS_Store
Thumbs.db

# Django / site data
db.sqlite3
*.sqlite3
media/
staticfiles/

# Envs / secrets
.env
.env.*
.venv/
venv/

# Editors
.vscode/
.idea/
```
Commit the database only if you really want to share local data; otherwise prefer fixtures as shown above.

## Troubleshooting
- Media not showing: Ensure `DEBUG=True` in dev, and check that `<img src="/media/...">` resolves.
- Logout 405: This app uses a custom logout view that accepts GET/POST; if you switch back to Django’s `LogoutView`, use POST.
- Form errors: Ensure custom `clean_*` methods return their values and that your inputs meet validation rules.

## Next Steps / Enhancements
- Member detail pages with slugs
- Search, filters, pagination for members
- Email notifications on new join requests
- Move inline CSS to static files and add a build step if needed
- Unit tests for forms and views
