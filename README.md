# personal-website
This repo contains Dash code to create personal website to display some basic info, photos, and some projects.

Link to website:
https://personal-website-v1.herokuapp.com/ 
https://www.victor-arango-quiroga.com/





# To run locally:

1. Create virtual environment 

2. Activate environment:

'source venv/bin/activate'

Note: Using WSL/Linux

3. Install gunicorn (server to run Flask/Dash app). Note: Flask built-in server can be used as well to debug, but gunicorn is the one running the website. 
sudo apt install gunicorn

4. Install dependecies:

'pip install -r requirements.txt'


# To deploy in Heroku:
1. Login: 

'heroku login'

Note: It'll open a window to login to Heroky CLI

2. Once code changes are added and committed:
'git push heroku master' 


