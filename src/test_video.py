import os
import subprocess
import time

# 启动 mediamtx
mediamtx_command = "E:\\Video\\mediamtx_v1.9.3_windows_amd64\\mediamtx.exe"
os.startfile(mediamtx_command)
time.sleep(1)


ffmpeg_command = [
    'ffmpeg',
    '-re',
    '-stream_loop', '-1',
    '-i', 'C:\\Users\\ASUS\\Desktop\\test_video\\assets\\xiaomi.mp4',
    '-c:v', 'libx264',
    '-f', 'rtsp',
    'rtsp://localhost:8554/live.sdp'  # RTSP 流地址
]

# 启动FFmpeg进程
process = subprocess.Popen(ffmpeg_command, stdin=subprocess.PIPE)

# 启动 VLC 播放 RTSP 流
vlc_command = [
    'E:\\Video\\VLC\\vlc.exe',  # VLC 的绝对路径
    'rtsp://localhost:8554/live.sdp'
]
subprocess.Popen(vlc_command)


