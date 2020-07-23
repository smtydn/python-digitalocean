from .baseapi import BaseAPI


class ProjectResource(BaseAPI):
    """Project Resource management

    Attributes returned by API:
    urn (str): The uniform resource name of the resource.
    assigned_at (str): A time value given in ISO8601 combined date and time format that represents when the project was created.
    status (str): The status of assigning and fetching the resources.
    """

    def __init__(self, *args, **kwargs):
        self.urn = None
        self.assined_at = None
        self.status = None

        super(ProjectResource, self).__init__(*args, **kwargs)

    def __str__(self):
        return '<ProjectResource: %s>' % self.urn
