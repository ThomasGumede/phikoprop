import uuid

def handle_profile_upload(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return f"profile/{filename}"

def handle_room_cover_upload(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return f"rooms/{filename}"

def handle_room_content_upload(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}-{}.{}'.format(uuid.uuid4().hex,ext)
    return f"rooms/{instance.room.title}/{filename}"