
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Item


class StaticViewSitemap(Sitemap):

	def item(self):
		return ['gispay',]

	def location(self, item):
		return reverse(item)

class ItemSitemap(Sitemap):

	def item(self):
		return Item.objects.all()

	def get_absolute_url(self):
		return {self.item_id}