from django.db import models

import random
import os


def get_filename_ext(filepath):
	base_name=os.path.basename(filepath)
	name ,ext=os.path.splitext(base_name)
	return name ,ext

def upload_image_path(instance,filename):
	new_filename=random.randint(1,13516546431654)
	name ,ext=get_filename_ext(filename)
	final_filename='{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
	return "files/{final_filename}".format(
		new_filename=new_filename,
		final_filename=final_filename
		)


class question_model(models.Model):
    level=models.IntegerField(unique=True)
    title=models.CharField(max_length=200,null=True)
    description=models.TextField(null=True)
    file=models.FileField(upload_to=upload_image_path,null=True,blank=True)
    correct_ans=models.CharField(max_length=500)
    top_level=models.IntegerField(default=34)
    line=models.BooleanField(default=False)
    file_check=models.BooleanField(default=False)


    def __str__(self):
        return self.title

