# -*- coding: utf-8 -*-
from pyaudio import PyAudio, paInt16 
import numpy as np 
import wave 
import time

class VoiceDetector:
    def __init__(self):
        self.NUM_SAMPLES = 2000      # pyAudio内部缓存的块的大小
        self.SAMPLING_RATE = 8000    # 取样频率
        self.MAX_GAP_LENGTH=3
       # 开启声音输入
        self.pa = PyAudio() 
        self.energy_threshold=self.normalize_environment_threshold()

    def normalize_environment_threshold(self):
        print u"请保持安静，正在评估环境噪声,需要7s钟......"
        time.sleep(2)
        print u"请保持安静，正在评估环境噪声,需要5s钟......"  
        self.stream = self.pa.open(format=paInt16, channels=1, rate=self.SAMPLING_RATE, input=True, 
                        frames_per_buffer=self.NUM_SAMPLES)
        energy=0          
        for i in range(0,5):
           # 读入NUM_SAMPLES个取样
            string_audio_data = self.stream.read(self.NUM_SAMPLES) 
            # 将读入的数据转换为数组
            audio_data = np.fromstring(string_audio_data, dtype=np.short) 
            energy=energy+self.SoundEnergy(audio_data)
            print u"请保持安静，正在评估环境噪声,需要"+str(4-i)+u"s钟......"    
        self.stream.close()
        if energy <0 :
            return 0.1*energy#0.5*energy/5.0
        else:
            return 0.4*energy#2*energy/5.0    
        
    # 将data中的数据保存到名为filename的WAV文件中
    def save_wave_file(self,filename, data): 
        wf = wave.open(filename, 'wb') 
        wf.setnchannels(1) 
        wf.setsampwidth(2) 
        wf.setframerate(self.SAMPLING_RATE) 
        wf.writeframes("".join(data)) 
        wf.close() 

    def QueryVoice(self): 
        recording_flag=False
        save_flag=False
        current_gap_len=self.MAX_GAP_LENGTH
        save_buffer = [] 
        #print "initiate to Monitoring the Micphone...\n"
        print u"==========请提问/说话/聊天==========\n"    
        self.stream = self.pa.open(format=paInt16, channels=1, rate=self.SAMPLING_RATE, input=True, 
                        frames_per_buffer=self.NUM_SAMPLES)         
        while True: 
            # 读入NUM_SAMPLES个取样
            string_audio_data = self.stream.read(self.NUM_SAMPLES) 
            # 将读入的数据转换为数组
            audio_data = np.fromstring(string_audio_data, dtype=np.short) 
            energy=self.SoundEnergy(audio_data)
            if recording_flag==False and energy >0 :
                recording_flag=True
                print 'start recording'
            #检测语句结束
            if recording_flag==True and energy >0 :
                current_gap_len=self.MAX_GAP_LENGTH   
                
            if recording_flag==True and energy <0 :
                current_gap_len=current_gap_len-1
                print current_gap_len
                
            if recording_flag==True and current_gap_len <=0 :
                recording_flag=False   
                if len(save_buffer)>3:
                    save_flag=True
                    print 'stop recording and saving'
                else:#过短的录音不识别
                    save_flag=False
                    save_buffer=[] 
                    print 'repeat recording'
            
            if recording_flag==True:    
                # 将要保存的数据存放到save_buffer中
                save_buffer.append( string_audio_data ) 
        
            if save_flag==True: 
                self.save_wave_file("temp.wav", save_buffer)
                self.save_buffer = [] 
                save_flag=False
                print "temp.wav saved"
                self.stream.close()
                return True

    def SoundEnergy(self,audio_data):
        normalized_audio=audio_data/32767.0
        energy=np.fft.fft(normalized_audio)/len(normalized_audio)
        return np.log(np.sum(np.abs(energy)) )/np.log(20)
        
if __name__ == "__main__":          
    vd=VoiceDetector()
    print vd.energy_threshold
    vd.QueryVoice()