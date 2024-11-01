from django.test import SimpleTestCase
from django.urls import reverse, resolve
from budget.views import project_list, project_detail, ProjectCreateView

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolves(self):
        url = reverse('list')
        print(resolve(url))
        self.assertEqual(resolve(url).func, project_list)

    def test_add_url_resolves(self):
        url = reverse('add')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, ProjectCreateView) #.view_class resolve error from testing a url using a class based view
    
    def test_detail_url_resolves(self):
        url = reverse('detail')
        print(resolve(url, args=['some-slug']))     #the detail url requires a slug
        self.assertEqual(resolve(url).func, project_detail)