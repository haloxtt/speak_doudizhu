#coding=utf-8
import pyaudio
import numpy as np
from scipy import fftpack
import wave


def recording(filename, time=0, threshold=10000):
    """
    :param filename: 文件名
    :param time: 录音时间,如果指定时间，按时间来录音，默认为自动识别是否结束录音
    :param threshold: 判断录音结束的阈值
    :return:
    """
    CHUNK = 1024  # 块大小
    FORMAT = pyaudio.paInt16  # 每次采集的位数
    CHANNELS = 1  # 声道数
    RATE = 	16000  # 采样率：每秒采集数据的次数
    RECORD_SECONDS = 1000  # 录音时间
    WAVE_OUTPUT_FILENAME = filename  # 文件存放位置
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("start voice recording*****************************start .......")
    frames = []
    if time > 0:
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
    else:
        isBegin = 0
        end = 0
        while True:
            data = stream.read(CHUNK)
            rt_data = np.frombuffer(data, np.dtype('<i2'))
            # 傅里叶变换
            fft_temp_data = fftpack.fft(rt_data, rt_data.size, overwrite_x=True)
            fft_data = np.abs(fft_temp_data)[0:fft_temp_data.size // 2 + 1]

            # 测试阈值，输出值用来判断阈值
            print(sum(fft_data) // len(fft_data))

            # 判断麦克风是否停止，判断说话是否结束，# 麦克风阈值，默认10000
            if sum(fft_data) // len(fft_data) > threshold:
                isBegin += 1
            else:
                if isBegin > 0 :
                    break
            frames.append(data)
    print(" end voice recording ************** end voice recording")
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


# recording('/Users/xietaotao/Documents/编码奇才/秋名山街道监控探头/time.mp3', time=5)  # 按照时间来录音，录音5秒
# recording('output.wav')  # 没有声音自动停止，自动停止
