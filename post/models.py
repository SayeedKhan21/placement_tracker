from django.db import models
from app.models import (
    Placement_Detail  ,
)
from base.models import (
    BaseModel ,
)
# Create your models here.


class Post(BaseModel) :
    title = models.CharField(max_length=100)
    content = models.TextField()
    offer = models.ForeignKey(Placement_Detail ,on_delete = models.CASCADE ,related_name = 'offer')
    
    def __str__(self) : 
        return self.title