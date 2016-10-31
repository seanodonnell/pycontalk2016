import json

from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task()
    def get_homepage(self):
        self.client.get("/")


class WebSiteUser(HttpLocust):
    host = 'http://localhost:8000'
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0
