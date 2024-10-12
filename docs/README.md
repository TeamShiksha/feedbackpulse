# feedbackpulse

This application allows aspiring developer, designer or product managers to onboard [Team.shiksha](https://team.shiksha/) projects. Other feature includes:
1. Give user access to github org, and add them to proper teams.
2. Check if user is member of discord, and give them proper role.
3. Raise snapshot every 2 months to other members.
4. Raise/revoke admin/operator access for different projects.
5. Raise/revoke AWS access.

## Requirements
1. tailwindcss
2. python (3.11.1 <= version)
3. `set FLASK_APP=app:create_app`
4. `set FLASK_CONFIG='development'` (Optional by default 'development')

## How to run this project

```
git clone https://github.com/TeamShiksha/feedbackpulse.git
cd feedbackpulse
python -m venv venv
venv\Scripts\activate(Windows, based on your OS please google how to activate virtual environment)
pip install -r requirements.txt
python app.py
```

## Important

If you are making changes only in html tags and want the app to load automatically on changes, use the command below:
```
python app.py --extra-files "templates/your_filename.html"
```

If you are making changes in the tailwind css or using a new class, you will need to run the below commands to make sure the changes are reflecting:
```
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css
flask run
``` 
or
```
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css && flask run
```
To make this simple you can merge all the above commands in one line as give below:
```
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css && flask run --extra-files "templates/your_filename.html"
```

## Before commit

isort and black are added to the requirements.txt to make import and  styling correct. Run the below command to make sure the imports and code formating is done porperly before every commit.  

```
isort *.py
black *.py
``` 