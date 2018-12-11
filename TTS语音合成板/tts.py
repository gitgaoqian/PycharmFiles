# -*- coding: utf-8 -*-
import serial
import time
class TTS():
    def __init__(self):
        self.ser=serial.Serial("/dev/ttyUSB0",9600,timeout=10)#芯片如何进行硬件配置波特率
        self.cmd_head = b'\xfd'
    def status_find(self):
        find_head = b'\xfd'
        find_len = b'\x00\x01'
        find_word = b'\x21'
        find_all = find_head+find_len+find_word
        self.ser.write(find_all)
        status=self.ser.read()
        return status
    def start_ttx(self):
        ChipStatus = self.status_find()
        if ChipStatus == b'O':#如果芯片处于空闲状态,设置一帧数据,进行语音合成
            self.cmd_encode = b'\x03'
            self.cmd_word = b'\x01'
            self.cmd_data = "西红柿".encode("utf-16")
            length = (len(self.cmd_data)+2)
            b=bytes([length])
            self.cmd_len = b'\x00'+b
            cmd_all = self.cmd_head + self.cmd_len + self.cmd_word + self.cmd_encode + self.cmd_data
            self.ser.write(cmd_all)
            ReturnData = self.ser.read()
            if ReturnData == b'E':
                print ("收到错误的命令帧！")
        elif ChipStatus == b'N':
            print ("芯片正在合成！")
    def stop_ttx(self):
        self.cmd_len = b'\x00\x01'
        self.cmd_word = b'\x02'
        cmd_all = self.cmd_head + self.cmd_len + self.cmd_word
        self.ser.write(cmd_all)
    def pause_ttx(self):
        self.cmd_head = b'\xfd'
        self.cmd_len = b'\x00\x01'
        self.cmd_word = b'\x03'
        cmd_all = self.cmd_head + self.cmd_len + self.cmd_word
        self.ser.write(cmd_all)
    def resume_ttx(self):
        self.cmd_len = b'\x00\x01'
        self.cmd_word = b'\x04'
        cmd_all = self.cmd_head + self.cmd_len + self.cmd_word
        self.ser.write(cmd_all)
    def PowerSaveMode(self):
        self.cmd_len = b'\x00\x01'
        self.cmd_word = b'\x88'
        cmd_all = self.cmd_head + self.cmd_len + self.cmd_word
        self.ser.write(cmd_all)
    def Wake(self):
        self.cmd_len = b'\x00\x01'
        self.cmd_word = b'\xff'
        cmd_all = self.cmd_head + self.cmd_len + self.cmd_word
        self.ser.write(cmd_all)
if __name__=="__main__":
    tts = TTS()
    tts.start_ttx()




