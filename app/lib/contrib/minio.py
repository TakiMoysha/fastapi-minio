from functools import lru_cache
from advanced_alchemy.types.file_object.backends.obstore import ObstoreBackend
from advanced_alchemy.types.file_object.data_type import StoredObject


# ==============================================================

from minio import Minio
from minio.error import MinioException


@lru_cache(maxsize=1)
def get_minio_client(entrypoint: str, access_key: str, secret_key: str):
    client = Minio(
        entrypoint,
        access_key=access_key,
        secret_key=secret_key,
    )
    if not is_health(client):
        raise RuntimeError("MinIO is not healthy")

    return client


def is_health(client: Minio):
    try:
        client.list_buckets()
        return True
    except MinioException as err:
        return False
