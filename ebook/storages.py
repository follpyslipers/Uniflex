from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
import oss2
from django.conf import settings

@deconstructible
class AliyunOSSStorage(Storage):
    def __init__(self, access_key_id=None, access_key_secret=None, bucket_name=None, endpoint=None):
        self.access_key_id = access_key_id or settings.OSS_ACCESS_KEY_ID
        self.access_key_secret = access_key_secret or settings.OSS_ACCESS_KEY_SECRET
        self.bucket_name = bucket_name or settings.OSS_BUCKET_NAME
        self.endpoint = endpoint or settings.OSS_ENDPOINT
        self.bucket = oss2.Bucket(oss2.Auth(self.access_key_id, self.access_key_secret), self.endpoint, self.bucket_name)

    def _open(self, name, mode='rb'):
        file_obj = self.bucket.get_object(name)
        return file_obj

    def _save(self, name, content):
        self.bucket.put_object(name, content)
        return name

    def url(self, name):
        return f"https://{self.bucket_name}.{self.endpoint}/{name}"

    def exists(self, name):
        return self.bucket.object_exists(name)

    def delete(self, name):
        self.bucket.delete_object(name)

    def size(self, name):
        return self.bucket.head_object(name).content_length

    def listdir(self, path):
        # List directory not implemented
        raise NotImplementedError("listdir is not implemented")
