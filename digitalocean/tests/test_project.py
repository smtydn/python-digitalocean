import json
import responses

import digitalocean
from .BaseTest import BaseTest


class TestProject(BaseTest):

    @responses.activate
    def setUp(self):
        super(TestProject, self).setUp()
        self.project = digitalocean.Project(id="4e1bfbc3-dc3e-41f2-a18f-1b4d7ba71679", token=self.token)

    @responses.activate
    def test_load(self):
        data = self.load_from_file('projects/single.json')
        project_path = f"projects/{self.project.id}"

        url = self.base_url + project_path
        responses.add(responses.GET,
                      url,
                      body=data,
                      status=200,
                      content_type='application/json')

        self.project.load()

        self.assert_get_url_equal(responses.calls[0].request.url, url)
        self.assertEqual(self.project.id, "4e1bfbc3-dc3e-41f2-a18f-1b4d7ba71679")

    @responses.activate
    def test_assign_resources(self):
        data = self.load_from_file('projectresource/assign.json')
        url = self.base_url + f'projects/{self.project.id}/resources'
        responses.add(responses.POST,
                      url,
                      body=data,
                      status=202,
                      content_type='application/json')
        self.project.assign_resources(json.loads(data)['resources'])
        self.assert_url_query_equal(responses.calls[0].request.url, url)
