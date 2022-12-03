from django.db import models


class Found(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Voting(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name='user'
    )

    def __str__(self) -> str:
        return str(self.user.id_card)
