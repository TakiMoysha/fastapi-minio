from minio import Minio


async def is_minio_healthy(minio: Minio) -> bool:
    try:
        minio.list_buckets()
        return True
    except Exception:
        return False


async def is_model_loaded(retrieval_model) -> bool:
    try:
        return True
    except Exception:
        return False
