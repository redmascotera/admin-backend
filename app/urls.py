"""App Urls"""

# Load all the api urls here
from app.api.doc import doc_urls

# Create URL Patterns and extend with all the api urls
urlpatterns = []
urlpatterns.extend(doc_urls.urlpatterns)
