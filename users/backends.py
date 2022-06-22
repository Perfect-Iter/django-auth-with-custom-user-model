from models import UserModel
import logging


class MyAuthBackend(object):
    def authenticate(self, email, password):    
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                return None
        except UserModel.DoesNotExist:
            logging.getLogger("error_logger").error("user with login %s does not exists ")
            return None
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None

    def get_user(self, nat_id):
        try:
            user = UserModel.objects.get(nat_id=nat_id)
            if user.is_active:
                return user
            return None
        except UserModel.DoesNotExist:
            logging.getLogger("error_logger").error("user with %(nat_id) not found")
            return None