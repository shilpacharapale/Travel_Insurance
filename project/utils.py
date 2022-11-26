import json
import pickle
import config
import numpy as np

class Insurance():
    def __init__(self,Age,GraduateOrNot,AnnualIncome,FamilyMembers,ChronicDiseases,FrequentFlyer,EverTravelledAbroad,GovernmentSector):
        self.Age = Age
        self.GraduateOrNot = GraduateOrNot
        self.AnnualIncome = AnnualIncome
        self.FamilyMembers = FamilyMembers
        self.ChronicDiseases = ChronicDiseases
        self.FrequentFlyer = FrequentFlyer
        self.EverTravelledAbroad =EverTravelledAbroad
        self.GovernmentSector = GovernmentSector

    def load_model(self):
        with open(config.JSON_MODEL_PATH,"r") as f:
            self.json_data = json.load(f)

        with open(config.MODEL_PATH,"rb") as f:
            self.model = pickle.load(f)

    def get_insure(self):
        self.load_model()
        test_array = np.zeros(len(self.json_data["columns"]))
        test_array[0] = self.Age
        test_array[1] = self.json_data["Graduate_Not"][self.GraduateOrNot]
        test_array[2] = self.AnnualIncome
        test_array[3] = self.FamilyMembers
        test_array[4] = self.ChronicDiseases
        test_array[5] = self.json_data["Frequent_Flyer"][self.FrequentFlyer]
        test_array[6] = self.json_data["EverTravelled_Abroad"][self.EverTravelledAbroad]
        test_array[7] = self.json_data["Government_Sector"][self.GovernmentSector]
        pred = self.model.predict([test_array])[0]
        return pred



