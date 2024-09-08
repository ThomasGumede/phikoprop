import uuid

def handle_profile_upload(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return f"profile/{filename}"

def handle_relativeprofile_upload(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return f"profile/relatives/{filename}"