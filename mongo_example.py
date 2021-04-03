from .mongo import BaseDatabase

USERS = 'Users'


class ExampleDatabase(BaseDatabase):

    def add_user(self, user_id: int, name: str):
        return self.add_object(USERS, {'_id': user_id, 'name': name})

    def get_all_users(self):
        return self.get_objects(USERS, {})

    def get_all_users_id(self):
        return [user['_id'] for user in self.get_all_users()]

    def get_user(self, **kwargs):
        return self.get_object(USERS, kwargs)

    def count_users(self) -> int:
        return len(self.get_all_users())

    def set_user_REL(self, user_id: int, REL: int):
        self.update_object(USERS, {'_id': user_id}, '$set', {'REL': REL})

    def set_user_DEM(self, user_id: int, DEM: int):
        self.update_object(USERS, {'_id': user_id}, '$set', {'DEM': DEM})

    def set_user_rate(self, user_id: int, rate: int):
        self.update_object(USERS, {'_id': user_id}, '$set', {'rate': rate})

    def set_user_room(self, user_id: int, room: int):
        self.update_object(USERS, {'_id': user_id}, '$set', {'room': room})

    def check_number_room(self, i: int) -> int:
        return len(self.get_objects(USERS, {'room': i}))

    def get_users_buy_room(self, i: int):
        return self.get_objects(USERS, {'room': i})

    def set_user_referral(self, user_id: int, referral: int):
        self.update_object(USERS, {'_id': user_id}, '$set', {'referral': referral})

    def set_user_rule(self, user_id: int, accept_rules: bool):
        self.update_object(USERS, {'_id': user_id}, '$set', {'accept_rules': accept_rules})

    def delete_all_users(self):
        self.delete_objects(USERS, {})

    def get_users_with_rate(self):
        return self.get_objects(USERS, {'rate': {'$gt': 0}})
