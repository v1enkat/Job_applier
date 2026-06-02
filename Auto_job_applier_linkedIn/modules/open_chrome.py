import time

from modules.helpers import get_default_temp_profile, make_directories
from config.settings import run_in_background, stealth_mode, disable_extensions, safe_mode, file_name, failed_file_name, logs_folder_path, generated_resume_path
from config.questions import default_resume_path
if stealth_mode:
    import undetected_chromedriver as uc
else:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from modules.helpers import find_default_profile_directory, critical_error_log, print_lg, get_installed_chrome_major_version
from selenium.common.exceptions import SessionNotCreatedException

options, driver, actions, wait = None, None, None, None


def _build_chrome_options():
    opts = uc.ChromeOptions() if stealth_mode else Options()
    if run_in_background:
        opts.add_argument("--headless")
    if disable_extensions:
        opts.add_argument("--disable-extensions")
    opts.add_argument("--no-first-run")
    opts.add_argument("--no-default-browser-check")
    opts.add_argument("--disable-popup-blocking")
    return opts


def _apply_profile(opts, isRetry: bool = False):
    profile_dir = find_default_profile_directory()
    if isRetry or safe_mode or not profile_dir:
        guest_dir = get_default_temp_profile()
        make_directories([guest_dir])
        if isRetry:
            print_lg("Will login with a guest profile, browsing history will not be saved in the browser!")
        else:
            print_lg("Logging in with a guest profile, Web history will not be saved!")
        opts.add_argument(f"--user-data-dir={guest_dir}")
    else:
        opts.add_argument(f"--user-data-dir={profile_dir}")


def _create_chrome_driver(opts):
    if stealth_mode:
        print_lg("Starting Chrome (undetected mode)...")
        chrome_major = get_installed_chrome_major_version()
        if chrome_major:
            print_lg(f"Detected installed Chrome major version: {chrome_major}. Pinning undetected-chromedriver to it.")
            return uc.Chrome(options=opts, version_main=chrome_major, use_subprocess=True)
        print_lg("Could not auto-detect installed Chrome version; letting undetected-chromedriver pick the latest.")
        return uc.Chrome(options=opts, use_subprocess=True)
    return webdriver.Chrome(options=opts)


def _cleanup_chrome_session(partial_driver=None):
    if partial_driver is None:
        return
    try:
        partial_driver.quit()
    except Exception:
        pass
    try:
        if partial_driver.service and partial_driver.service.process:
            partial_driver.service.process.kill()
    except Exception:
        pass


def createChromeSession(isRetry: bool = False):
    make_directories([file_name, failed_file_name, logs_folder_path + "/screenshots", default_resume_path, generated_resume_path + "/temp"])
    print_lg("IF YOU HAVE MORE THAN 10 TABS OPENED, PLEASE CLOSE OR BOOKMARK THEM! Or it's highly likely that application will just open browser and not do anything!")

    opts = _build_chrome_options()
    _apply_profile(opts, isRetry)

    partial_driver = None
    try:
        partial_driver = _create_chrome_driver(opts)
        partial_driver.maximize_window()
        session_wait = WebDriverWait(partial_driver, 5)
        session_actions = ActionChains(partial_driver)
        return opts, partial_driver, session_actions, session_wait
    except SessionNotCreatedException:
        _cleanup_chrome_session(partial_driver)
        raise


def init_chrome():
    '''
    Opens Chrome only when the bot is ready to use it (called from main()).
    Retries once with a fresh guest profile if the first session fails.
    '''
    global options, driver, actions, wait
    if driver is not None:
        return

    print_lg("Opening Chrome browser...")
    try:
        options, driver, actions, wait = createChromeSession()
    except SessionNotCreatedException as e:
        critical_error_log("Failed to create Chrome Session, retrying with guest profile", e)
        time.sleep(2)
        options, driver, actions, wait = createChromeSession(True)
    except Exception as e:
        msg = 'Seems like Google Chrome is out dated. Update browser and try again!\n\nIf issue persists, try Safe Mode: set safe_mode = True in config/settings.py'
        if isinstance(e, TimeoutError):
            msg = "Couldn't download Chrome-driver. Set stealth_mode = False in config!"
        print_lg(msg)
        critical_error_log("In Opening Chrome", e)
        from pyautogui import alert
        alert(msg, "Error in opening chrome")
        _cleanup_chrome_session(driver)
        driver = None
        raise SystemExit(1) from e

    print_lg("Chrome ready. Navigating to LinkedIn...")
    driver.get("https://www.linkedin.com/login")
    return options, driver, actions, wait
