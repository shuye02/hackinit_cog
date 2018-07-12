# Cog

**This project is forked from [techx/cog](https://github.com/techx/cog), which is a hardware checkout system for hackathons.**  

It is written in Python 2, based on the framework of [Python Flask](http://flask.pocoo.org/) and enabled by [Gunicorn](http://gunicorn.org/) as a WSGI HTTP Server

This README.md is written by [shuye02](https://www.github.com/shuye02).  
You can go to [here](https://github.com/techx/cog/blob/master/README.md) for the original README.md of this project.

## Features

You can refer to the [original README.md](https://github.com/techx/cog/blob/master/README.md) from the [original project](https://github.com/techx/cog/).

## Deployment

#### Dependencies list

- python2
- python2-pip
- python2-virtualenv (optional, but *recommended*)
- PostgreSQL
- some other python libraries (refer to [requirements.txt](/requirements.txt))

#### Installing dependencies

1. Install python2, python2-pip  
 `Depends on your Linux distro, please refer to your distro wiki`
2. Install python2-virtualenv  
 `$ pip install virtualenv`
3. Setup python 2 virtual environment (optional, but *recommended*)  
 `$ virtualenv venv`
4. Source your virtual environment   
 `$ source venv/bin/activate`
5. Install dependent Python libraries   
 `(venv) $ pip install -r requirements.txt`
6. You can then leave your virtual env by typing `deactivate`
7. Install PostgreSQL and start it  
  You can refer to the [Arch Linux wiki](https://wiki.archlinux.org/index.php/PostgreSQL#Installing_PostgreSQL) for the **Installation** and **Intial Configuration** of PostgreSQL

##### An example of PostgreSQL Initial Configuration
```sh
# Switch to PostgreSQL admin account
$ sudo -u postgres -i

# Add your username
[postgres]$ createuser --interactive
[postgres]$ exit

# Create your database
$ createdb myDatabaseName -U username
# the [-U username] parameter can be omitted if the database user has the same name as your Linux user
```

> **Note**:  
  The database username is recommended to be your Linux username, since PostgreSQL uses a [peer authentication](https://www.postgresql.org/docs/current/static/auth-methods.html#AUTH-PEER) technique to map between Linux and database usernames.  
  So, if you create a PostgreSQL user with the same name as your Linux username, it allows you to access the PostgreSQL database shell without having to specify a user to login (which makes it quite convenient).

And you may want to check whether your database are accessible or not.
```sh
$ psql -d myDatabaseName
=> \?
=> \q (or CTRL+d)
```

#### Configuration

##### Customize for your own hackathon

You can go to [config.py](/hardwarecheckout/config.py) to edit the following settings:
* Your Hackathon name (*default to "Hack.init()"*)
* Toggle Submission Settings
  * Proposal for lottery items
  * Multiple submissions for the same item
  * etc.
* Toggle Item Display
* Info texts shown at the index page

In addition, you can change the default [favicon.png](/hardwarecheckout/static/favicon.png) of your website and the [default picture](/hardwarecheckout/static/images/default.png) for your hardware items.

> **Note**:  
  If you have installed the dependent python libraries in your virtual environment, you need to source the virtual environment before running the following commands.  
  And you may want to run the following commands in a [Linux Screen terminal](https://www.gnu.org/software/screen/manual/screen.html).  
  Especially when you are running cog in a vps, so that you can use `screen -r` command to retrieve the terminal from different login sessions.

##### Environment Variables

You **need** to set the following environment variables before getting your cog running
* `DATABASE_URL`: the PostgreSQL database URL  
  It should be in the form of `postgres://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]`.  
  *An example `DATABASE_URL` may look like `postgres://username@localhost/cog`*
* `QUILL`: the URL to your [Quill](https://github.com/techx/quill) instance for auth.  
  *An example `QUILL` may look like `http://localhost:3000/`*
* `SECRET`: it needs to be exactly the **same** JWT secret set in your QUILL configurations.

#### Running

* Run `python initialize.py`.  
  This initializes the database — run it if you make any changes to the models and
  are fine with overwriting data.
* Run `make run`.  
  The site is now listening at `0.0.0.0:8000`  
> **Note**:  
  You can change the listening address and port in [Makefile](/Makefile)  
  For example, you may want to listen only `127.0.0.1:8000` and have nginx forward to this port.

## Directory Architectures
*TO-DO*

## Customizations
*This part is cited directly from the [original README.md](https://github.com/techx/cog/blob/master/README.md) of the original project.*

#### Adding Hardware via [Google Sheets](https://www.google.com/sheets/about/)

While you can add individual items one-by-one, we recommend creating a
spreadsheet with all your items and importing this into Cog in one go.
Currently, the only supported way to do this is via Google Sheets. An example
Cog inventory sheet can be found
[here](https://docs.google.com/spreadsheets/d/1ZCHa_F3i0vyoZtjJNyNhBg-flRBs-DUIT1GtKC26P14/edit#gid=0).

To import from a Google Sheet, simply turn on view-only sharing and paste the main URL (not the sharing URL) into Cog after clicking 'Import Google Sheet' on the main inventory page.

> **Note**:  
  You may need to set up a proxy to have access to Google Sheets depending on your network environment.

#### Customizing Branding

Cog uses the [Semantic UI](https://semantic-ui.com/) framework for styling.
Branding can easily be customized using Semantic UI
[themes](https://semantic-ui.com/usage/theming.html).

While Cog mostly uses default Semantic UI styling, a minimal amount of custom
CSS lives in `hardwarecheckout/static/sass/app.scss`. In order to rebuild the
CSS when the Sass is changed, install [Sass](https://sass-lang.com/) and run
`sass --watch sass:css` in the `/static` directory.
