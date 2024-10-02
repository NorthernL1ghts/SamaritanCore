import os
import json
from pathlib import Path

class ApplicationSettings:
    # Universal project path
    c_ProjectPath = Path("C:/Dev/Samaritan/SamaritanCore")
    c_SettingsFile = c_ProjectPath / "Settings.json"

    def __init__(self):
        self.m_FilePath = self.c_SettingsFile
        self.m_Settings = {}
        self.Deserialize()

    def Serialize(self):
        with open(self.m_FilePath, 'w') as json_file:
            json.dump({"SamaritanCore Application Settings": self.m_Settings}, json_file, indent=4)

    def Deserialize(self):
        if not self.m_FilePath.exists():
            return False

        with open(self.m_FilePath, 'r') as json_file:
            data = json.load(json_file)
            self.m_Settings = data.get("SamaritanCore Application Settings", {})
        return True

    def HasKey(self, key):
        return key in self.m_Settings

    def Get(self, name, defaultValue=""):
        return self.m_Settings.get(name, defaultValue)

    def GetFloat(self, name, defaultValue=0.0):
        return float(self.m_Settings.get(name, defaultValue))

    def GetInt(self, name, defaultValue=0):
        return int(self.m_Settings.get(name, defaultValue))

    def Set(self, name, value):
        self.m_Settings[name] = value

    def SetFloat(self, name, value):
        self.m_Settings[name] = str(value)

    def SetInt(self, name, value):
        self.m_Settings[name] = str(value)