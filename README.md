# Django Blogs

A simple Django + Django REST Framework blogging application with custom user
authentication. The project demonstrates basic CRUD operations for blog posts
as well as a custom user model and registration endpoints.

## Features

- Custom `CustomNewUser` model with email-based authentication
- JWT authentication for protected API routes using `djangorestframework-simplejwt`
- RESTful endpoints for creating, listing, updating, and deleting blog posts
- Admin interface configured for the blog and user models

## Refactoring Notes (March 2026)

To make the codebase more idiomatic and maintainable the following changes were
applied:

1. **Model renaming**: `My_blogs` model was renamed to `Blog`.
   - Existing migration files still refer to the old model name. After pulling
     these updates you should create a new migration to rename the table:
     ```bash
     python manage.py makemigrations myApp
     # It will generate a `RenameModel` operation.
     python manage.py migrate
     ```
2. **View refactor**: replaced function-based views with a DRF `ModelViewSet` + router for the blog API.
3. **Serializer cleanup**: aligned names and removed unused imports.
4. **URL configuration**: switched to a router-based approach to simplify
   routing and improve REST compliance.
5. **accounts improvements**: added permission checks, fixed misspellings, and
   cleaned imports.
6. **PEP8 and style fixes**: removed unused imports, added docstrings, and
   streamlined code readability.

> 🔧 Remember to run `makemigrations` after renaming models or changing
> field definitions. Because the existing migrations were created with the old
> model name, you may want to squash migrations or manually edit them in a
> production setting.

## Installation & Setup

### Running the test suite

There is a very small skeleton of tests in `myApp/tests.py`. Once the
dependencies are installed and migrations have been applied you can run the
full Django test suite with:

```bash
python manage.py test
```

There are no tests included in the repository—feel free to add your own as needed.

## Installation & Setup

1. **Clone the repository**:

   ```bash
   git clone <repo-url> django-blogs
   cd django-blogs
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate # Unix/macOS
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure settings**:
   - Ensure `AUTH_USER_MODEL = 'accounts.CustomNewUser'` is set in
     `myBlog/settings.py`.
   - Update database settings if not using SQLite.

5. **Run migrations and create superuser**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

| Path           | Method | Description                       |
| -------------- | ------ | --------------------------------- |
| `/blogs/`      | GET    | List all blogs                    |
| `/blogs/`      | POST   | Create a new blog (authenticated) |
| `/blogs/{id}/` | GET    | Retrieve blog by ID               |
| `/blogs/{id}/` | PUT    | Update blog (authenticated)       |
| `/blogs/{id}/` | DELETE | Delete blog (authenticated)       |

Authentication is handled via JWT; obtain tokens using the standard
`/api/token/` and `/api/token/refresh/` endpoints provided by
`rest_framework_simplejwt` (add to your root URL configuration if not present).

## Further Improvements

- Add comprehensive test coverage for models, serializers, and views.
- Implement pagination, filtering, and search for the blog list.
- Associate blog posts with their creators and enforce ownership rules.
- Apply `pre-commit` hooks or linters for consistent style.

---
