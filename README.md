# Personal Wwebsite
This repo contains Dash code to create personal website to display some basic info, photos, and some projects.

Link to website:

- https://personal-website-v1.herokuapp.com/ 
- https://www.victor-arango-quiroga.com/


# To run locally:

1. Create virtual environment 

2. Activate environment:

  :eyes:``` source venv/bin/activate ```

:pencil2: Note: Using WSL/Linux

3. Install gunicorn (server to run Flask/Dash app). Note: Flask built-in server can be used as well to debug, but gunicorn is the one running the website. 

:eyes: ```sudo apt install gunicorn```

4. Install dependecies:
  
  :eyes: ```pip install -r requirements.txt ```

5. Run:

  :eyes: ``` gunicorn app:flask_app ```


# To deploy in Heroku:
1. Login: 

  :eyes: ``` heroku login ```

:pencil2: Note: It'll open a window to login to Heroky CLI

2. Once code changes are added and committed:

  :eyes: ```git push heroku master```

:pencil2: Note: CICD pipeline integrated so one only needs to merge a PR to master branch and it will automatically deploy to prod (PR deploys to QA first). 

# SSL Certificate

Free provider: https://zerossl.com/?fpr=geekflare
It provides 90-days free certificates, up to 3. Or 1 year SSL certificate for $10 a month. 

- Where to find my domain info? https://domains.google.com/registrar/ 
 
- Verify domain ownership, go to DNS -> Maange custom records -> add new Host name, type, TTL, Data provided by zerossl. 
  
- Download Certificate created on Zerossl. Unzip folder.

- How to add to Heroku? https://devcenter.heroku.com/articles/ssl
  -   `heroku login`
  -   `heroku certs:add server.crt server.key`
  -   Navigate to unzipped folder where certificate is.
  -   `heroku certs:add certificate.crt private.key`
*The bottom line is that Heroku mentions they offer free SSL certificates but that's really not the case unless you have a Hobby ($7/mo) or Pro plan.*
https://stackoverflow.com/questions/52185560/heroku-set-ssl-certificates-on-free-plan#:~:text=Free%20SSL%20in%20Heroku%20doesn,for%20the%20SSL%20to%20work. 

Note: Thinking to migrate website to other platforms where I can use free ssl certificates. 


