from django.db import models

# Model to archive database locally
class Videos(models.Model):
    name = models.TextField(max_length=200)
    shortName = models.CharField(default="", max_length=100)
    iconUri = models.URLField()
    manifestUri = models.URLField()
    source = models.CharField(max_length=50)
    focus = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    extraText = models.JSONField() # Array
    certificateUri = models.URLField(default=None, null=True, blank=True)
    description = models.TextField(default=None, max_length=1024, null=True, blank=True)
    isFeatured = models.BooleanField(default=False)
    drm = models.JSONField() # Array
    features = models.JSONField() # Array
    licenseServers = models.JSONField()
    licenseRequestHeaders = models.JSONField()
    requestFilter = models.CharField(default=None, max_length=100, null=True, blank=True)
    responseFilter = models.CharField(default=None, max_length=100, null=True, blank=True)
    clearKeys = models.JSONField()
    extraConfig = models.JSONField(default=None, null=True, blank=True)
    adTagUri = models.URLField(default=None, null=True, blank=True)
    imaVideoId = models.CharField(default=None, max_length=50, null=True, blank=True)
    imaAssetKey = models.CharField(default=None, max_length=50, null=True, blank=True)
    imaContentSrcId = models.IntegerField(default=None, null=True, blank=True)
    mimeType = models.CharField(default=None, max_length=200, null=True, blank=True)
    mediaPlaylistFullMimeType = models.CharField(default=None, max_length=200, null=True, blank=True)
    storedProgress = models.IntegerField(default=0)
    storedContent = models.JSONField(default=None, null=True, blank=True)

