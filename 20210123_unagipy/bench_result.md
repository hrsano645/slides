
# unagipy m1 mac bench

## python3.9.1 / rosseta / numpy 1.19.5

```
(.env) hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_numpy % pip list
Package    Version
---------- -------
numpy      1.19.5
pip        20.3.3
setuptools 49.2.1
(.env) hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_numpy % python                 
Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:44:01) 
[Clang 12.0.0 (clang-1200.0.32.27)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> exit()
(.env) hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_numpy % python ./numpy_speed.py 
53.73243689537048
(.env) hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_numpy % python ./numpy_speed.py
50.61187505722046
(.env) hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_numpy % python ./numpy_speed.py
48.99569892883301
(.env) hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_numpy % python ./numpy_speed.py
43.72466516494751
(.env) hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_numpy % python ./numpy_speed.py
40.71826505661011
(.env) hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_numpy % 
```

## python3.8.2/ rosseta / numpy 1.19.5

```
hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_py38_numpy % /usr/bin/python3 --version
Python 3.8.2
hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_py38_numpy % /usr/bin/python3 -m venv .env
hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_py38_numpy % source .env/bin/activate
(.env) hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_py38_numpy % python --version
Python 3.8.2
(.env) hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_py38_numpy % pip install -U pip
Collecting pip
  Using cached https://files.pythonhosted.org/packages/54/eb/4a3642e971f404d69d4f6fa3885559d67562801b99d7592487f1ecc4e017/pip-20.3.3-py2.py3-none-any.whl
Installing collected packages: pip
  Found existing installation: pip 19.2.3
    Uninstalling pip-19.2.3:
      Successfully uninstalled pip-19.2.3
Successfully installed pip-20.3.3
(.env) hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_py38_numpy % pip install numpy                    
Collecting numpy
  Using cached numpy-1.19.5-cp38-cp38-macosx_10_9_x86_64.whl (15.6 MB)
Installing collected packages: numpy
Successfully installed numpy-1.19.5
(.env) hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_py38_numpy % ls -la                  
total 8
drwxr-xr-x   4 hiroshi  staff  128  1 14 13:38 .
drwxr-xr-x  10 hiroshi  staff  320  1 14 13:38 ..
drwxr-xr-x   6 hiroshi  staff  192  1 14 13:38 .env
-rw-r--r--@  1 hiroshi  staff  411  1 14 13:37 numpy_speed.py
(.env) hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_py38_numpy % python ./numpy_speed.py 
40.13820433616638
(.env) hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_py38_numpy % python ./numpy_speed.py
39.195082902908325
(.env) hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_py38_numpy % python ./numpy_speed.py
38.5051531791687
(.env) hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_py38_numpy % python ./numpy_speed.py
40.20181107521057
(.env) hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_py38_numpy % python ./numpy_speed.py
39.54714274406433
(.env) hiroshi@hrsano645noMacBook-Air(x86_64) test_x86_py38_numpy % 
```

## python3.8.2 /arm native / tfmac numpy

```
(.env) hiroshi@hrsano645noMacBook-Air(arm64) tf-mac % python --version                
Python 3.8.2
(.env) hiroshi@hrsano645noMacBook-Air(arm64) tf-mac % pip list                        
Package                Version
---------------------- ---------
absl-py                0.11.0
appnope                0.1.2
astunparse             1.6.3
backcall               0.2.0
cached-property        1.5.2
cachetools             4.2.0
certifi                2020.12.5
chardet                4.0.0
decorator              4.4.2
flatbuffers            1.12
gast                   0.4.0
google-auth            1.24.0
google-auth-oauthlib   0.4.2
google-pasta           0.2.0
grpcio                 1.33.2
h5py                   2.10.0
idna                   2.10
ipython                7.19.0
ipython-genutils       0.2.0
jedi                   0.18.0
Keras-Preprocessing    1.1.2
Markdown               3.3.3
numpy                  1.18.5
oauthlib               3.1.0
opt-einsum             3.3.0
parso                  0.8.1
pexpect                4.8.0
pickleshare            0.7.5
pip                    20.3.3
prompt-toolkit         3.0.10
protobuf               3.14.0
ptyprocess             0.7.0
pyasn1                 0.4.8
pyasn1-modules         0.2.8
Pygments               2.7.4
requests               2.25.1
requests-oauthlib      1.3.0
rsa                    4.7
setuptools             51.1.2
six                    1.15.0
tensorboard            2.4.0
tensorboard-plugin-wit 1.7.0
tensorflow-addons      0.11.2
tensorflow-estimator   2.4.0
tensorflow-macos       0.1a1
termcolor              1.1.0
traitlets              5.0.5
typeguard              2.10.0
typing-extensions      3.7.4.3
urllib3                1.26.2
wcwidth                0.2.5
Werkzeug               1.0.1
wheel                  0.36.2
wrapt                  1.12.1
(.env) hiroshi@hrsano645noMacBook-Air(arm64) tf-mac % ls -la                          
total 16
drwxr-xr-x   5 hiroshi  staff  160  1 14 14:25 .
drwxr-xr-x  10 hiroshi  staff  320  1 14 13:38 ..
drwxr-xr-x   7 hiroshi  staff  224  1 14 14:23 .env
-rw-r--r--@  1 hiroshi  staff  411  1 14 14:25 numpy_speed.py
-rw-r--r--   1 hiroshi  staff  111  1 14 13:51 venv_activate.sh
(.env) hiroshi@hrsano645noMacBook-Air(arm64) tf-mac % python ./numpy_speed.py 
20.357348918914795
(.env) hiroshi@hrsano645noMacBook-Air(arm64) tf-mac % python ./numpy_speed.py
20.62715792655945
(.env) hiroshi@hrsano645noMacBook-Air(arm64) tf-mac % python ./numpy_speed.py
20.686599016189575
(.env) hiroshi@hrsano645noMacBook-Air(arm64) tf-mac % python ./numpy_speed.py
20.64151406288147
(.env) hiroshi@hrsano645noMacBook-Air(arm64) tf-mac % python ./numpy_speed.py
20.638553142547607
(.env) hiroshi@hrsano645noMacBook-Air(arm64) tf-mac % 
```

## python3.9.0 / Ryzen7 5800X / 

``` 
(.env) PS C:\Users\hiroshi\Documents\workspace\personal\test_ryzen_x86> python --version
Python 3.9.0
Package    Version
numpy      1.19.5
setuptools 49.2.1
(.env) PS C:\Users\hiroshi\Documents\workspace\personal\test_ryzen_x86> python .\numpy_speed.py
Traceback (most recent call last):
  File "C:\Users\hiroshi\Documents\workspace\personal\test_ryzen_x86\numpy_speed.py", line 16, in <module>
    np.dot(arr[k], arr[j])
  File "<__array_function__ internals>", line 5, in dot
KeyboardInterrupt
(.env) PS C:\Users\hiroshi\Documents\workspace\personal\test_ryzen_x86> python --version
Python 3.9.0
(.env) PS C:\Users\hiroshi\Documents\workspace\personal\test_ryzen_x86> python .\numpy_speed.py
308.8210823535919
(.env) PS C:\Users\hiroshi\Documents\workspace\personal\test_ryzen_x86> python .\numpy_speed.py
306.63446831703186
(.env) PS C:\Users\hiroshi\Documents\workspace\personal\test_ryzen_x86>

# TODO:2021-01-14 遅すぎたので中断した。
# winのnumpy遅すぎる問題があったかもしれないので追試必要かも。
```