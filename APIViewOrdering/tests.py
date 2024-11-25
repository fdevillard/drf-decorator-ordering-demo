from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class ViewsTestCase(APITestCase):
    def test_anonymous_user_cannot_access_api_view_first(self):
        url = reverse("api_view_first")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_anonymous_user_cannot_access_permission_first(self):
        url = reverse("permission_first")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
