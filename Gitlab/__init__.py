import json

from Gitlab import Event
from Gitlab.Event import Push, Issue, MergeRequest, Comment, WikiPage


class Gitlab:
    def __init__(self, payload):
        self.payload = payload
        self.object_kind = payload['object_kind']
        self.project_name = payload['project']['name']
        self.project_url = payload['project']['web_url']

    def get_event(self) -> Push | Issue | MergeRequest | Comment | WikiPage | None:
        match self.object_kind:
            case Event.push:
                return Push(self.payload)
            case Event.issue:
                return Issue(self.payload)
            case Event.merge_request:
                return MergeRequest(self.payload)
            case Event.comment:
                return Comment(self.payload)
            case Event.wiki_page:
                return WikiPage(self.payload)
            case _:
                return None


payload = """{
  "object_kind": "push",
  "event_name": "push",
  "before": "8f7e542ce392ea608b1eb4053572f8a1b8dcf0dc",
  "after": "e18fc237446890b7759d04779138ff8202a6de1d",
  "ref": "refs/heads/main",
  "checkout_sha": "e18fc237446890b7759d04779138ff8202a6de1d",
  "message": null,
  "user_id": 10708052,
  "user_name": "Marco Dong",
  "user_username": "User16421775608429967892",
  "user_email": null,
  "user_avatar": "https://secure.gravatar.com/avatar/1d634a0f4631de25033e0f060a8ee505?s=80&d=identicon",
  "project_id": 33097076,
  "project": {
    "id": 33097076,
    "name": "isw-telegram",
    "description": null,
    "web_url": "https://gitlab.com/User16421775608429967892/isw-telegram",
    "avatar_url": null,
    "git_ssh_url": "git@gitlab.com:User16421775608429967892/isw-telegram.git",
    "git_http_url": "https://gitlab.com/User16421775608429967892/isw-telegram.git",
    "namespace": "Marco Dong",
    "visibility_level": 20,
    "path_with_namespace": "User16421775608429967892/isw-telegram",
    "default_branch": "main",
    "ci_config_path": "",
    "homepage": "https://gitlab.com/User16421775608429967892/isw-telegram",
    "url": "git@gitlab.com:User16421775608429967892/isw-telegram.git",
    "ssh_url": "git@gitlab.com:User16421775608429967892/isw-telegram.git",
    "http_url": "https://gitlab.com/User16421775608429967892/isw-telegram.git"
  },
  "commits": [
    {
      "id": "e18fc237446890b7759d04779138ff8202a6de1d",
      "message": "added books and contents commands\n",
      "title": "added books and contents commands",
      "timestamp": "2022-01-18T23:45:12+01:00",
      "url": "https://gitlab.com/User16421775608429967892/isw-telegram/-/commit/e18fc237446890b7759d04779138ff8202a6de1d",
      "author": {
        "name": "madong",
        "email": "viaimperiale@gmail.com"
      },
      "added": [

      ],
      "modified": [
        "Salesforce/Object/Course.py",
        "Salesforce/__init__.py",
        "Telegram/Commands.py"
      ],
      "removed": [

      ]
    },
    {
      "id": "da5968ffaf6e98e1c061d02105d5a2c06028b4e4",
      "message": "fix session expired salesforce\n",
      "title": "fix session expired salesforce",
      "timestamp": "2022-01-18T09:15:49+01:00",
      "url": "https://gitlab.com/User16421775608429967892/isw-telegram/-/commit/da5968ffaf6e98e1c061d02105d5a2c06028b4e4",
      "author": {
        "name": "madong",
        "email": "viaimperiale@gmail.com"
      },
      "added": [

      ],
      "modified": [
        "Salesforce/__init__.py"
      ],
      "removed": [

      ]
    },
    {
      "id": "8f7e542ce392ea608b1eb4053572f8a1b8dcf0dc",
      "message": "added Procfile for Heroku automatically run main.py\n",
      "title": "added Procfile for Heroku automatically run main.py",
      "timestamp": "2022-01-18T00:02:36+01:00",
      "url": "https://gitlab.com/User16421775608429967892/isw-telegram/-/commit/8f7e542ce392ea608b1eb4053572f8a1b8dcf0dc",
      "author": {
        "name": "madong",
        "email": "viaimperiale@gmail.com"
      },
      "added": [
        "Procfile"
      ],
      "modified": [

      ],
      "removed": [
        "Salesforce/Object/__init__.py"
      ]
    }
  ],
  "total_commits_count": 3,
  "push_options": {
  },
  "repository": {
    "name": "isw-telegram",
    "url": "git@gitlab.com:User16421775608429967892/isw-telegram.git",
    "description": null,
    "homepage": "https://gitlab.com/User16421775608429967892/isw-telegram",
    "git_http_url": "https://gitlab.com/User16421775608429967892/isw-telegram.git",
    "git_ssh_url": "git@gitlab.com:User16421775608429967892/isw-telegram.git",
    "visibility_level": 20
  }
}"""
g = Gitlab(json.loads(payload,strict=False)).get_event()
print(g.formatted_message_md)
print(g.formatted_commits_md)
