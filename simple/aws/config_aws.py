AWS_ACCESS_KEY_ID = "AKIAIETIR4PRSE6ILEGA"
AWS_SECRET_ACCESS_KEY = "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"
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'simple.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'simple.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'filmitouchfiles1'
S3DIRECT_REGION = 'ap-southeast-1'
AWS_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = 'https://%s/assets/' % AWS_CUSTOM_DOMAIN
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
AWS_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}