import json
import responses

import digitalocean
from .BaseTest import BaseTest


class TestProject(BaseTest):

    @responses.activate
    def setUp(self):
        super(TestProject, self).setUp()
        self.project = digitalocean.Project(id=12345, token=self.token)

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
