from azure.storage.blob.baseblobservice import BaseBlobService
from azure.storage.blob import BlobPermissions
from datetime import datetime, timedelta

account_name = 'storage1011'
account_key = '5v311ra3pIDPVIuqGOmWhojvwUA3D8ULOx7GiXMKFlCSeWlWO/1bYlv9UIftdcP4ljAxxb7LOv9pkMLOEVBsMA=='
container_name = 'storage1011'
blob_name = 'audio'

url = f"https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}"

service = BaseBlobService(account_name=account_name, account_key=account_key)
token = service.generate_blob_shared_access_signature(container_name, blob_name, permission=BlobPermissions.READ, expiry=datetime.utcnow() + timedelta(hours=1),)

url_with_sas = f"{url}?{token}"

print(url_with_sas)