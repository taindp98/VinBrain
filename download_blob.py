import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Quick start code goes here
    # connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    connect_str = 'DefaultEndpointsProtocol=https;AccountName=storage1011;AccountKey=5v311ra3pIDPVIuqGOmWhojvwUA3D8ULOx7GiXMKFlCSeWlWO/1bYlv9UIftdcP4ljAxxb7LOv9pkMLOEVBsMA==;EndpointSuffix=core.windows.net'
    # print('connect_str',connect_str)
    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create a unique name for the container
    # container_name = str(uuid.uuid4())
    container_name = 'audio'

    # Create the container
    # container_client = blob_service_client.create_container(container_name)

    local_path = "./audio"
    # os.mkdir(local_path)

    # Create a file in the local data directory to upload and download
    local_file_name ='04_19_2021_18_22_02' + ".wav"
    upload_file_path = os.path.join(local_path, local_file_name)

    # Write text to the file
    # file = open(upload_file_path, 'w')
    # file.write("Hello, World!")
    # file.close()

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    # print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    # with open(upload_file_path, "rb") as data:
    #     blob_client.upload_blob(data)

    print("\nListing blobs...")

    # List the blobs in the container
    # blob_list = container_client.list_blobs()
    # for blob in blob_list:
    #     print("\t" + blob.name)

    # Download the blob to a local file
    # Add 'DOWNLOAD' before the .txt extension so you can see both files in the data directory  
    download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.wav', 'DOWNLOAD.wav'))
    print("\nDownloading blob to \n\t" + download_file_path)

    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

except Exception as ex:
    print('Exception:')
    print(ex)

