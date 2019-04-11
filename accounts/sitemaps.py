

from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
# from .models import Item


class StaticViewSitemap(Sitemap):

	def items(self):
		return ['logout','profile']

	def location(self, item):
		return (item)

# class ItemSitemap(Sitemap):
# 	changefreq="daily"
# 	priority = 1.0

# 	def items(self):
# 		return Item.objects.all()

	