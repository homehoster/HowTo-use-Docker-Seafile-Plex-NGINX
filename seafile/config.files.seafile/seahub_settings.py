#NUR URL von http auf https ändern
FILE_SERVER_ROOT = "https://<Domain bspw. seafile.dyn.de>/seafhttp"

#diese Zeile noch einfügen
SERVICE_URL = 'https://<Domain bspw. seafile.dyn.de>/seafhttp'

# Enable E-Mail Support 
# EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.xxx.xx'        # smpt server
EMAIL_HOST_USER = 'deineMailAdresse'    # username and domain
EMAIL_HOST_PASSWORD = 'password'    # password
EMAIL_PORT = 465 # 25
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

# Set reply-to header to user's email or not, defaults to ``False``. For details,
# please refer to http://www.w3.org/Protocols/rfc822/
ADD_REPLY_TO_HEADER = True

OFFICE_SERVER_TYPE = 'CollaboraOffice'
ENABLE_OFFICE_WEB_APP = True
# OFFICE_WEB_APP_BASE_URL = 'http://collabora:9980/hosting/discovery'
OFFICE_WEB_APP_BASE_URL = 'https://doc.deine.domain/hosting/discovery'

# Expiration of WOPI access token
# WOPI access token is a string used by Seafile to determine the file's
# identity and permissions when use LibreOffice Online view it online
# And for security reason, this token should expire after a set time period
WOPI_ACCESS_TOKEN_EXPIRATION = 30 * 60   # seconds

# List of file formats that you want to view through LibreOffice Online
# You can change this value according to your preferences
# And of course you should make sure your LibreOffice Online supports to preview
# the files with the specified extensions
OFFICE_WEB_APP_FILE_EXTENSION = ('odp', 'ods', 'odt', 'xls', 'xlsb', 'xlsm', 'xlsx','ppsx', 'ppt', 'pptm', 'pptx', 'doc', 'docm', 'docx')

# Enable edit files through LibreOffice Online
ENABLE_OFFICE_WEB_APP_EDIT = True

# types of files should be editable through LibreOffice Online
OFFICE_WEB_APP_EDIT_FILE_EXTENSION = ('odp', 'ods', 'odt', 'xls', 'xlsb', 'xlsm', 'xlsx','ppsx', 'ppt', 'pptm', 'pptx', 'doc', 'docm', 'docx')

# Enable Metadata Management
ENABLE_METADATA_MANAGEMENT = True
METADATA_SERVER_URL = 'http://seafile-md-server:8084'

# video thumbnails (disabled by default)
ENABLE_VIDEO_THUMBNAIL = False
