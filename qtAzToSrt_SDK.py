# 使用 Pydub 套件透過 FFmpeg 將各種視頻轉檔為 .wav 檔案。
    # qt 程式執行的時候不輸入 key 可以單純測試轉 .wav 檔案。
    # 目前測試可用的檔案包含 .wav .mp4 .avi .mpg 
    # Pydub 是依賴 FFmpeg 轉檔，所以照理 FFmpeg 所支援的檔案應該都可以轉。
    # 有興趣測試的可在選擇【開啓檔案】時，右邊的檔案()選擇【所有檔案(*.*)】來測試更多檔案類型。
class pyFFmpegPydub():
    # 建立ffmpeg_output資料夾。
    def mkdir(path):
        import os
        #判斷目錄是否存在
        #存在：True
        #不存在：False
        folder = os.path.exists(path)
    
        #判斷結果
        if not folder:
            #如果不存在，則建立新目錄
            os.makedirs(path)
            print(path)
            print('-----建立目錄成功-----')
    
        else:
            #如果目錄已存在，則不建立，提示目錄已存在
            print(path)
            print('-----目錄已經存在-----')
    # 以下是用法
    # path = 'd:\\xxoo\\test'
    # path = 'ffmpeg_output'
    # mkdir(path)    

    def pydubToWav(FDpath_from,FDpath_export,FDpath_rate):    
        print("轉檔來源：" + FDpath_from)
        print("轉出檔案：" + FDpath_export)
        print("設定採樣率：" + str(FDpath_rate))
        print("---------------------------------")
        from pydub import AudioSegment     # 載入 pydub 的 AudioSegment 模組
        print('開始轉檔...') 
        
        #採樣建議用22050，yanjie 程式暫時用 16000 為主。
        # song = AudioSegment.from_file("5.自製教學視頻_PianoDemo_15秒.mp4").set_frame_rate(16000) # set_frame_rate 設定採樣率。
        song = AudioSegment.from_file(FDpath_from).set_frame_rate(FDpath_rate) # set_frame_rate 設定採樣率。

        # r_file = song.export("5.自製教學視頻_PianoDemo_15秒.mp4.wav", format="wav") #如果不設定 format="wav" ，預設是 mp3 格式。
        r_file = song.export(FDpath_export, format="wav") #如果不設定 format="wav" ，預設是 mp3 格式。
        # r_file = "<檔案>"
        # print('轉換完成'+ str(r) ) 
        # channels = song.channels                      # 讀取聲道數量
        duration = song.duration_seconds                # 讀取長度
        frame_rate = song.frame_rate
        # print("音軌："+ str(channels))
        print("長度："+ str(duration)+"秒")       
        print("採樣率："+ str(frame_rate))        
        import time
        time.sleep(2) # 雖然程式應該是轉檔後，才會繼續下一步，但這裏 yan jie 還是 sleep 等一下不那麽急。

        return str(r_file)
        
    
#檔案路徑分割
class pyPathPart(): 
    # 用法
    # from qtAzToSrt_SDK import pyPathPart as SDK_Path
    # self.textEdit.append("路徑：" + SDK_Path.path(file_path))
    #檔案的路徑        
    def path(file_path):
        import os                
        file_path_path = os.path.split(file_path)[0]  # 路徑不含檔名。
        file_path_path = file_path_path.replace("/","\\") + "\\"
        return file_path_path
    
    #檔案的名稱        
    def name(file_path):
        import os
        file_path_name = os.path.split(file_path)[1]  # 檔名包含副檔名
        file_path_name_left = os.path.splitext(file_path_name)[0] # 檔名【不】包含副檔名
        return file_path_name_left
    
    #檔案的副檔名      
    def nameEx(file_path):
        import os
        file_path_name = os.path.split(file_path)[1]  # 檔名包含副檔名
        file_path_name_right = os.path.splitext(file_path_name)[1] # 檔名【不】包含副檔名
        return file_path_name_right 
    
    #找出目前程式所在路徑    
    def nowPath():    
        import pathlib
        now_path = str(pathlib.Path().absolute())+"\\" #目前程式所在路徑
        return now_path
    
    #開檔案：輸出資料(目前用在輸出字幕) or (Azure 取得的 json 格式資料)。
    def fileWrite(filePath,fileStr): #寫出檔案的filePath(完整路徑+檔名+副檔名)，fileStr(文件内容)。       
        try:
            f = open(filePath, 'w' , encoding="utf-8")    
            f.write(fileStr)
            f.close()            
        except IOError:
            print('ERROR: can not found ' + filePath)
            if f:
                f.close()
        finally:
            if f:
                f.close()
                
    #開檔案：讀取檔案全部的字串。目前用在讀取 WLTS 的 json格式。(只在測試時使用)
    def fileRead(filePath): #寫出檔案的filePath(完整路徑+檔名+副檔名)，fileStr(文件内容)。       
        try:
            f = open(filePath, 'r',encoding="utf-8")
            fileStr = f.read() #讀取檔案全部的字串。 
            f.close()                      
        except IOError:
            print('ERROR: can not found ' + filePath)
            if f:
                f.close()
        finally:
            if f:
                f.close()  
        return fileStr
                
        
    
class pyAzWLST():
    # 用法：上面的 init , add 等是測試資料。
    # from qtAzToSrt_SDK import pyAzWLST as SDK_WLST    
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    # self.lineEdit.setText(self.lineEdit.text() + str(SDK_WLST(3,4).add()))
    def add(self):
        sum=self.x+self.y
        return sum

    # self.lineEdit.setText(self.lineEdit.text() + str(SDK_WLST.add2(2,3)))     
    def add2(x,y):
        sum= x + y
        return sum

    #process_WLTS  程式——開始 start ===========================================
    def process_WLTS(az_key,az_region,az_locale,az_audio_filepath):
        import azure.cognitiveservices.speech as speechsdk
        import time        
        print("Speech to text request received")
    
        # speechapi_settings =  SpeechAPIConf()    
        # audio_filepath = "rain中文.wav"
        # audio_filepath = "按摩四句.wav"
        # audio_filepath = "中間間隔十秒不説話.wav"
        # audio_filepath = "許院長開幕致詞.wav"
        # audio_filepath = "許院長開幕致詞3mb.wav"
        audio_filepath = az_audio_filepath #使用 process_WLTS 參數。
        # locale = "zh-TW" # Change as per requirement 根據要求更改
        locale = az_locale # 使用 process_WLTS 參數。
    
        print(audio_filepath)
        audio_config = speechsdk.audio.AudioConfig(filename=audio_filepath) 
        # speech_config = speechsdk.SpeechConfig(subscription="bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", region="eastus")
        speech_config = speechsdk.SpeechConfig(subscription=az_key, region=az_region)
        speech_config.request_word_level_timestamps()
        speech_config.speech_recognition_language = locale
        speech_config.set_profanity(speechsdk.ProfanityOption.Raw) #Raw：一字不差地包含不雅字詞。
        
        # https://stackoverflow.com/questions/62554058/subtitles-captions-with-microsoft-azure-speech-to-text-in-python
        # speech_config.enable_dictation() #啟用聽寫。僅支持語音連續識別。例如，話語“你住在城裡問號”將被解釋為文本“你住在城裡嗎？”。
        speech_config.output_format = speechsdk.OutputFormat(1) #原始程式碼，不用這行時也一樣只有一句
        # speech_config.output_format = speechsdk.OutputFormat(0) #也一樣只有一句
    
        # Creates a recognizer with the given settings
        # 使用給定的設置創建一個識別器
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    
        # Variable to monitor status
        # 監控狀態的變量
        done = False
      
        # Service callback for recognition text 
        # 識別文本的服務回調
        transcript_display_list = []
        transcript_ITN_list = []
        confidence_list = []
        words = []
        def parse_azure_result(evt):
            import json
            response = json.loads(evt.result.json)
            transcript_display_list.append(response['DisplayText'])
            confidence_list_temp = [item.get('Confidence') for item in response['NBest']] #
            # confidence_list_temp = [item.get('Confidence') for item in ['NBest'][0]['Words']] #不能用。       
            max_confidence_index = confidence_list_temp.index(max(confidence_list_temp))
            confidence_list.append(response['NBest'][max_confidence_index]['Confidence'])
            transcript_ITN_list.append(response['NBest'][max_confidence_index]['ITN'])
            words.extend(response['NBest'][max_confidence_index]['Words'])
            # print(evt)
    
        # Service callback that stops continuous recognition upon receiving an event `evt`
        # 在接收到事件 `evt` 時停止連續識別的服務回調
        def stop_cb(evt):
            print('CLOSING on {}'.format(evt))
            speech_recognizer.stop_continuous_recognition()
            nonlocal done
            done = True
    
            # Do something with the combined responses
            # 對合併的響應做一些事情
            print(transcript_display_list) #辨識結果字串。列['你好，今天是下雨天。']
            print(confidence_list)  
            print(words)                   #全部word_level_timestamps 的 json結果。
    
            #開檔案輸出資料,=>qt SDK 中寫檔案改成只有回傳字串。        
            global Str_Output_process_WLTS #記錄輸出檔案的内容文字。以後可以在程式裏面做回傳。這裏回傳需要用全域變數。
            Str_Output_process_WLTS = "" #記錄輸出檔案的内容文字。以後可以在程式裏面做回傳。
            Str_Output = "" #記錄輸出檔案的内容文字。以後可以在程式裏面做回傳。        
            try:
                # path = audio_filepath + '_WLTS.txt'
                # f = open(path, 'w' , encoding="utf-8")
                
                import json            
                Str_tdlist = "".join(transcript_display_list) # transcript_display_list = ["a", "b", "c"] #結果字串         
                Str_Output += "!transcript_start!" + Str_tdlist + "!transcript_end!" 
                # f.write("!transcript_start!" + Str_tdlist + "!transcript_end!")
    
                Str_words = json.dumps(words,ensure_ascii=False)
                Str_Output += "!words_start!" + Str_words +"!words_end!"
                # f.write("!words_start!" + Str_words +"!words_end!") 
                
                # f.write(Str_Output)
                Str_Output_process_WLTS = Str_Output
                # f.close()  
            except:
                print('Str_Output_process_WLTS ERROR')
# =============================================================================
#             except IOError:
#                 print('ERROR: can not found ' + path)
#                 if f:
#                     f.close()
#             finally:
#                 if f:
#                     f.close()        
# =============================================================================
    
    
        # Connect callbacks to the events fired by the speech recognizer
        # 將回調連接到語音識別器觸發的事件
        # speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt))) #過程log    
        speech_recognizer.recognizing.connect(lambda evt: print(".",end = '',flush = True)) #過程log，Yanjie取代。
        speech_recognizer.recognized.connect(parse_azure_result) #每一段辨識結果。
        speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt))) 
        speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
        # speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
        speech_recognizer.canceled.connect(lambda evt: print("CANCELED",end = '',flush = True)) #Yanjie取代。
       
        # stop continuous recognition on either session stopped or canceled events
        # 在會話停止或取消的事件上停止連續識別
        speech_recognizer.session_stopped.connect(stop_cb)
        # speech_recognizer.canceled.connect(stop_cb)
        speech_recognizer.canceled.connect("") #Yanjie取代。
    
        # Start continuous speech recognition
        print("Initiating speech to text")
        speech_recognizer.start_continuous_recognition()
        while not done:
            time.sleep(.5)
            # time.sleep(10)
            
        #記錄輸出檔案的内容文字。以後可以在程式裏面做回傳。這裏回傳需要用全域變數。
        return Str_Output_process_WLTS    
    
    #process_WLTS  程式——結束 end   =========================================== 




    #process_jsonToSub  程式——開始 start ===========================================    
    # 舊的方法：開啓【*_WLTS.txt】轉 Subtitle 字幕 
    # 新的方法：傳入 WLTS 的 json格式字串，傳出 轉好的 Subtitle 字幕。
    def process_jsonToSub(temp_StrAll):
        #將微妙轉換成正常的時間，準備轉換為字幕用的時間戳記。
        from datetime import time
        def time_from_ticks(ticks) -> time :
            microseconds_1 = ticks / 10
            microseconds_2 = microseconds_1 % 1000000
            seconds_1 = microseconds_1 / 1000000
            seconds_2 = seconds_1 % 60
            minutes_1 = seconds_1 / 60
            minutes_2 = minutes_1 % 60
            hours = minutes_1 / 60
            return time(int(hours), int(minutes_2), int(seconds_2), int(microseconds_2))  
    
        #字串相識比對函式，回傳相似度最大的【句尾】索引值。
        def str_similar(s_transA, s_list_words):
            import difflib     
            # print(s_transA)
            # print(s_list_words)    
            tempStr = "" 
            list_words_ratio = [] #記錄字串相識比對的值。
            list_words_Str = [] #目前串連的字串。
            for wnum in range(0,len(s_list_words)):	    
                tempStr += s_list_words[wnum]  
                list_words_ratio.append(round(difflib.SequenceMatcher(None, s_transA, tempStr).quick_ratio(),3))
                list_words_Str.append(tempStr)
                # print(str(wnum)+" "+str(list_words_ratio[wnum])+list_words_Str[wnum])		
                
            maxIndex = list_words_ratio.index(max(list_words_ratio)) #相似度最大的值之索引位置。    
            
            return maxIndex    
        '''
        # 函式回傳 n1+n2 的結果
        def add(n1, n2):
            result=n1+n2
            return result
            
        # 呼叫函式，取得回傳值
        value=add(1, 8)
        print(value) # 這裡我們會印出 9    
        '''
               
        try:   
            # 開啓檔案
            # f = open(temp_path, 'r',encoding="utf-8")
            #讀取檔案全部的字串。已經改爲傳來json格式，word_level_timestamps()  
            WLTStemp_StrAll = temp_StrAll   
            # print(WLTStemp_StrAll+"\n")
            
            WLTStemp_StrSplit   = WLTStemp_StrAll.split("!transcript_end!!words_start!") #分割全部的字串
            WLTStemp_transcript = WLTStemp_StrSplit[0].replace("!transcript_start!" , "") #取出transcript字串，例如：【你好，今天是下雨天。】
            WLTStemp_transcript = WLTStemp_transcript.replace("。","，") #句號取代逗號，例如：【你好，今天是下雨天，】
            if WLTStemp_transcript[len(WLTStemp_transcript)-1] == "，" : WLTStemp_transcript = WLTStemp_transcript[:-1] #去掉結尾的逗號，，例如：【你好，今天是下雨天】    
            WLTStemp_words      = WLTStemp_StrSplit[1].replace("!words_end!" , "") #取出words字串，json格式。[{"Word": "你好", "Offset": 8700000, ....}]
            print("【原全文】" + WLTStemp_transcript + "【#句號取代逗號，分割用逗號】") #transcript 字串
            # print(WLTStemp_words)    #words      字串，JSON String 的 時間戳記。
              
            # 將JSON String轉換成List<Dictionary>
            print("---------------------------------------------")
            print("---- 將JSON String轉換成List<Dictionary> ----\n")
            import json
            # word='[{"Name":"Jennifer", "Age":"30"}, {"Name":"Bill", "Age":"1"}]' 
            # list_words = json.loads(word)        
            
            list_words = json.loads(WLTStemp_words) #json 字組 + 時間戳記 + 持續時間。
            list_words_start = [] #記錄開始時間(字組)，轉換成字幕格式時間戳記。   
            list_words_end = []   #記錄結束時間(字組)，轉換成字幕格式時間戳記。 
            # print(len(list_words))
            print("  字組 \t\t開始時間 \t\t結束時間")
            for lnum in range(0,len(list_words)): # print(list_words[0]['Word'] + str(list_words[0]['Offset']))           
                time_format = "%H:%M:%S,%f"
                
                #開始時間，時間戳記(微秒)轉 -> 字幕格式時間戳記。例如：1672900000 => 00:02:47,290
                ticks_mil_start = list_words[lnum]['Offset'] #1672900000
                ts_start = time_from_ticks(ticks_mil_start).strftime(time_format)[:-3] #開始時間，字幕格式時間戳記。
                list_words_start.append(ts_start) #用list記錄開始時間，方便後面存取出。
                
                #結束時間，時間戳記(微秒)轉 -> 字幕格式時間戳記。1768500000 + 4800000 => 00:02:57,330
                ticks_mil_end = list_words[lnum]['Offset'] + list_words[lnum]['Duration'] #29900000 + 12900000
                ts_end = time_from_ticks(ticks_mil_end).strftime(time_format)[:-3] #結束時間，字幕格式時間戳記。
                list_words_end.append(ts_end) #用list記錄結束時間，方便後面存取出。
                
                print(lnum, end = ' ')
                print(list_words[lnum]['Word'] , end = ' \t\t') 
                print(str(list_words_start[lnum]) , end = ' \t') #Offset 與 Duration 是 int 可以相加。
                # print(str(list_words[lnum]['Duration']) , end = ' \t') #字組持續時間，
                print(str(list_words_end[lnum]) + " ") #可以找出結束的時間戳記。
    
            #試以 list_transcript 為基準比對list_words
            print("---------------------------------------------")        
            list_transcript = WLTStemp_transcript.split("，") #分割，用逗號【，】分割每一句。
            firNum  = 0 #記錄每一句的開始位置。每一句句首。
            nowNum  = 0 #記錄 list_words 目前位置。找每一句句尾用的指標。
            tempStr = ""
            list_outTemp = [] #記錄準備輸出的時間戳記，和原句分割的每一句。
            # tempStr = list_words[nowNum]['Word']
            
            for lnum in range(0,len(list_transcript)): #python range 後面自己會減1。            
                print("【原" + str(lnum) + "句】"+list_transcript[lnum] + "\t\t" , end=" ")
     
                try:
                    # 邏輯合理但先不用。因爲原句和合并句子字不一樣
                    firNum = nowNum
                    while tempStr != list_transcript[lnum]:
                        tempStr += list_words[nowNum]['Word']
                        nowNum += 1
                    print("【句尾】" + list_words[nowNum-1]['Word'] , end="\n") 
                    outTemp_time = list_words_start[firNum] + " --> " + list_words_end[nowNum-1]
                    print("【時戳】" + outTemp_time)
                    tempStr = ""  
                    print("try:" + str(nowNum))
                                    
    
                except:
                    nowNum = firNum #nowNum在try的時候超出索引。拉回當句句首。
                    tempStr = "" #同nowNum
                    # print("ex" + str(firNum))
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ex:" + str(nowNum))
                    
                    simNum = 0 #回傳相似度最大的【句尾】索引值。
                    # simNum = str_similar(transA,list_words)
                    T_list_words = [] #將list_words[]['Word']的字串暫存到這，作為參數傳送到str_similar()
                    for wnum in range(firNum,len(list_words)):                
                        # print(str(wnum) + " " + str(list_words[wnum]['Word']))
                        T_list_words.append(list_words[wnum]['Word'])                    
                        
                    simNum = str_similar(list_transcript[lnum],T_list_words) #回傳【句尾】索引值。
                    # print(str(simNum)) #17
                    # print(list_transcript[lnum])
                    nowNum = firNum + simNum + 1
                    print("【句尾】" + list_words[nowNum-1]['Word'] , end="\n")
                    outTemp_time = list_words_start[firNum] + " --> " + list_words_end[nowNum-1]
                    print("【時戳】" + outTemp_time +"\n")                
                    # return
    
                #記錄準備輸出的時間戳記，和原句分割的每一句。list_outTemp.append(["時間戳記1","句子1"])
                list_outTemp.append([outTemp_time,list_transcript[lnum]]) #["時間戳記1","句子1"]
                # print("\t字幕格式check:"+list_outTemp[lnum][0]+ " " +list_outTemp[lnum][1])                
            
            print("=====================================================")
            print("================= 轉換為字幕格式 =====================\n")
            finall_outTemp = ""
            for lnum in range(0,len(list_outTemp)):
                finall_outTemp += str(lnum+1) + "\n"
                finall_outTemp += list_outTemp[lnum][0]+ "\n" + list_outTemp[lnum][1]+ "\n\n"
            # print(finall_outTemp)#準備 return 最終字幕
            return finall_outTemp #回傳 return 最終字幕
        
        except IOError:
            print('ERROR: can not found ')    
    #process_jsonToSub  程式——結束 end   =========================================== 
         
    
    
    