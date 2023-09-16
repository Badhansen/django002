I tried this book for learning and developing my skills (**Django for APIs 3.1**) thanks William S. Vincent for this awesome book.

![](https://github.com/Badhansen/django002/blob/master/images/books.jpg)

To contribute or run this project, follow the steps below:
### 1. Clone the repository

```
git clone https://github.com/Badhansen/django001.git
```

### 2. Create your own virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Virtual environments are where dependencies are stored, similar to `node_modules` in JavaScript. Every time you start your machine, you must activate the virtual environment using `source venv/bin/activate`.

*Here are some useful links that I used to create this project*
- [Install pyenv](https://opensource.com/article/19/5/python-3-default-mac) alternative to `venv` Virtual Environments.
- [Managing pyenv, virtualenv, and pyenv-virtualenv](https://gist.github.com/Badhansen/19100e5548ef154360361ab7f45c183f), this link help me a lot managing all environment and django projects.
- [Interested in pyenv read this as well](https://realpython.com/intro-to-pyenv/)



### 3. Install your requirements

```
pip install -r requirements.txt
```

This will install all the necessary dependencies for the project.

## Development

Before the development and running phase, please go to any of the projects and start the server by running:

```bash
python manage.py runserver
```

Remember to activate the virtual environment (`source venv/bin/activate`) or if you are using pyenv (`pyenv activate vname`) every time you work on the project to ensure you're using the correct Python version and dependencies.

## Contribution

If you wish to contribute to this project, please create a new branch and submit a pull request with your changes. We welcome contributions from the community!

###############################################################
---
# Understanding Web Development Concepts

This README provides an overview of important concepts related to web development, including URLs, the Internet Protocol Suite, HTTP, REST, and API Schema.

## URL (Uniform Resource Locator)

A URL is the address of a resource on the internet. It typically consists of three parts:
- Scheme: Specifies how to access the resource (e.g., `https`)
- Hostname: The actual name of the site (e.g., `www.google.com`)
- Path (Optional): The specific path to a resource on the server (e.g., `/about/`)

## Internet Protocol Suite

The Internet Protocol Suite consists of a set of protocols used for communication on the internet. Key components include:
- DNS (Domain Name System): Translates domain names into IP addresses.
- TCP (Transmission Control Protocol): Provides reliable, ordered, and error-checked data delivery.
- HTTP (Hypertext Transfer Protocol): Facilitates communication between client and server over the internet.

## HTTP Verbs

HTTP verbs are actions that can be performed on web resources. Common HTTP verbs include GET, POST, PUT, and DELETE.

## Endpoints

Web APIs have endpoints, which are URLs with available actions (HTTP verbs) that expose data. An endpoint returning multiple data resources is known as a collection.

## HTTP

HTTP is a request-response protocol between a client and a server. It consists of a request/status line, headers, and an optional body. Responses include status codes indicating success, redirection, client errors, or server errors.

## Status Codes

HTTP status codes are categorized into:
- 2xx: Success
- 3xx: Redirection
- 4xx: Client Error
- 5xx: Server Error

## REST (REpresentational State Transfer)

REST is an approach to building web APIs that is:
- Stateless
- Supports common HTTP verbs
- Returns data in formats like JSON or XML

## API Schema and Documentation

A schema is a machine-readable document outlining all API endpoints, URLs, and supported HTTP verbs. Proper documentation is crucial for API developers and consumers.

---

By understanding these concepts, you'll be better equipped to work with web development technologies and build effective web applications and APIs.

# Django Rest Framework (DRF) Overview

Django Rest Framework (DRF) is a powerful toolkit for building Web APIs using Django. Unlike traditional Django applications that serve web pages, DRF focuses on creating APIs that return data in JSON format. This README provides an overview of key concepts related to DRF.

## Getting Started

To create a RESTful API using DRF, follow these three main steps:

1. **URL Routing**: Define URL routes in a `urls.py` file to map API endpoints to specific views.

2. **Serializers**: Use a `serializers.py` file to transform data into JSON format. Serializers are crucial for formatting data for API endpoints.

3. **Views**: Create views in a `views.py` file to apply logic to each API endpoint. Views handle data retrieval, processing, and responding to HTTP requests.

## Serializers

Serializers are essential for translating data into a format that is easy to consume over the internet, typically in JSON. Key points about serializers:

- Always add a `__str__` method to provide a human-readable name for each model instance.
- Serializers help in displaying data at API endpoints.

## Migration Files

Migration files are crucial for debugging applications and maintaining a structured database. To keep migrations manageable:

- Create a migration file for each small change.
- Avoid mixing migrations from different apps to simplify debugging.

## CORS (Cross-Origin Resource Sharing)

CORS is necessary when a client interacts with an API hosted on a different domain or port. DRF recommends using the `django-cors-headers` middleware to handle CORS. Follow these steps:

1. Add `corsheaders` to the `INSTALLED_APPS`.

2. Include `CorsMiddleware` above `CommonMiddleware` in the `MIDDLEWARE` setting.

3. Create a `CORS_ORIGIN_WHITELIST` to specify allowed domains.

**Note:** Ensure that `corsheaders.middleware.CorsMiddleware` appears above `django.middleware.common.CommonMiddleware` in the `MIDDLEWARE` setting.

## Permissions

DRF provides several out-of-the-box permissions settings to secure your API. These permissions can be applied at project-level, view-level, or individual model-level. Some common project-level permissions include:

- `AllowAny`: Allows any user, authenticated or not, full access.
- `IsAuthenticated`: Requires users to be authenticated for access.
- `IsAdminUser`: Limits access to admin/superusers.
- `IsAuthenticatedOrReadOnly`: Allows unauthorized users to view, but only authenticated users can write, edit, or delete.

To implement these permissions, update the `DEFAULT_PERMISSION_CLASSES` setting in `settings.py`.

**Note:** Requests with HTTP verbs in `SAFE_METHODS` (GET, OPTIONS, HEAD) are considered read-only, granting permission by default.

## Adding Login to Browsable API

To simplify login in the browsable API, add the following URL route to your project-level `urls.py`:

```python
path('api-auth/', include('rest_framework.urls'))
```

# User Authentication and Authorization in Django REST Framework (DRF)

This README provides an overview of user authentication and authorization concepts in Django REST Framework (DRF) and different authentication methods.

## Authentication Overview

Authentication is the process by which a user can register for a new account, log in with it, and log out. DRF supports various authentication methods, each with its pros and cons.

### Basic Authentication

- **Description**: Basic Authentication is a common form of HTTP authentication. It requires clients to send approved authentication credentials with each request.
- **Pros**: Simplicity, widely supported.
- **Cons**: Inefficient as the server must verify credentials on every request. Credentials are sent unencrypted, so it should only be used with HTTPS.

### Session Authentication

- **Description**: Session Authentication is stateful. The client logs in with credentials and receives a session ID (stored as a cookie) for future requests.
- **Pros**: Credentials sent only once, efficient, and supports session-based login.
- **Cons**: Limited to a single browser session, not suitable for multiple domains or APIs with multiple front-ends.

### Token Authentication

- **Description**: Token Authentication is stateless. A unique token is generated and stored by the client after initial authentication. Tokens are passed in headers for each request.
- **Pros**: Scalable, supports multiple front-ends, and efficient.
- **Cons**: Token size can become a performance issue. Store tokens securely in cookies or local storage to prevent XSS attacks.

### JSON Web Tokens (JWTs)

- **Description**: JWTs are an enhanced version of tokens with benefits like token expiration and encryption. They can be added to DRF via third-party packages.
- **Pros**: Enhanced features, safer over unsecured HTTP.
- **Cons**: Tokens can become large, store securely.

## Default Authentication in DRF

By default, DRF uses both Session Authentication and Basic Authentication. Session Authentication powers the Browsable API and login/logout functionality. Basic Authentication is used to pass the session ID in the HTTP headers for the API itself.

## Implementing Token Authentication

To implement Token Authentication, update the `DEFAULT_AUTHENTICATION_CLASSES` setting in `settings.py`:
```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```

# Viewsets and Routers in Django REST Framework (DRF)

This README provides an overview of Viewsets and Routers, powerful tools within Django REST Framework (DRF) that streamline API development by combining related views and automatically generating URL patterns.

## Viewsets

A Viewset is a mechanism in DRF that allows you to group the logic for multiple related views into a single class. This abstraction simplifies API development and reduces code redundancy.

### Example User Viewset

```python
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
```
