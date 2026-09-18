# How to use the minecraft API
Note that this is v1 and does not have a front end.
as such, we will proceed using fastAPI's /docs default path.

Also note that there are 2 sets of steps, 
one set are for external users who may use this api for their own servers and their userbase.   
The other one are for internal users, who sp ecifically use my server
## 1) Go to the site
Proceed to the api web dashboard at {url}/docs  
Eg: [https://api.blindmanzeye.me/docs]()

## 2) Authorize Session
All API endpoints require authorization. For devs, please configure a key for your environment. This 
can be a generic passphrase, but i suggest generating a cryptographically secure key. all of mine were generated via the bash command: 
```bash
openssl rand -base64 32
```



for Users, please retrieve a key from an admin 

After retrieving a key, on the site, click the green authorize button and paste the key in the input box labeled **"value"** 
and press authorize and close.

## 3) Execute commands
Now you may execute commands from the list.
to execute a command:
### i) Select the desired command to expand it
### ii) Select **Try it out** 
### iii) Select **Execute**

After selecting **Execute**, it should give you an option to **Execute** again or **clear**
once you are given these options, scroll down until you see details and code

tl;dr if you see `code 200` then your command probably went through
if you see `code 5xx` then an internal server error caused your command to not go through
and you should probably talk to your admin