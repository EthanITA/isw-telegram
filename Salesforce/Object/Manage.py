from Salesforce.Object.Group import Group


class Manage:
    def __init__(self, _id, name, group: Group):
        self.id = _id
        self.name = name
        self.group: Group = group
