import requests
from datetime import datetime, timedelta

def get_weather(delta):
    # URL API BMKG yang akan diakses
    url = "https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=71.03.17.1016"

    # Membuat permintaan GET ke API
    response = requests.get(url)

    # Memeriksa status response
    if response.status_code == 200:
        # Mengubah response menjadi format JSON
        data = response.json()
        
        weather = data["data"]
        # Tentukan tanggal hari ini tetapi tetap pada jam 11:00:00
        now = datetime.now()
        today = datetime(now.year, now.month, now.day, 11, 0, 0)  # Contoh: 2024-10-04 11:00:00
        time_data = today + timedelta(hours=delta)

        # Filter data cuaca berdasarkan local_datetime yang sesuai dengan hari ini pada jam 11:00:00
        list_result = []

        for lokasi_data in weather:
            for periode in lokasi_data["cuaca"]:
                for cuaca in periode:
                    # Konversi string local_datetime ke datetime object
                    local_dt = datetime.strptime(cuaca["local_datetime"], "%Y-%m-%d %H:%M:%S")
                    
                    # Cek apakah local_datetime sama dengan hari ini (tanggal saat ini pada jam 11:00:00)
                    if local_dt == time_data:
                        list_result.append(cuaca)

        return list_result[0]
    else:
        print(f"Error: Tidak dapat mengakses API BMKG. Status code: {response.status_code}")



data = get_weather(24)
print(data["weather"])
