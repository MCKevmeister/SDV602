from jsn_drop_service import jsnDrop
from time import gmtime


def now_time_stamp():
    time_now = gmtime()
    timestamp_str = f"{time_now.tm_year}-" \
                    f"{time_now.tm_mon}-" \
                    f"{time_now.tm_mday} " \
                    f"{time_now.tm_hour}:" \
                    f"{time_now.tm_min}:" \
                    f"{time_now.tm_sec} "
    return timestamp_str


class UserManager(object):
    current_user = None
    current_pass = None
    current_status = None
    chat_list = None
    this_user_manager = None

    def __init__(self) -> None:
        super().__init__()

        self.jsnDrop = jsnDrop("0daa9aa0-17d8-4d8c-8203-2c94dc91c034", "https://newsimland.com/~todd/JSON")

        # SCHEMA Make sure the tables are  CREATED - jsnDrop does not wipe an existing table if it is recreated
        self.jsnDrop.create("tblUser", {"PersonID PK": "A_LOOONG_NAME" + ('X' * 50),
                                        "Password": "A_LOOONG_PASSWORD" + ('X' * 50),
                                        "Status": "STATUS_STRING"})

        self.jsnDrop.create("tblChat", {"PersonID PK": "A_LOOONG_NAME" + ('X' * 50),
                                        "DESNumber": "A_LOOONG_DES_ID" + ('X' * 50),
                                        "Chat": "A_LOONG____CHAT_ENTRY" + ('X' * 255),
                                        "Time": now_time_stamp() + ('X' * 50)})
        UserManager.this_user_manager = self

    def register(self, user_id, password):
        self.jsnDrop.select("tblUser",
                            f"PersonID = '{user_id}'")
        if "DATA_ERROR" in self.jsnDrop.jsnStatus:
            self.jsnDrop.store("tblUser",
                               [{'PersonID': user_id, 'Password': password, 'Status': 'Registered'}])
            UserManager.currentUser = user_id
            UserManager.current_status = 'Logged Out'
            result = "Registration Success"
        else:
            result = "User Already Exists"

        return result

    def login(self, user_id, password):
        self.jsnDrop.select("tblUser",
                            f"PersonID = '{user_id}' AND Password = '{password}'")
        if "DATA_ERROR" in self.jsnDrop.jsnStatus:
            result = "Login Fail"
            UserManager.current_status = "Logged Out"
            UserManager.current_user = None
        else:
            UserManager.current_status = "Logged In"
            UserManager.current_user = user_id
            UserManager.current_pass = password
            self.jsnDrop.store("tblUser",
                               [{"PersonID": user_id, "Password": password, "Status": "Logged In"}])
            result = "Login Success"
        return result

    def chat(self, message):
        if UserManager.current_status != "Logged In":
            result = "You must be logged in to chat"

        else:
            user_id = UserManager.current_user
            api_result = self.jsnDrop.store("tblChat", [{'PersonID': user_id,
                                                         'Chat': message,
                                                         'Time': now_time_stamp()}])
            if "ERROR" in api_result:
                result = self.jsnDrop.jsnStatus
            else:
                result = "Chat sent"

        return result

    def get_chat(self):
        result = None

        if UserManager.current_status == "Logged In":
            api_result = self.jsnDrop.select("tblChat")
            if not ('DATA_ERROR' in api_result):
                UserManager.chat_list = self.jsnDrop.jsnResult
                result = UserManager.chat_list
        return result

    def logout(self):
        result = "Must be 'Logged In' to 'LogOut' "
        if UserManager.current_status == "Logged In":
            api_result = self.jsnDrop.store("tblUser", [{"PersonID": UserManager.current_user,
                                                         "Password": UserManager.current_pass,
                                                         "Status": "Logged Out"}])
            if not ("ERROR" in api_result):
                UserManager.current_status = "Logged Out"
                result = "Logged Out"
            else:
                result = self.jsnDrop.jsnStatus

        return result
