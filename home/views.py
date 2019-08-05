from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, viewsets

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Departments, Programs, Teachers, Rooms, Subjects, Batch, Groups, Timeslot

from .serializers import *


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all().order_by('departmentname')
    serializer_class = DepartmentSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Programs.objects.all().order_by('programname')
    serializer_class = ProgramsSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teachers.objects.all().order_by('teachername')
    serializer_class = TeachersSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all().order_by('roomname')
    serializer_class = RoomsSerializer


class SubjectsViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.all().order_by('subjectname')
    serializer_class = SubjectsSerializer


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all().order_by('batchid')
    serializer_class = BatchSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all().order_by('groupid')
    serializer_class = GroupsSerializer


class TimeslotViewSet(viewsets.ModelViewSet):
    queryset = Timeslot.objects.all().order_by('timeid')
    serializer_class = TimeslotSerializer



