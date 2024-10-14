# Program Dengan Tema Sistem Pendataan Pemasangan Wifi Indihome
def login():
    from prettytable import PrettyTable  

    Tabel = PrettyTable()
    Tabel.field_names = ["No", "Pilihan"]
    def Data(No, Pilihan):
        Tabel.add_row([No, Pilihan])

    Data("1", "Admin")
    Data("2", "Customer")
    Data("3", "Exit")
    print(Tabel)

# Input Pilihan Pengguna dan Password
    Pengguna = input("Pilih Pengguna: ")
    Password = input("Masukan Password: ")
    if Pengguna == "Admin":
        if Password == "Admin123":
            Admin()
    elif Pengguna == "Customer".lower():
        if Password == "Customer123".lower():
            User()
    elif Pengguna == "Exit".lower():
        print("Terima Kasih:) ")
    else:
        print("Maaf Tidak Ada Inputan")

# Prettytable
from prettytable import PrettyTable  

Tabell = PrettyTable()
Tabell.field_names = ["No", "Masa Paket", "Nama Paket", "Harga Pembelian "]
Tabell.add_row(["1", "1/bln", "Paket Hemat", "Rp.250.000"])
Tabell.add_row(["2", "2/bln", "Paket Premium", "Rp.350.000"])
Tabell.add_row(["3", "3/bln", "Paket Extra", "Rp.450.000"])

# def Admin
def Admin():
    Nama = input("Masukan Nama Anda: ")
    while True:
        print(f"Welcomee! ({Nama}) Silahkan Pilih Kebutuhan Anda:)")
        from prettytable import PrettyTable  

        Tabelll = PrettyTable()
        Tabelll.field_names = ["No", "Pilihan"]

        def Dataa(No, Pilihan):
            Tabelll.add_row([No, Pilihan])

        Dataa("1", "Tambah Paket")
        Dataa("2", "Cek Paket")
        Dataa("3", "Update Paket")
        Dataa("4", "Cancel Paket")
        Dataa("5", "Exit")
        print(Tabelll)

# Input Pilihan Untuk Masuk ke CRUD
        Pilihan = input("Masukan Pilihan: ")
        if Pilihan == "1":
            Tambah_Paket()
        elif Pilihan == "2":
            Cek_Paket()
        elif Pilihan == "3":
            Update_Paket()
        elif Pilihan == "4":
            Cancel_Paket()
        elif Pilihan == "5":
            login()
            return True
        else:
            print("Maaf Tidak Ada Pilihan")

# def User/Customer
def User():
    Nama = input("Masukan Nama Anda: ")
    while True:
        print(f"Welcomee! ({Nama}) Silahkan Pilih Sesuai Kebutuhan Anda:)")
        from prettytable import PrettyTable  

        Tabellll = PrettyTable()
        Tabellll.field_names = ["No", "Pilihan"]
        def Dataaa(No, Pilihan):
            Tabellll.add_row([No, Pilihan])

        Dataaa("1", "Cek Paket")
        Dataaa("2", "Pembelian Paket")
        Dataaa("3", "Exit")
        print(Tabellll)

# Input Pilihan ke Pembelian
        Pilihan = input("Masukan Pilihan: ")
        if Pilihan == "1":
            Cek_Paket()
        elif Pilihan == "2":
            Pembelian_Paket()
        elif Pilihan == "3":
            print("Terima Kasih")
            return True
        else:
            print("Maaf TidaK Ada Pilihan")

def Tambah_Paket():
    while True:
        Cek_Paket()
        No = input("Masukan Nomor: ")
        Masa_Paket = str(input("Masukan Masa Paket: "))
        Nama_Paket = str(input("Masukan Nama Paket: "))
        Harga_Paket = str(input("Masukan Harga Pembelian: "))
        Tabell.add_row([No,Masa_Paket,Nama_Paket,Harga_Paket])
        print(Tabell)
        Lanjut = input("Mau tambah/tidak: ")
        if Lanjut == "Y":
            Tambah_Paket()
        elif Lanjut == "T":
            
            return True
        else:
            print("program anda berhenti")

# def Cek Paket
def Cek_Paket():
    print(Tabell)

# def Update Paket
def Update_Paket():
    while True:
        print(Tabell)
        No = input("Masukkan No Paket Yang Ingin Diupdate: ")
        for Ubah in Tabell._rows:
            if Ubah[0] == No:
                Nomor_Paket = input("Masukan Masa Paket Admin baru: ")
                Nama_Baru = input("Masukkan Nama Paket Baru: ")
                Harga_Pembelian_Baru = input("Masukkan Harga Pembelian Baru: ")
                Ubah[1] = Nomor_Paket
                Ubah[2] = Nama_Baru
                Ubah[3] = Harga_Pembelian_Baru
                print("Paket Berhasil Diupdate")
                print(Tabell)
                return True
        else:
            print("Kelas Tidak Ditemukan.")

# def Cancel Paket
def Cancel_Paket():
    while True:
        print(Tabell)
        No = input("Masukkan No Paket Yang Ingin Dihapus: ")
        for Delete in Tabell._rows:
            if Delete[0] == No:
                Tabell._rows.remove(Delete)
        print(Tabell)
        return True

# def Pembelian Paket
def Pembelian_Paket():
    while True:
        print(Tabell)
        No = input("Masukkan Nomor Paket Yang Ingin Dibeli: ")
        for Beli in Tabell._rows:
            if Beli[0] == No:
                print(f"Anda Telah Membeli Paket ({Beli[1]}) dengan Nama ({Beli[2]}) dan Waktu ({Beli[3]}.")
                Tabell._rows.remove(Beli)
                print("Paket Yang Tersedia Setelah Pembelian:")
                print(Tabell)
                return True
            
login()