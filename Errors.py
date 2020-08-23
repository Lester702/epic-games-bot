# Custom errors

class AlreadyPurchasedError(Exception):
    def __init__(self):
        super().__init__("You have already purchased this game.")

class LoginFailedError(Exception):
    def __init__(self):
        super().__init__("Unable to login to your Epic Games account. Please check that your credentials were entered correctly.")

class ReCaptchaError(Exception):
    def __init__(self):
        super().__init__("Unable to continue. Possibly due to a ReCAPTCHA test.")