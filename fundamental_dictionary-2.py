"""
Tipe dictionary adalah untuk menghubungkan antara Key dan Value
KVP = Key Value Pair
"""

# contoh kasus data gojek

print('Data ini dikirimkan oleh server ke aplikasi pengguna sehingga pengguna tahu driver terdekat')

data_driver_server_gojek = {
    'tanggal': '2021-1-19',
    'driver_list':
        {'nama': 'Eko', 'jarak': 10},
        {'nama': 'Budi', 'jarak': 30}
    ]
}

print(
    f" Driver paling dekat dengan jarak anda saat ini adalah {data_driver_server_gojek['driver_list'][0]['jarak']} meter")
