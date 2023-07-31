import time
import pyautogui
import subprocess
import cv2
class BluetoothConnect(object):
    def open_settings_app():
        # Open the Settings app
        subprocess.run('start ms-settings:', shell=True)
        time.sleep(2)  # Allow time for the app to open

    def navigate_to_bluetooth():
        # Move the mouse to the search bar and click on it
        pyautogui.moveTo(800, 200)  # Adjust the coordinates according to your screen resolution
        pyautogui.click()

        # Type "Bluetooth" in the search bar and press Enter
        pyautogui.write('Bluetooth', interval=0.1)
        pyautogui.press('enter')
        time.sleep(2)  # Allow time for the Bluetooth settings to open
        pyautogui.moveTo(600, 200)
        pyautogui.click()

    def select_bluetooth_device(device_name):
        # Scroll down to find the "JBL Clip 3" device
        for _ in range(5):
            pyautogui.scroll(-1)  # Scroll up to locate the device
            time.sleep(0.5)

        # Locate and click on the "JBL Clip 3" device
        device_location = pyautogui.locateCenterOnScreen('jbl_clip_3.png', confidence=0.8)
        if device_location is None:
            print("Device 'JBL Clip 3' not found.")
            return False

        pyautogui.click(device_location)

        # Wait for the device page to load
        time.sleep(2)

        return True

    def tap_connect():
        # Find and click the "Connect" button
        time.sleep(2)
        connect_button_location = pyautogui.locateCenterOnScreen('connect_button.png', confidence=0.8)
        if connect_button_location is None:
            print("Connect button not found.")
            return False

        pyautogui.click(connect_button_location)
        time.sleep(2)

    def main_action():
        BluetoothConnect.open_settings_app()
        BluetoothConnect.navigate_to_bluetooth()
        if BluetoothConnect.select_bluetooth_device("JBL Clip 3"):
            BluetoothConnect.tap_connect()
        else:
            print("Failed to connect to 'JBL Clip 3'.")





