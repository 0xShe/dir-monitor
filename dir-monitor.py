import os
import time
import requests

def monitor_folder():
    folder_path = r'C:\\Users\\'  # 监控的文件夹路径 路径使用双斜杠
    log_file = 'Test.log'  # 日志文件路径

    # 在第一次启动时，保存目录下的所有文件到日志文件
    with open(log_file, 'w') as f:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                f.write(os.path.join(root, file) + '\n')

    while True:
        # 读取之前保存的文件列表
        with open(log_file, 'r') as f:
            previous_files = set(f.read().splitlines())

        # 获取文件夹下的所有文件
        current_files = set()
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                current_files.add(os.path.join(root, file))

        # 获取新增的 可执行程序 文件
        new_php_files = current_files - previous_files
        new_php_files = [file for file in new_php_files if file.endswith(('.php', '.php5', '.php7'))] #后缀根据自己使用的语言进行修改

        # 如果有新增的 可执行程序 文件
        if new_php_files:
            with open(log_file, 'a') as f:
                f.write('\nDetected new 可执行程序 files:\n')
                f.write('\n'.join(new_php_files))
                f.write('\n')

            # 访问网站
            response = requests.get('https://sctapi.ftqq.com/自己server酱的key.send?title=Test&desp=Test')
            if response.status_code == 200:
                print('有入侵迹象 请查看日志')

        time.sleep(60)  # 60秒后再次检测

monitor_folder()
