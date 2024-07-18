import os
import random
import json

# CSVファイルのパス
current_dir = os.path.dirname(os.path.abspath(__file__))
current_data_path = os.path.join(
    current_dir, 'data/machine_data.json'
)


class CreateDummyData:
    '''
    ダミーのデータを作成する
    '''
    def __init__(self):
        """
        初期処理
        """

    def get_json_data(self) -> dict:
        """
        jsonデータを取得
        """
        try:
            with open(current_data_path, 'r') as file:
                data = json.load(file)
            return data
        except Exception() as e:
            print(e)
            return []

    def create_all_data(self) -> dict:
        """
        すべてのデータを作成する
        """
        all_data = self.get_json_data()

        # エアコンの計測データを更新
        all_data["air_conditioner_A"] = self.simulate_air_conditioner()
        all_data["air_conditioner_B"] = self.simulate_air_conditioner()

        # 換気扇の計測データを更新
        all_data["fan"] = self.simulate_fan()

        # 二酸化炭素測定機の計測データを更新
        all_data["co2_monitor"] = self.simulate_co2_monitor()

        # 温湿度計の計測データを更新
        all_data["thermohygrometer_A"] = self.simulate_thermohygrometer()
        all_data["thermohygrometer_B"] = self.simulate_thermohygrometer()

        return all_data

    def simulate_air_conditioner(self) -> dict:
        """
        エアコン計測データのシミュレート
        """
        ret_data = {
            "temp": random.randint(0, 100),
            "mode": random.choice(["冷房", "暖房"])
        }

        return ret_data

    def simulate_fan(self) -> dict:
        """
        換気扇のシミュレート
        """
        ret_data = {
            "value": random.choice(["ON", "OFF"])
        }

        return ret_data

    def simulate_co2_monitor(self) -> dict:
        """
        二酸化炭素測定機のシミュレート
        """
        ret_data = {
            "value": random.randint(500, 1100)
        }

        return ret_data

    def simulate_thermohygrometer(self) -> dict:
        """
        温湿度計のシミュレート
        """
        ret_data = {
            "temp": random.randint(0, 100),
            "humidity": random.randint(0, 100)
        }

        return ret_data
