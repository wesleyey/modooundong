from django.db import models
from common.models import CommonModel


# Create your models here.
class Place(CommonModel):
    """Place Model Definition"""

    name = models.CharField(max_length=180, default="")
    address = models.CharField(
        max_length=250,
    )
    description = models.TextField()
    details = models.ManyToManyField("places.Detail")
    creator = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def total_details(self):
        return self.details.count()

    def rating(self):
        count = self.review_set.count()
        if count == 0:
            return "No Review"
        else:
            total_rating = 0
            for review in self.review_set.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 1)


class Detail(CommonModel):
    """Detail Definition"""

    name = models.CharField(max_length=150)
    description = models.CharField(
        max_length=150,
        default="",
    )

    def __str__(self):
        return self.name
