# airtable_to_box_backup
The Python script uses the Python packages xlwt and boxsdk for creating Excel spreadsheets and interfacing with the Box API, respectively.

### Local Installation ###
#### Dependencies ####
```bash
pip3 install -r requirements.txt
```

NOTE: If you haven't installed **pip3**, run the following:
```bash
sudo apt install python3-pip
```

If using Python2 (as opposed to Python3, simply imstall pip as follows and replace "pip3" with "pip":
```bash
sudo apt install python-pip
```

Fill in the four [config files](https://github.com/ryanku98/airtable_to_box_backup/tree/master/config) with your corresponding configuration

Run a one-off backup process with ```python3 backup_airtable.py```, or run a repeated cron-like job with ```python3 scheduleCron.py```

NOTE: Running automated Python scripts locally would be better with actual [cron jobs](https://pypi.org/project/python-crontab/), [Windows Scheduler](https://datatofish.com/python-script-windows-scheduler/), or [Automator](https://smallbusiness.chron.com/schedule-automator-tasks-mac-os-x-39132.html) (OS X)

### Installation on Heroku ###
1. Download & install [git](https://git-scm.com/downloads)
2. Create a [Heroku account](https://signup.heroku.com/dc); for this use case a free account should suffice
3. Download & install [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
4. Download / clone this repository
5. Using Heroku CLI, run the following commands (Command Prompt for Windows, Terminal for OS X, etc.)
    1. Log into your Heroku account:
    ```bash
    heroku login
    ```
    2. Create a Heroku application:
    ```bash
    heroku apps:create <your-heroku-app-name>
    ```
    NOTE: All Heroku apps must have unique names, so you may need to try multiple times for a unique app name

    3. Verify that the local git repository is configured with an extra Heroku remote:
    ```bash
    git remote -v
    ```
    4. Add, commit, and push code to Heroku's master branch:
    ```bash
    git commit -am "Initial commit"
    git push heroku master
    ```
6. Specify number of workers for this application:
```bash
heroku ps:scale worker=1
```
7. It should start running by now, so check the logs to verify:
```bash
heroku logs --tail
```
8. Easily stop / start the worker by running the following:
```bash
# stop command
heroku ps:stop worker.1
# start command
heroku ps:restart worker.1
```
If you're getting errors, run `heroku ps` to verify the name of your worker

### Updating Code ###
1. Make necessary changes
2. Commit the changes to git version control and upload to Heroku
```bash
git commit -am "[describe changes here]"
git push heroku master
```
NOTE: after making any changes, make sure the worker is up and running by running `heroku ps`
