from django.db import models

class Roulette(models.Model):
    id = models.AutoField(primary_key=True)
    bets=models.IntegerField()
    open=models.BooleanField()

    def getid(self):
        return self.id

class Player(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,unique=True)
    funds=models.IntegerField()

    def __str__(self):
        return self.name

class Bet(models.Model):
    id=models.AutoField(primary_key=True)
    player_id=models.IntegerField()
    roulette_id=models.IntegerField()
    ammount=models.IntegerField()

    def getid(self):
        return self.id


