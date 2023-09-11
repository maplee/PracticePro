import subprocess
import time

def execute_adb_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(e)

def start_app(package_name, activity_name):
    execute_adb_command(f"adb shell am start -n {package_name}/{activity_name}")

def stop_app(package_name):
    execute_adb_command(f"adb shell am force-stop {package_name}")


def clear_app(package_name):
    execute_adb_command(f"adb shell pm clear {package_name}")


if __name__ == "__main__":
    package_name = "com.mogo.launcher.f"
    activity_name = "com.mogo.eagle.core.function.main.MainLauncherActivity"  # 替换为实际的 Activity 类名

    while True:
        # 启动应用程序
        print("Starting the app...")
        start_app(package_name, activity_name)
        time.sleep(8)  # 等待60秒，即1分钟

        # 关闭应用程序
        print("Stopping the app...")
        stop_app(package_name)
        time.sleep(1)  # 等待60秒，即1分钟
