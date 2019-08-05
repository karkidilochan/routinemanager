from rest_framework import serializers
from .models import Departments, Programs, Teachers, Rooms, Subjects, Batch, Groups, Timeslot


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departments
        fields = '__all__'


class ProgramsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Programs
        fields = '__all__'


class TeachersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teachers
        fields = '__all__'


class RoomsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rooms
        fields = '__all__'


class SubjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subjects
        fields = '__all__'


class BatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Batch
        fields = '__all__'


class GroupsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groups
        fields = '__all__'


class TimeslotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timeslot
        fields = '__all__'

