from rest_framework import serializers
from .models import Departments, Programs, Teachers, Rooms, Subjects, Batch, Groups, Timeslot


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departments


class ProgramsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Programs


class TeachersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teachers


class RoomsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rooms


class SubjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subjects


class BatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Batch


class GroupsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groups


class TimeslotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timeslot

