# Tugas 2
## 1.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Menginstall env dengan python.
2. Menginstall dependencies.
3. Membuat aplikasi baru dan mendaftarkan ke dalam `settings.py`.
4. Membuat template dasar menggunakan html.
5. Membuat implementasi di `models.py`.
6. Membuat implementasi di `views.py`.
7. Mengonfiguarsi routing URL di `urls.py` direktori aplikasi main dan routing URL di `urls.py`di direktori utama.
## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara *`urls.py`*, *`views.py`*, *`models.py`*, dan berkas html.
<br>

![Bagan Django](https://cdn.discordapp.com/attachments/1013790676296683592/1149595864315199529/Bagan_django.png)
<br>
Client akan request ke `urls.py`. Lalu, `urls.py`akan memilih view dari `views.py`. Setelah itu, `views.py` akan mengirimkan query ke `models.py` dan mengembalikan data. Selanjutnya akan memilih berkas HTML dan HTML akan menampilkan halaman web kembali ke client.

## 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? 
- Virtual environment digunakan untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer local. 
- Kita bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment hanya kita tidak dapat mengisolasi project untuk mencegah terjadinya konfilk antar project.

## 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
- Model View Controller (MVC) adalah sebuah metode untuk membuat sebuah aplikasi dengan memisahkan data (Model) dari tampilan (View) dan cara bagaimana memprosesnya (Controller)
- Model View Template (MVT) adalah sebuah konsep arsitektur yang digunakan dalam pengembangan web untuk memisahkan komponen-komponen utama dari sebuah aplikasi. 
- Model View ViewModel (MVVM) adalah salah satu arsitektur pembuatan aplikasi berbasis GUI yang berfokus pada pemisahan antara kode untuk logika bisnis dan tampilan aplikasi.
___

<br>

# Tugas 3
## 2. Apa perbedaan antara form POST dan form GET dalam Django?
### Form Post:
- Form POST adalah method yang digunakan untuk mengirimkan data pada web seperti input text ataupun radio button.
- Data yang dikirim melalui HTTP request adalah data berupa teks biasa (text).
- Dengan cara ini, data tersebut tidak bisa disimpan oleh browser secara langsung tanpa menambah proses penyambungan untuk memodifikasinya.
- Jika ingin membuka halaman lainnya atau menuju ke URL lain, harus mengirimkannya via method post.
- Dalam pengiriman data tersebut tidak ada batasan ukuran atau jumlahnya.
- Pengguna bisa melihat isi dari setiap field pada halaman web.
- Biasanya digunakan untuk menyimpan informasi seperti username/password, nama user dll.
- jika pembuatan berhasil, maka akan mengembalikan HTTP status code 201
### Form Get:
- Form GET adalah method yang digunakan untuk mendapatkan data pada web. 
- Form GET mengembalikan HTTP status code 200 (OK) jika data berhasil diambil dari server.
- Data yang dikirimkan melalui HTTP request merupakan parameter url.
- Parameter ini akan disertai oleh tanda ? dan dilanjutkan dengan key=value&key=value.
- Digunakan untuk membaca data saja tanpa memperbarui database.

## 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
| |XML|JSON|HTML|
|-|-|-|-|
|**Format**|Textual|Textual|Markup Language|
|**Data Type**|Terstruktur|Tidak Terstruktur|Tidak Terstruktur|
|**Structure**|Hierarchical|Flat|Tree Structure|
|**Size**|Besar|Kecil|Sedang|
|**Speed of Transmission**|Lambat|Cepat|Sangat Cepat|
|**Usage**|Web Services|APIs|Web Pages|
## 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- Formatnya sangat sederhana sehingga prosesnya sangat cepat.
- Format tersebut juga bisa diproses oleh komputer tanpa harus mendeklarasikannya .
- Kita tidak perlu membuat class baru untuk menerima atau memanipulasi data dari API terkait.
- Pembuatan data JSON dapat ditulis dalam bahasa pemrograman apapun.
## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. membuat input fields form di `forms.py`.
2. membuat function-function baru untuk menampilkan di `views.py`

`create_product`:
```python 
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
`XML`:
```python
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

`JSON`:
```python
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
``` 
`XML by ID`:
```python
def show_xml_by_id(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
`JSON by ID`:
```python
def show_json_by_id(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
3. meng-import function-function dari `views.py` ke `urls.py`
4. membuat path baru di urls.py untuk memanggil fungsi di `views.py`.
```python
...
path('create-product', create_product, name='create_product'),
path('xml/',show_xml,name='show_xml'),
path('json/',show_json,name='show_json'),
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<int:id>/', show_json_by_id, name='show_json_by_id')
...
```
![Postman](image.png)