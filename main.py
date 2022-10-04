from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFrame
import sys
from Ui_win import Ui_Form # 把win的類匯入讓這邊可以用
 
class MainFrame(QFrame, Ui_Form):
    #AzKey，AzRegion,全域變數。
    set_AzKey    = ""
    set_AzRegion = "" 
    
    def __init__(self, parent=None):
        super(MainFrame, self).__init__(parent) # 調用父類把子類對象轉為父類對象     
        # 調用介面
        self.setupUi(self) 
        
        # 信號         
        self.pushButton_importKeyRegion.clicked.connect(self.calculation_importKeyRegion) # 信號與槽連接
        self.pushButton_OpenFile.clicked.connect(self.calculation_OpenFile) # 信號與槽連接
        self.pushButton_Transcribe.clicked.connect(self.calculation_Transcribe) # 信號與槽連接
        self.pushButton.clicked.connect(self.calculation) # 信號與槽連接
        self.pushButton.setGeometry(QtCore.QRect(390, 400, 104, 0)) ##設定後面 0，0 讓 pushButton 按鈕消失。
        self.lineEdit.setGeometry(QtCore.QRect(20, 430, 481, 0))   ##設定後面 0 讓 lineEdit 文字方塊消失。
        # pushButton_TransSub
        self.pushButton_Transcribe.setGeometry(QtCore.QRect(390, 360, 104, 0)) ##連線轉換 ##設定後面 0，0 讓 pushButton 按鈕消失。
        self.pushButton_TransSub.clicked.connect(self.calculation_TransSub) # 信號與槽連接
       
    # 【匯入 Key / Region】按鈕
    # 自訂槽函數_匯入AzKey，AzRegion，目前暫時放程式裏面。
    def calculation_importKeyRegion(self):     
        #從 config.json 匯入 AzureSubscriptionKey 和 AzureServiceRegion        
        path = "config.json" 
        f = None
        try: 
            # 開啓檔案
            # f = open(path, 'r',encoding="utf-8") #都是英文的檔案可能不需要 utf-8
            f = open(path, 'r')
            self.textEdit.append("從 config.json 檔匯入 Key / Region \n")
            
            import json
            #json 的資料形式字串
            # strjson = '{"firstName": "Allen", "lastName":"Chen"}'
            strjson = f.read()
            #轉換json
            parsedJson = json.loads(strjson)
            # print(parsedJson['AzureSubscriptionKey']) 
            # print(parsedJson['AzureServiceRegion'])
            self.set_AzKey = parsedJson['AzureSubscriptionKey']
            self.set_AzRegion = parsedJson['AzureServiceRegion']
            f.close()            
        except IOError:
            print('ERROR: can not found ' + path)
            self.textEdit.append("匯入失敗\n")
            if f:
                f.close()
        finally:
            if f:
                f.close()
                
        self.lineEdit_AzKey.setText(self.set_AzKey) #全域變數 AzKey。
        self.lineEdit_AzRegion.setText(self.set_AzRegion) #全域變數 AzRegion。      
        
    # 【開啓檔案】按鈕
    # 自訂槽函數_開啓檔案
    def calculation_OpenFile(self): 
        #開啓檔案路徑與檔名。
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        #完整的路徑+檔名+副檔名
        file_path = filedialog.askopenfilename(parent=root, title='選擇檔案', filetypes=(("檔案","*.wav;*.mp4;*.avi;*.mpg"),("所有檔案","*.*")))
        if file_path == "":return #如果開啓檔案，選擇取消。
        
        #路徑與檔名
        import os 
        file_path_path = os.path.split(file_path)[0]  # 路徑不含檔名。['/home/ubuntu/python', 'example.py']  的第二個欄位
        file_path_name = os.path.split(file_path)[1]  # 檔名包含副檔名
        file_path_name_left = os.path.splitext(file_path_name)[0] # 檔名【不】包含副檔名
       
        self.lineEdit_FilePath.setText(file_path) #顯示檔案路徑
        self.lineEdit_FileOutput.setText(file_path_path+"/"+file_path_name_left+".srt") #顯示輸出路徑
        
        # self.lineEdit.setText(file_path_path)
        # self.textEdit.append(file_path_name)
        # self.textEdit.append(file_path_name_left)

    # v2版本使用先留著。按鈕關閉。
    # 自訂槽函數_轉換。
    def calculation_Transcribe(self):          
        self.textEdit.append("轉換過程：")
        #執行轉換字幕的指令。
        cmd_str = "<now_path>captioning.exe --key <key> --region <region> --input <inputFile> --output <outputFile> --srt --recognizing --threshold 3 --profanity raw --phrases \"Contoso;Jessie;Rehaan\" --languages zh-TW"
        cmd_str = cmd_str.replace('<key>', self.lineEdit_AzKey.text()) #指令 <key>
        cmd_str = cmd_str.replace('<region>', self.lineEdit_AzRegion.text()) #指令 <region>

        #找出目前程式所在路徑
        import pathlib
        #print(str(pathlib.Path().absolute())+"\\")
        now_path = str(pathlib.Path().absolute())+"\\" #目前程式所在路徑
       
        # self.lineEdit.setText("程式所在路徑："+now_path)
        # cmd_str = cmd_str.replace('<now_path>', now_path) #指令 <now_path>
        # 微軟源碼執行檔路徑前後加上 【""】 在程式執行還是不能用。不能處理路徑空白不能識別的 bug。
        # cmd_str = cmd_str.replace('<now_path>captioning.exe', "\""+now_path+"captioning.exe\"") #指令 <now_path> #處理路徑空白不能識別的 bug。
        cmd_str = cmd_str.replace('<now_path>', "") #指令 <now_path> now_path 不要用程式路徑反而可以，處理路徑空白不能識別的 bug。 

        #輸入檔案的路徑 <inputFile>，和輸出檔案的路徑 <outputFile>        
        if self.lineEdit_FilePath.text() == "":#如果沒有【開啓檔案】，路徑是空的。
            self.textEdit.append("還沒【開啓檔案】\n")
            return
        self.textEdit.append("目前程式的路徑 <now_path>")
        self.textEdit.append(now_path +"\n")
        
        self.textEdit.append("輸入檔案的路徑 <inputFile>")
        self.textEdit.append(self.lineEdit_FilePath.text()+"\n")
        # cmd_str = cmd_str.replace('<inputFile>', self.lineEdit_FilePath.text()) #指令 <inputFile>
        cmd_str = cmd_str.replace('<inputFile>', "\""+self.lineEdit_FilePath.text()+"\"") #指令 <inputFile>
        
        self.textEdit.append("輸出檔案的路徑 <outputFile>")
        self.textEdit.append(self.lineEdit_FileOutput.text()+"\n")
        # cmd_str = cmd_str.replace('<outputFile>', self.lineEdit_FileOutput.text()) #指令 <outputFile>
        cmd_str = cmd_str.replace('<outputFile>', "\""+self.lineEdit_FileOutput.text()+"\"") #指令 <outputFile>

        #yanjie here home hh
        # self.textEdit.append(self.lineEdit_AzKey.text())
        # self.textEdit.append(self.lineEdit_AzRegion.text())
        self.textEdit.append("轉換指令如下：")        
        self.textEdit.append(cmd_str+"\n")
        
        #使用微軟的 Azure 開源碼 captioning.exe 進行字幕轉化
        import os    
        #os.system("Transcribe.bat")    
        #os.system(str(now_path)+"Transcribe.bat")
        # os.system("captioning.exe")
        os.system(cmd_str)
        self.textEdit.append("==============  執行結束  ==============") 


    # v2版本使用先留著。按鈕關閉。
    # 自訂槽函數_測試 ansi to utf-8 , 去除"[zh-TW] "字串。
    def calculation(self):  
        #.setText方法讓文字顯示在lineEdit上
        #self.lineEdit.setText(self.lineEdit.text() +'彥杰\n') 
        self.textEdit.setText("")
        self.textEdit.append("開始轉換成【utf-8】格式的 srt 字幕檔案\n")
        
        #檔案格式整理:start ==========> ansi to utf-8 , 去除"[zh-TW] "字串。
        # path = '許院長開幕致詞.srt' 
        path = self.lineEdit_FileOutput.text() #輸出檔案的路徑 <outputFile>
        f = None
        try: 
            # 開啓檔案
            # f = open(path, 'r',encoding="utf-8") # 檔案是ansi不是utf-8
            f = open(path, 'r')
            fileText = f.read()
            # print(fileText)
            
            fileText_TranOutput = fileText.replace('[zh-TW] ', '') #字串'[zh-TW] '的地方取代為空白
            print(fileText_TranOutput)          
            f.close()
            
            f = open(path, 'w' , encoding="utf-8")
            f.write(fileText_TranOutput)
            f.close()
            self.textEdit.append("轉換完成\n")
            
            
        except IOError:
            print('ERROR: can not found ' + path)
            self.textEdit.append("轉換失敗\n")
            if f:
                f.close()
        finally:
            if f:
                f.close()       
        #檔案格式整理:end ==========>

    # v3版【轉換字幕】按鈕。
    # 自訂槽函數_轉換字幕_微軟 docs 的 WLST 字級時間戳記轉字幕。
    def calculation_TransSub(self):
        # 測試用法
        # self.lineEdit.setText(self.lineEdit.text() +'彥杰\n') 
        # from qtAzToSrt_SDK import pyAzWLST as SDK_WLST
        # self.lineEdit.setText(self.lineEdit.text() + str(SDK_WLST.add2(2,3))) 
       
        #輸入檔案的路徑 <inputFile>，和輸出檔案的路徑 <outputFile>        
        if self.lineEdit_FilePath.text() == "":#如果沒有【開啓檔案】，路徑是空的。
            self.textEdit.append("還沒【開啓檔案】\n")
            return #yajie 測試時暫時不要，        
        
        #輸入檔案的：路徑 + 檔名 + 副檔名。（音頻檔案 .wav or .mp4）
        from qtAzToSrt_SDK import pyPathPart as SDK_Path        
        self.textEdit.append("目前程式的路徑：\n" + SDK_Path.nowPath() + "\n") #找出目前程式所在路徑
        file_path_input = self.lineEdit_FilePath.text() #輸入檔案的完整路徑，包含路徑 + 檔名 + 副檔名。
        file_P_path = SDK_Path.path(file_path_input)
        file_P_name = SDK_Path.name(file_path_input)
        file_P_nameEx = SDK_Path.nameEx(file_path_input)
        self.textEdit.append("輸入檔案的：路徑 + 檔名 + 副檔名")
        self.textEdit.append("路徑：" + file_P_path)
        self.textEdit.append("檔名：" + file_P_name)
        self.textEdit.append("副檔名：" + file_P_nameEx) #.wav or .mp4 未來判斷是否轉換。
 
        #如果不是 .wav 例如 .mp4 .avi .mpg 先進行轉檔成 .wav ============
        if file_P_nameEx != ".wav":
            self.textEdit.append("\n"+ file_P_nameEx + " 需要轉檔案...")
            from qtAzToSrt_SDK import pyFFmpegPydub as SDK_FFdub            
            # print(file_P_path + "ffmpeg_output")
            SDK_FFdub.mkdir(file_P_path + "ffmpeg_output") # 建立ffmpeg_output資料夾。
            
            FDpath_from   = file_P_path + file_P_name + file_P_nameEx #檔案來源
            FDpath_export = file_P_path + "ffmpeg_output\\" + file_P_name +".wav" #輸出檔案
            FDpath_rate   = 16000 #採樣率
           
            try:
                # 使用 Pydub 套件透過 FFmpeg 將各種視頻轉檔為 .wav 檔案。
                r_file = SDK_FFdub.pydubToWav(FDpath_from,FDpath_export,FDpath_rate)
                print(r_file + "\n\n轉檔完成。")
                self.textEdit.append("轉檔完成。")
            except:
                self.textEdit.append("視頻檔轉 .wav 失敗，請檢查檔案。")
                return 
            
            # return #20221001 寫完。
        # =============================================================
        
        #開檔案：讀取檔案全部的字串。目前用在讀取 WLTS 的 json格式。(只在測試時使用)
        # WLTS 檔案的路徑
        # file_path_WLTS = file_path_input + "_WLTS.txt"
        # WLTStemp_StrAll = SDK_Path.fileRead(file_path_WLTS) # WLTStemp_StrAll json格式字串。
        # print(WLTStemp_StrAll)
        
        
        # 使用 process_WLTS(和 Azure 要 json)，process_jsonToSub(json 轉字幕)
        print("連接 Azure 上傳檔案，要求取得 WLTS(字級時間戳記) ========================")
        from qtAzToSrt_SDK import pyAzWLST as SDK_WLST 
        # process_WLTS ====== start ======
        azure_key = self.lineEdit_AzKey.text()      #"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        azure_region = self.lineEdit_AzRegion.text() #"eastus"
        azure_locale = "zh-TW" 
        if file_P_nameEx == ".wav":       
            azure_audio_filepath = self.lineEdit_FilePath.text() #輸入檔案的路徑
        else:
            azure_audio_filepath = FDpath_export # 轉檔後的 .wav 檔案所在路徑   
        
        print(".wav 檔案所在路徑：" + azure_audio_filepath)
        # return # 放行後就連接 Azure + 開始轉換。！！！不輸入 key 可以單純轉檔。
            
        try:
            #連接 Azure(****** 和 Azure 要 json ******)            
            WLTStemp_StrAll = SDK_WLST.process_WLTS(azure_key,azure_region,azure_locale,azure_audio_filepath) 
        except:
            self.textEdit.append("\n連線失敗：請檢查 azure_key , azure_region , 路徑與檔案格式。")
            return
        # print(azure_key,azure_region,azure_locale,azure_audio_filepath)

        # process_WLTS ======  end  ======      


     
        
        #輸出檔案的路徑直接用 lineEdit 上的。
        #開檔案：輸出資料(目前用在輸出字幕) or (Azure 取得的 json 格式資料)。
        # process_jsonToSub ====== start ======        
        file_path_output = self.lineEdit_FileOutput.text() #輸出檔案的路徑             
        # fileStr_output = "輸出資料\n你好\n今天很可以。\n謝謝"
        try:
            #(****** json 轉字幕 ******)
            fileStr_output = SDK_WLST.process_jsonToSub(WLTStemp_StrAll) 
            SDK_Path.fileWrite(file_path_output, fileStr_output) #寫出檔案的filePath(完整路徑+檔名+副檔名)，fileStr(文件内容)。
            print(fileStr_output)
            self.textEdit.append("\n轉字幕完成。")
        except:
            self.textEdit.append("\n轉字幕失敗：請檢查 azure_key , azure_region , 路徑與檔案格式。")
            return        
        
        # process_jsonToSub ======  end  ======        
        
        
        # import os    
        # os.system("@ping 127.0.0.1 -n 5 -w 1000 > nul")
        # aaa = os.system("pause")
        # self.textEdit.append("已經等了5秒" + str(aaa))         
        


        
        

        

#-------- main  主程式如下  --------------------------------          
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainFrame = MainFrame()
    mainFrame.show()
    sys.exit(app.exec_())         

