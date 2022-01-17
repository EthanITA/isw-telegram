from Salesforce.Object.Manage import Manage


class Professor:
    def __init__(self,
                 _id: str,
                 first_name,
                 email,
                 website,
                 manage: Manage,
                 last_name=None,
                 alias=None,
                 bio=None,
                 personal_website=None,
                 phone=None,
                 tg_user_id=0,
                 tg_username=None):
        self.id = _id
        self.first_name = first_name
        self.email = email
        self.website = website
        self.manage: Manage = manage
        self.last_name = last_name
        self.alias = alias
        self.bio = bio
        self.personal_website = personal_website
        self.phone = phone
        self.tg_user_id = tg_user_id
        self.tg_username = tg_username
