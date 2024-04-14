Purpose of the code is to Demostrate Machine learning for network attack detection.

**Train_Test_Network.csv **
File shows network traffic data logs used for model training and testing.

**ai_attach_detection_model.py **#########Pre_Transformation Test Data#########
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
 [    4 89816]]
Main Python script for importing traffic data log, label encoding, dataset splitting and model training and testing. 


**RESULTS**
Based on the current dataset, model has accuracy of more than 99.99%

#########Pre_Transformation Test Data#########
          src_ip  src_port         dst_ip  dst_port proto service    type
0    3.122.49.24      1883  192.168.1.152     52976   tcp       -  normal
1   192.168.1.30     42908  192.168.1.250      7435   tcp       -  attack
2  192.168.1.152     45789  192.168.1.190        53   udp     dns  normal
3   192.168.1.30     42908   192.168.1.46      1641   tcp       -  attack
4   192.168.1.79     47260  192.168.1.255     15600   udp       -  normal
#########POST_Transformation Test Data-src_ip only#################Pre_Transformation Test Data#########
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
 [    4 89816]]
