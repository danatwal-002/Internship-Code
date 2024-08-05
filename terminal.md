
Library for seeing parameters for camera: v4l-utils

Download on terminal:  `sudo apt-get install v4l-utils`

Viewing camera params, 0 for RPI cam, 1 for webcam:  ``` v4l2-ctl -d /dev/video0 --list-formats-ext```

Use all CPUS for FR speedup:
```face_recognition --cpus -1 /home/sul/Desktop/pyPro/FR_Data/demoImages/known /home/sul/Desktop/pyPro/FR_Data/demoImages/unknown```

View CPUs:
```jtop```