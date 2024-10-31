import subprocess

config_path = "E:\\Video\\mediamtx_v1.9.3_windows_amd64\\mediamtx.yml"
mediamtx_command = [
    "E:\\Video\\mediamtx_v1.9.3_windows_amd64\\mediamtx.exe",
    "-config",
    config_path
]

try:
    process = subprocess.Popen(mediamtx_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # 获取输出
    stdout, stderr = process.communicate()

    if stdout:
        print("STDOUT:", stdout.decode())
    if stderr:
        print("STDERR:", stderr.decode())
except Exception as e:
    print("Error:", str(e))
