from flask import Flask
from flask_apscheduler import APScheduler

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# set configuration values
class Config:
    SCHEDULER_API_ENABLED = True

app.config.from_object(Config())
# initialize scheduler
scheduler = APScheduler()
# if you don't wanna use a config, you can set options here:
# scheduler.api_enabled = True
scheduler.init_app(app)

# interval example
@scheduler.task('interval', id='do_job_1', seconds=30, misfire_grace_time=900)
def job1():
    print('Job 1 executed')

scheduler.start()

if __name__ == "__main__":
    app.run()