import screen_brightness_control as sbc
import requests

# url = f"https://{SERVER}/external/api/get?token={TOKEN}&{VIRTUAL-PIN}"

class Screen:
    pVal = "100"
    luxDic = {}
    
    def __init__(self, token, vPin) -> None:
        self.url = f"https://blynk.cloud/external/api/get?token={token}&{vPin}"
     
    def setBrightness(self):
        cVal = self.getExternalLight()
        if cVal != self.pVal: 
            for key in self.luxDic:
                if(int(cVal) <= key):
                    sbc.set_brightness(self.luxDic[key])
                    self.pVal = cVal
                    print(f"Obtained value: {cVal}; Brightness: {self.luxDic[key]} %")
                    break
    def populateDic(self):
        with open('dic.txt', 'r') as f:
                for line in f:
                    x, y = line.strip().split(":")
                    self.luxDic[int(x)] = int(y)
                print(self.luxDic)
    def getExternalLight(self):
        return requests.get(self.url).text 
    @staticmethod
    def getBrightness():
        return sbc.get_brightness()

