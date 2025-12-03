# xss_array_injection (lang=Malay)
## Source code
`server1.py` ialah versi backend yang lemah <br>
`server2.py` ialah versi backend yang telah diperkuat

Pastikan anda telah install python interpreter dalam pc/laptop anda
Download di website official python
[https://www.python.org/downloads/](https://www.python.org/downloads/)

# Download source code ataupun clone repo ini
[!screenshot](134434.png)

or

```sh
git clone https://github.com/Mika259/xss_array_injection.git
```
```sh
cd xss_array_injection
```

## Install requirement
```sh
pip install flask
```

## Jalankan server untuk uji
Untuk jalankan server flask versi vuln xss
```sh
python server1.py
```

Untuk jalankan server flask versi diperbaiki dan diperkuat
```sh
python server2.py
```

Selepas jalankan salah satu, kamu boleh akses `http://localhost:8000` untuk cuba payload xss yang bermacam untuk uji samaada dikesan atau tak.

# Education Purposes Only
