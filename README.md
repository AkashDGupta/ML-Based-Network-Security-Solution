Purpose of the code is to Demostrate Machine learning for network attack detection.

**Train_Test_Network.csv **
**Train_Test_Network.csv**
File shows network traffic data logs used for model training and testing.

**ai_attack_detection_model.py**
Python script for label encoding, dataset splitting and model training and testing.

**INSTALED PACKAGES**

**NUMPY**

pip3 install numpy
Defaulting to user installation because normal site-packages is not writeable
Collecting numpy
  Downloading numpy-1.26.4-cp312-cp312-win_amd64.whl.metadata (61 kB)
     ---------------------------------------- 61.0/61.0 kB 466.1 kB/s eta 0:00:00
Downloading numpy-1.26.4-cp312-cp312-win_amd64.whl (15.5 MB)
   ---------------------------------------- 15.5/15.5 MB 6.1 MB/s eta 0:00:00
Installing collected packages: numpy
  WARNING: The script f2py.exe is installed in 'C:\Users\XXXX\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed numpy-1.26.4

**SCIPY**

pip3 install scipy
Defaulting to user installation because normal site-packages is not writeable
Collecting scipy
  Downloading scipy-1.13.0-cp312-cp312-win_amd64.whl.metadata (60 kB)
     ---------------------------------------- 60.6/60.6 kB 461.8 kB/s eta 0:00:00
Requirement already satisfied: numpy<2.3,>=1.22.4 in c:\users\XXXX\appdata\local\packages\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\localcache\local-packages\python312\site-packages (from scipy) (1.26.4)
Downloading scipy-1.13.0-cp312-cp312-win_amd64.whl (45.9 MB)
   ---------------------------------------- 45.9/45.9 MB 5.6 MB/s eta 0:00:00
Installing collected packages: scipy

**PANDAS**

pip3 install pandas
Defaulting to user installation because normal site-packages is not writeable
Collecting pandas
  Downloading pandas-2.2.2-cp312-cp312-win_amd64.whl.metadata (19 kB)
Requirement already satisfied: numpy>=1.26.0 in c:\users\XXXX\appdata\local\packages\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\localcache\local-packages\python312\site-packages (from pandas) (1.26.4)
Collecting python-dateutil>=2.8.2 (from pandas)
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz>=2020.1 (from pandas)
  Downloading pytz-2024.1-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.7 (from pandas)
  Downloading tzdata-2024.1-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas)
  Downloading six-1.16.0-py2.py3-none-any.whl.metadata (1.8 kB)
Downloading pandas-2.2.2-cp312-cp312-win_amd64.whl (11.5 MB)
   ---------------------------------------- 11.5/11.5 MB 6.3 MB/s eta 0:00:00
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
   ---------------------------------------- 229.9/229.9 kB 6.9 MB/s eta 0:00:00
Downloading pytz-2024.1-py2.py3-none-any.whl (505 kB)
   ---------------------------------------- 505.5/505.5 kB 6.3 MB/s eta 0:00:00
Downloading tzdata-2024.1-py2.py3-none-any.whl (345 kB)
   ---------------------------------------- 345.4/345.4 kB 7.1 MB/s eta 0:00:00
Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: pytz, tzdata, six, python-dateutil, pandas
Successfully installed pandas-2.2.2 python-dateutil-2.9.0.post0 pytz-2024.1 six-1.16.0 tzdata-2024.1

**SCIKIT-LEARN**

pip install scikit-learn
Defaulting to user installation because normal site-packages is not writeable
Collecting scikit-learn
  Downloading scikit_learn-1.4.2-cp312-cp312-win_amd64.whl.metadata (11 kB)
Requirement already satisfied: numpy>=1.19.5 in c:\users\akagupta\appdata\local\packages\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\localcache\local-packages\python312\site-packages (from scikit-learn) (1.26.4)
Requirement already satisfied: scipy>=1.6.0 in c:\users\akagupta\appdata\local\packages\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\localcache\local-packages\python312\site-packages (from scikit-learn) (1.13.0)
Collecting joblib>=1.2.0 (from scikit-learn)
  Downloading joblib-1.4.0-py3-none-any.whl.metadata (5.4 kB)
Collecting threadpoolctl>=2.0.0 (from scikit-learn)
  Downloading threadpoolctl-3.4.0-py3-none-any.whl.metadata (13 kB)
Downloading scikit_learn-1.4.2-cp312-cp312-win_amd64.whl (10.6 MB)
   ---------------------------------------- 10.6/10.6 MB 6.3 MB/s eta 0:00:00
Downloading joblib-1.4.0-py3-none-any.whl (301 kB)
   ---------------------------------------- 301.2/301.2 kB 6.2 MB/s eta 0:00:00
Downloading threadpoolctl-3.4.0-py3-none-any.whl (17 kB)
Installing collected packages: threadpoolctl, joblib, scikit-learn
Successfully installed joblib-1.4.0 scikit-learn-1.4.2 threadpoolctl-3.4.0



**RESULTS**

Based on the current dataset, model has accuracy of more than 99.99%

#########Pre_Transformation Test Data#########
          src_ip  src_port         dst_ip  dst_port proto service    type
0    3.122.49.24      1883  192.168.1.152     52976   tcp       -  normal
1   192.168.1.30     42908  192.168.1.250      7435   tcp       -  attack
2  192.168.1.152     45789  192.168.1.190        53   udp     dns  normal
3   192.168.1.30     42908   192.168.1.46      1641   tcp       -  attack
4   192.168.1.79     47260  192.168.1.255     15600   udp       -  normal



#########POST_Transformation Test Data-src_ip only#########
   src_ip  src_port         dst_ip  dst_port proto service    type
0    8047      1883  192.168.1.152     52976   tcp       -  normal
1    4602     42908  192.168.1.250      7435   tcp       -  attack
2    4590     45789  192.168.1.190        53   udp     dns  normal
3    4602     42908   192.168.1.46      1641   tcp       -  attack
4    4614     47260  192.168.1.255     15600   udp       -  normal

#########POST_Transformation Test Data-After All Label Encoding#########
   src_ip  src_port  dst_ip  dst_port  proto  service  type
0    8047      1883    1510     52976      1        0     1
1    4602     42908    1520      7435      1        0     0
2    4590     45789    1515        53      2        3     1
3    4602     42908    1527      1641      1        0     0
4    4614     47260    1521     15600      2        0     1

#########Trained Model Accuracy Mesurement#########
Accuracy 0.999956619816068

#########Confusion Matrix for Trained Model#########
Confusion Matrix [[48490     2]
 [    4 89816]]#
