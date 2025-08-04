import os
import uuid

def image_path_wrapper(instance, filename, folder_name):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join(folder_name, filename)

def profile_image_path(instance, filename):
    return image_path_wrapper(instance, filename, 'profile_pics')

def cover_image_path(instance, filename):
    return image_path_wrapper(instance, filename, 'cover_pics')
