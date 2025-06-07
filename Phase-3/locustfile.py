from locust import HttpUser, TaskSet, task, between


class UserBehavior(TaskSet):

    @task(1)
    def scenario_1_open_dashboard(self):
        # سناریو 1: فقط مشاهده داشبورد
        self.client.get(
            "http://localhost/humhub/index.php?r=dashboard%2Fdashboard", name="Dashboard View")

    @task(2)
    def scenario_2_view_post_with_comments(self):
        # سناریو 2: مشاهده پیام ها
        self.client.get(
            "http://localhost/humhub/index.php?r=dashboard%2Fdashboard", name="Dashboard View")
        self.client.get(
            "http://localhost/humhub/index.php?r=mail%2Fmail%2Findex", name="View Messages")

    @task(2)
    def scenario_3_create_new_post(self):
        # سناریو 3: مشاهده پروفایل خود و ادیت کردن ان
        self.client.get(
            "http://localhost/humhub/index.php?r=dashboard%2Fdashboard", name="Dashboard View")
        self.client.get(
            "http://localhost/humhub/index.php?r=user%2Fprofile%2Fhome&cguid=14288f05-3ec2-4d68-a77e-6bc75964225e", name="Profile View")
        self.client.post(
            "http://localhost/humhub/index.php?r=admin%2Fuser%2Fedit&id=1", name="Profile edit")
        # post ^

    @task(1)
    def scenario_4_like_multiple_posts(self):
        #  سناریو 4: مشاهده پروفایل و فالو کردن و پیام دادن
        self.client.get(
            "http://localhost/humhub/index.php?r=dashboard%2Fdashboard", name="Dashboard View")
        self.client.get(
            "http://localhost/humhub/index.php?r=user%2Fprofile%2Fhome&cguid=f7f7094c-ec9a-47ab-b347-589f9cb66685", name="profile")
        self.client.post(
            "http://localhost/humhub/index.php?r=user%2Fprofile%2Ffollow&amp;cguid=f7f7094c-ec9a-47ab-b347-589f9cb66685", name="follow")
        self.client.post(
            "http://localhost/humhub/index.php?r=mail%2Fmail%2Fcreate&amp;userGuid=f7f7094c-ec9a-47ab-b347-589f9cb66685", name="send message")

    @task(1)
    def scenario_5_interact_with_notifications(self):
        # سناریو 5: مشاهده لیست نوتیفیکیشن‌ها و یک نوتیف خاص
        self.client.get(
            "http://localhost/humhub/index.php?r=dashboard%2Fdashboard", name="Dashboard View")
        self.client.get(
            "http://localhost/humhub/index.php?r=notification%2Foverview", name="List Notifications")
        self.client.get(
            "http://localhost/humhub/index.php?r=notification%2Fentry&id=6&cId=6", name="View Notification #6")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 3)
