from django.db import models


class InputData(models.Model):
    weather = models.CharField(max_length = 30)
    temperature = models.IntegerField()
    car_model = models.CharField(max_length = 50)
    driver_id = models.IntegerField()


class Map(models.Model):
    pass


class Simulation(models.Model):
    pass


class Sensor_data(models.Model):
    pass


class Real_time_data(models.Model):
    pass


class Predictions(models.Model):
    pass