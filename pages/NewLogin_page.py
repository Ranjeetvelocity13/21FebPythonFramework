
import time
import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class LoginPage(BasePage): #oops - inh
    """
    LoginPage - Handles all login/logout related actions on demoblaze.com.
    Uses Bootstrap modal for login form.
    """

    # =========================================================
    # LOCATORS - All element locators for Login page
    # =========================================================

    # Navigation
    LOGIN_NAV_LINK = (By.ID, "login2")
    SIGNUP_NAV_LINK = (By.ID, "signin2")
    LOGOUT_NAV_LINK = (By.ID, "logout2")
    WELCOME_USER = (By.ID, "nameofuser")