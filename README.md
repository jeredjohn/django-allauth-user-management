# django-allauth-user-management

1: Settings:

SECRET_KEY, EMAIL_HOST_USER and EMAIL_HOST_PASSWORD have been set with
environment variables, so you will have to set those to your own.

2: Install and activate virtual environment

3: pip install -r requirements.txt

4: python manage.py makemigrations

5: python manage.py migrate

6: python manage.py runserver

That's it!

Users must verify email before signing in. To allow users to sign in without
verification comment out ACCOUNT_EMAIL_VERIFICATION = "mandatory" in settings.

Users may sign in with username, email, or phone.

Once signed in, there is a link to "Account" where users can manage their
information.
 
