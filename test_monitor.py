import cv2
import subprocess

# FFmpeg命令，设置为RTSP流
command = [
    'ffmpeg',
    '-y',  # 覆盖输出文件
    '-f', 'rawvideo',
    '-pix_fmt', 'bgr24',
    '-s', '640x480',
    '-r', '30',
    '-i', '-',
    '-c:v', 'libx264',
    '-f', 'rtsp',
    'rtsp://localhost:8554/live.sdp'
]

# 启动FFmpeg进程
process = subprocess.Popen(command, stdin=subprocess.PIPE)

# 打开摄像头
cap = cv2.VideoCapture(0)  # 0表示默认摄像头
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("无法读取视频帧")
            break

        # 确保帧大小与FFmpeg设置的分辨率匹配
        frame = cv2.resize(frame, (640, 480))

        # 将帧写入FFmpeg的标准输入
        process.stdin.write(frame.tobytes())

        # 显示实时视频
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    print("监控已停止")

# 释放资源
cap.release()
process.stdin.close()
process.wait()
cv2.destroyAllWindows()
