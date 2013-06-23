# created by Noah Coad 2013-03-01
# miscellaneous url based helper routines

from urllib import request, parse
import re, sys

# helpers for working with HTTP, URLs, and links
class Linker:

	# gets the html contents at a URL and look like a legit browser
	def get_page(self, url):
		user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
		headers = {'User-Agent':user_agent,}
		req = request.Request(url, None, headers)
		page = request.urlopen(req)
		html = str(page.read())
		page.close()
		return html

	# extracts the title of a web page at a URL
	def get_title(self, url):
		html = self.get_page(url)
		title = re.search(r'<title>(.*)</title>', html).group(1)
		title = ' '.join(title.split())
		return title

	# provides the HTML for a URL
	def make_link(self, url, title):
		return '<a href="{url}">{title}</a>'.replace('{url}', url).replace('{title}', title)


# helpers for working with Google
class Google:
	# fixes spelling using a google search
	# created by Noah Coad 2013-06-23 01:51am
	def spell(self, text):
		# grab html
		html = Linker().get_page('http://www.google.com/search?q=' + parse.quote(text))
		with open('debug_urltools_google_spell_page_source.html', 'w') as f:
			f.write(html)

		# pull pieces out
		match = re.search(r'(?:Showing results for|Did you mean).*?<a.*?>(.*?)</a>', html)
		if match is None:
			fix = text
		else:
			fix = match.group(1)
			fix = re.sub(r'<.*?>', '', fix);

		# return result
		return fix


# helpers for working with Noah Coad's blog
class CoadBlog:
	
	# performs an 'I Feel Lucky' search and returns top result
	def lucky(self, search_term):
		url = r'http://www.google.com/cse?cx=005947812333522790670:srzrqfvfpng&ie=UTF-8&sa=Search&siteurl=www.google.com/cse/home%3Fcx%3D005947812333522790670:srzrqfvfpng&ref=www.google.com/cse/panel/basics%3Fcx%3D005947812333522790670:srzrqfvfpng%26sig%3D__0EJk8-gzevtGHWnz0WdhmVV8hIo%3D&nojs=1&q='
		url += parse.quote(search_term)
		html = Linker().get_page(url)

		target_url = re.search(r'<li.*?href="(.*?)"', html).group(1)

		title = re.search(r'<li.*?<a.*?>(.*?)</a>', html).group(1)
		title = title.replace('<b>', '').replace('</b>', '')
		title = self.strip_title(title)

		return target_url, title

	# removes common blog prefixes from page title
	def strip_title(self, title):
		fix = title.replace('Noah Coad - ', '').replace(' - Noah Coad - Site Home - MSDN Blogs', '').replace(r" - #region Coad's Code (Noah Coad)", '').replace('Noah Coad, ', '').replace(' - Site Home - MSDN Blogs', '')
		return re.sub(r' - #region.*\Z', '', fix)

	# create an HTML link to the top search term hit
	def search_link(self, search_term):
		url, title = self.lucky(search_term)
		return Linker().make_link(url, self.strip_title(title))

	# create an email link for the top search term hit
	def email(self, search_term):
		url, title = self.lucky(search_term)

		email = "mailto:?subject={title}&body={url}"
		email = email.replace("{title}", parse.quote(title))
		email = email.replace("{url}", parse.quote(Linker().make_link(url, title)))

		return email