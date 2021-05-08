from django.db import models

from core import models as core_model

# Create your models here.
class TimeAbstractModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True

class Project(TimeAbstractModel):
    created_by = models.ForeignKey(core_model.User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_time_spent(self):
        pass

    def get_start_date(self):
        return self.start_date.date()

    def get_end_date(self):
        return self.end_date.date()



class Task(TimeAbstractModel):
    class StatusType(models.IntegerChoices):
        OPEN = 0, 'OPEN'
        END = 1, 'END'
        CLOSE = 2, 'CLOSED'
    created_by = models.ForeignKey(core_model.User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    skill = models.ForeignKey(core_model.Skill, on_delete=models.SET_NULL, null=True)
    duration = models.DurationField()       # replace duration by story points for agile scrum
    deadline = models.DateTimeField()
    status = models.IntegerField(choices=StatusType.choices, default=StatusType.OPEN)

    def __str__(self):
        return self.title

    def get_time_remaining(self):
        pass

    def save(self, *args, **kwargs):
        self.duration = self.duration * 60  # converts to duration in minutes
        super().save(*args, **kwargs)


    def get_assignee(self):
        user_list =  core_model.User.objects.filter(skills=self.skill)

        if user_list:
            print(user_list)
            user = min(user_list, key=lambda x:x.assigned_time())
            print(user)
            return user
        return None

    def auto_assign_task(self):
        user = self.get_assignee()
        if user:
            TaskAssignee.objects.create(user=user,task=self)
            return user
        return False




class TaskAssignee(TimeAbstractModel):
    user = models.ForeignKey(core_model.User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()

    def total_time_spent(self):
        pass


class AssigneeLog(TimeAbstractModel):
    assignee = models.ForeignKey(TaskAssignee, on_delete=models.SET_NULL, null=True)
    start = models.DateTimeField()
    end =  models.DateTimeField()

    def get_sprint_duration(self):
        return self.end - self.start
