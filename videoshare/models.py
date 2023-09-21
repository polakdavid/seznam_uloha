from django.db import models

# Create your models here.
class Videos(models.Model):
    name = models.TextField(max_length=200)
    shortName = models.CharField(default="", max_length=100)
    iconUri = models.URLField()
    manifestUri = models.URLField()
    source = models.CharField(max_length=50)
    focus = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    extraText = models.JSONField() # Array
    certificateUri = models.URLField(default=None)
    description = models.TextField(default=None, max_length=1024)
    isFeatured = models.BooleanField(default=False)
    drm = models.JSONField() # Array
    features = models.JSONField() # Array
    licenseServers = models.JSONField()
    licenseRequestHeaders = models.JSONField()
    requestFilter = models.CharField(default=None, max_length=100)
    responseFilter = models.CharField(default=None, max_length=100)
    clearKeys = models.JSONField()
    extraConfig = models.JSONField(default=None)
    adTagUri = models.URLField(default=None)
    imaVideoId = models.IntegerField(default=None)
    imaAssetKey = models.CharField(default=None, max_length=50)
    imaContentSrcId = models.IntegerField(default=None)
    mimeType = models.CharField(default=None, max_length=200)
    mediaPlaylistFullMimeType = models.CharField(default=None, max_length=200)
    storedProgress = models.IntegerField(default=0)
    storedContent = models.JSONField(default=None)
