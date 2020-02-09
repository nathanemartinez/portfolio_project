# Django imports
from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import BrokenLinkCheckerModelForm
from .models import BrokenLinkCheckerModel
# Web scraping imports
from bs4 import BeautifulSoup
import requests


def broken_link_checker(request):
	# checkers = BrokenLinkCheckerModel.objects.all()
	form = BrokenLinkCheckerModelForm()
	# So nothing shows up when I do {% if code %}
	access = ""
	links_404 = {}
	other_links = {}

	if request.method == 'POST':
		form = BrokenLinkCheckerModelForm(request.POST or None)
		if form.is_valid():
			name = form.cleaned_data['site_name']
			links = get_404_links(name)
			links_404 = links[0]
			other_links = links[1]
			# form.save()
			form = BrokenLinkCheckerModelForm(request.POST or None)
		else:
			access = "Unable to access site. The site may be blocking the bot. Did you enter the site correctly?"
	else:
		access = True
		form = BrokenLinkCheckerModelForm(request.POST or None)

	context = {'access': access, 'form': form, 'links_404': links_404, 'other_links': other_links}
	template_name = 'broken_link_checker/broken_link_checker.html'
	return render(request, template_name, context)


def get_404_links(link: str):
	"""
	Finds the 404 links on the page.
	:param link: The link
	:return: A list of broken links. OR None if an error occurred
	"""
	# Some sites don't allow you to access content without a user agent
	# Google 'what is my user agent'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
	}
	try:
		request = requests.get(link, headers=headers)
		soup = BeautifulSoup(request.text, 'html.parser')
		if soup is None:
			return None
	except:
		return None

	soup = BeautifulSoup(request.text, 'html.parser')
	links_404 = {}
	other_links = {}
	for link in soup.find_all('a', href=True):
		link_text = link.string
		link = link['href']
		if 'http://' or 'https://' in link:
			try:
				request = requests.get(link, headers=headers)
				code = request.status_code
				if code == 404:
					links_404[link] = link_text, code
				elif code != 200:
					other_links[link] = link_text, code
			except:
				pass
		else:
			pass

	return links_404, other_links


