# flet-pyrebase-wrapper
Experimenting with using Firebase with Flet

I'm probably looking to turn this wrapper into a more robust solution,
but for now it has met my needs for creating a Flet application with a 
Firebase backend including auth and database.

The primary reason for being unable to simply use pyrebase out of the
box was the need to persist authentication to different routes. Presently,
Flet docs say it only provides OAuth2 with its auth component. Devs are left
to their own devices otherwise.
