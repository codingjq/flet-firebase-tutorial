# Flet Firebase Tutorial
A notes application with Registration, Authentication, and Realtime CRUD that leverages the speed
and utility of both Flet and Firebase.

## Explainer video to be posted on [CodingJQ](https://youtube.com/@codingjq)

I used a wrapper around Pyrebase4 to abstract handling my data away from the views.

I used a Router that I designed in a previous tutorial. Stand by for a new Router that passes information
more efficiently from page to page.

I used a UserControl to build each Note to show how to build a custom UserControl.


## Running the example

1. git clone https://github.com/codingjq/flet-firebase-tutorial
2. python3 -m venv venv
3. ./venv/Scripts/active or source ./venv/bin/activate
4. pip install -r requirements.txt
5. Create config.py file with your Firebase Realtime Database details.
6. Configure Firebase rules to allow .read/.write for $uid. ($uid === auth.uid)
7. Enable authentication by email and password on Firbase. 
8. flet main.py