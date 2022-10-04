# Azure影片轉srt字幕工具v3 (qtAzToSrt v3)
**v3—20221003:更新**
* 支援轉檔(Pydub)：目前測試可用的檔案包含 .wav .mp4 .avi .mpg (依賴FFmpeg)
* 字級時間戳記 (WLTS) ：利用原文結果逗號分割，比對 WLTS 字級時間戳記，取出每一句的時間戳記。所以句子會比v2版的短。

> 程式語言:python
> 
> 作者：Jack

**在【exe3PydubToWLTS】資料夾下面的 main.exe 檔是發佈測試的版本，可以直接使用。**

**詳細的使用可以參考【程式說明：Azure影片轉srt字幕工具v3.docx】檔案。**

------------
**程式説明：**

程式核心是連接到微軟 Azure，上傳音頻檔取得字級時間戳記 WLTS(word level time stamps)，然後將原文結果用逗號分割，使用 python 的字串相似度比對套件，找出最佳的合并字組之時間戳記時段，進而產生相應字幕。

這支程式是使用python寫的GUI圖形界面轉字幕工具，【轉換字幕】按鈕點擊後，程式會判斷是否為 .wav 音頻檔，是的話直接上傳 Azure + 轉換字幕，不是的話則先進行轉檔，利用 Pydub 套件來將影片檔案轉出 .wav 音頻檔再上傳 Azure + 轉換字幕，Pydub 套件依賴 FFmpeg 前面已有説明。 

- 【main.py】：主程式。圖形界面上各功能的主程式撰寫。
- 【Ui_win.py】：圖形界面。vs code 配合 qt 設計去產生。
- 【qtAzToSrt_SDK.py】：配合主程式，將繁瑣的程式碼包裝，讓主程式容易閲讀。

------------
**參考網站:**

如何使用 Azure Speech to Text 和 Python SDK 獲取字級時間戳？
> https://stackoverflow.com/questions/56842391/how-to-get-word-level-timestamps-using-azure-speech-to-text-and-the-python-sdk

取得語音辨識結果 speech_config.request_word_level_timestamps()
> https://learn.microsoft.com/zh-tw/azure/cognitive-services/speech-service/get-speech-recognition-results?pivots=programming-language-python

讀取聲音資訊、輸出聲音（pydub）
> https://steam.oxxostudio.tw/category/python/example/pydub-sound-data.html

python比較字串相似度。
> https://www.796t.com/content/1544946186.html

------------
# Azure video to srt subtitle tool v3 (qtAzToSrt v3)
**v3-20221003:Updated**
* Support file conversion (Pydub): Currently available files for testing include .wav .mp4 .avi .mpg (depending on FFmpeg)
* Word-level time stamp (WLTS): Use the original text results to separate commas, compare the WLTS word-level time stamps, and take out the time stamp of each sentence. So the sentence will be shorter than the v2 version.

> Programming language: python
> 
> Author: Jack

**The main.exe file under the 【exe3PydubToWLTS】 folder is the release test version and can be used directly.**

**For detailed usage, please refer to the 【程式說明：Azure影片轉srt字幕工具v3.docx】 file.**

------------
**Program description:**

The core of the program is to connect to Microsoft Azure, upload audio files to obtain word level time stamps (WLTS), then separate the original results with commas, and use python's string similarity comparison suite to find the best combined word. The time stamp period of the group, and then the corresponding subtitles are generated.

This program is a GUI graphical interface conversion subtitle tool written in python. After clicking the [Convert Subtitles] button, the program will determine whether it is a .wav audio file. If it is, upload it directly to Azure + convert subtitles. If not, convert the file first. Use the Pydub package to convert the video file to a .wav audio file and upload the Azure + converted subtitles. The Pydub package relies on FFmpeg as described above.

- [main.py]: The main program. Write the main program of each function on the graphical interface.
- [Ui_win.py]: Graphical interface. VS code cooperates with qt design to generate.
- [qtAzToSrt_SDK.py]: Cooperate with the main program, wrap the cumbersome code to make the main program easy to read.

------------
**Reference website:**

How do I get word-level timestamps using Azure Speech to Text and the Python SDK?
> https://stackoverflow.com/questions/56842391/how-to-get-word-level-timestamps-using-azure-speech-to-text-and-the-python-sdk

Get speech recognition results speech_config.request_word_level_timestamps()
> https://learn.microsoft.com/en-tw/azure/cognitive-services/speech-service/get-speech-recognition-results?pivots=programming-language-python

Read sound information, output sound (pydub)
> https://steam.oxxostudio.tw/category/python/example/pydub-sound-data.html

python compare string similarity.
> https://www.796t.com/content/1544946186.html
