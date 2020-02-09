from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import Client
from django.urls import reverse


class TestHomePage(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Chrome(executable_path=r'main_project\tests\functional_tests\chromedriver.exe')
		self.client = Client()
		self.template_name = 'basic_pages/home.html'

	def tearDown(self):
		self.browser.close()

	def test_page_load(self):
		response = self.client.get(self.live_server_url)

		# *TESTS*
		self.assertEquals(
			response.status_code,
			200,
			msg="Home page status code != 200"
		)
		self.assertTemplateUsed(
			response,
			self.template_name,
			msg_prefix="The correct home page template was not loaded."
		)

	def test_navbar_text(self):
		self.browser.get(self.live_server_url)

		# Finds the navbar
		navbar = self.browser.find_element_by_id('main-navbar')
		# Gets the 'Nathan Martinez' element on the navbar
		navbar_brand_text = navbar.find_element_by_id('navbar-brand').text
		actual_navbar_brand_text = "Nathan Martinez"
		# Gets the 'Projects' element on the navbar
		navbar_projects = navbar.find_element_by_id('projects-nav-item')
		navbar_projects_text = navbar_projects.find_element_by_id('projects-nav-link').text
		actual_navbar_projects_text = "Projects"
		# Gets the 'About' element on the navbar
		navbar_about = navbar.find_element_by_id('about-nav-item')
		navbar_about_text = navbar_about.find_element_by_id('about-nav-link').text
		actual_navbar_about_text = "About"

		# *TESTS*
		# Testing brand text
		self.assertEquals(
			navbar_brand_text,
			actual_navbar_brand_text,
			msg="Navbar 'Nathan Martinez' text is not correct"
		)
		# Testing 'Projects' element text
		self.assertEquals(
			navbar_projects_text,
			actual_navbar_projects_text,
			msg="Navbar 'Projects' text is not correct"
		)
		# Testing 'About' element text
		self.assertEquals(
			navbar_about_text,
			actual_navbar_about_text,
			msg="Navbar 'About' text is not correct"
		)

	def test_navbar_links(self):
		self.browser.get(self.live_server_url)
		home_page_url = self.live_server_url

		# Finds the navbar
		navbar = self.browser.find_element_by_id('main-navbar')
		# Clicks navbar 'Nathan Martinez'
		navbar.find_element_by_id('navbar-brand').click()
		# The brand url
		brand_click_url = self.browser.current_url

		# Goes back to the home page
		self.browser.get(home_page_url)
		# Finds the navbar
		navbar = self.browser.find_element_by_id('main-navbar')
		# Clicks navbar 'Projects'
		navbar.find_element_by_id('projects-nav-link').click()
		# The 'projects' url
		projects_click_url = self.browser.current_url
		# The actual 'projects' url (what it should be)
		actual_projects_url = home_page_url + reverse('projects')

		# Goes back to the home page
		self.browser.get(home_page_url)
		# Finds the navbar
		navbar = self.browser.find_element_by_id('main-navbar')
		# Clicks navbar 'About'
		navbar.find_element_by_id('about-nav-link').click()
		# The 'about' url
		about_click_url = self.browser.current_url
		# The actual 'about' url (what it should be)
		actual_about_url = home_page_url + reverse('about')

		# *TESTS*
		self.assertEquals(
			brand_click_url,
			home_page_url + '/',
			msg="Navbar 'Nathan Martinez' link failed."
		)
		self.assertEquals(
			projects_click_url,
			actual_projects_url,
			msg="Navbar 'Projects' link failed."
		)
		self.assertEquals(
			about_click_url,
			actual_about_url,
			msg="Navbar 'About' link failed"
		)


