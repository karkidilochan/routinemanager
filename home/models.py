from django.db import models


class Departments(models.Model):
    departmentid = models.CharField(primary_key=True, max_length=2, blank=True)  # Field name made lowercase.
    departmentname = models.CharField(max_length=22, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.departmentid


class Programs(models.Model):
    departmentid = models.ForeignKey(Departments, on_delete=models.CASCADE)  # Field name made lowercase.
    programid = models.CharField(primary_key=True, max_length=3)  # Field name made lowercase.
    programname = models.CharField(max_length=32, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.programid


class Rooms(models.Model):

    departmentid = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)  # Field name made lowercase.
    roomname = models.CharField(primary_key=True, max_length=18)  # Field name made lowercase.
    description = models.CharField(max_length=40, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.roomname


class Subjects(models.Model):
    subjectid = models.CharField(max_length=13, primary_key=True, blank=True)  # Field name made lowercase.
    subjectname = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    departmentid = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)  # Field name made lowercase.
    tyear = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    tpart = models.CharField(max_length=2, blank=True, null=True)  # Field name made lowercase.
    iselective = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.subjectname


class Teachers(models.Model):
    departmentid = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)  # Field name made lowercase.
    teacherid = models.CharField(max_length=3, primary_key=True, blank=True)  # Field name made lowercase.
    teachername = models.CharField(max_length=32, blank=True, null=True)  # Field name made lowercase.
    totalclasses = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.teacherid


class Batch(models.Model):
    batchid = models.CharField(max_length=13, primary_key=True, blank=True)  # Field name made lowercase.
    year = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    programid = models.ForeignKey(Programs, on_delete=models.CASCADE)  # Field name made lowercase.
    tyear = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    tpart = models.CharField(max_length=2, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.batchid


class Groups(models.Model):
    groupid = models.CharField(max_length=13, primary_key=True, blank=True)  # Field name made lowercase.
    noofstudents = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    batchid = models.ForeignKey(Batch, on_delete=models.CASCADE)  # Field name made lowercase.
    complementary_group = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.groupid


class Timeslot(models.Model):
    SUNDAY = 'SUN'
    MONDAY = 'MON'
    TUESDAY = 'TUES'
    WEDNESDAY = 'WED'
    THURSDAY = 'THURS'
    FRIDAY = 'FRI'
    DAY_CHOICES = (
        (SUNDAY, 'Sunday'),
        (MONDAY, 'Monday'),
        (TUESDAY, 'Junior'),
        (WEDNESDAY, 'Senior'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
    )
    timeid = models.CharField(primary_key=True, max_length=10, blank=True)
    programid = models.ForeignKey(Programs, on_delete=models.CASCADE)  # Field name made lowercase.
    teacherid = models.ForeignKey(Teachers, on_delete=models.CASCADE)  # Field name made lowercase.
    groupid = models.ForeignKey(Groups, on_delete=models.CASCADE)
    subjectid = models.ForeignKey(Subjects, on_delete=models.CASCADE)  # Field name made lowercase.
    alternation = models.BooleanField(blank=True, null=True)
    classes = models.CharField(max_length=11, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    day = models.CharField(
        max_length=3,
        choices=DAY_CHOICES,
        default=SUNDAY,
    )
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.timeid

