from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5  # Adjust priority (0.1 - 1.0)
    changefreq = 'monthly'  # Update frequency

    def items(self):
        return ['index', 'about', 'contact']  # Replace with actual view names

    def location(self, item):
        return reverse(item)
