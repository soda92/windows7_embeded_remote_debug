fbwfmgr /enable
fbwfmgr /addvolume c:
FbwfMgr /addexclusion C: \Temp
FbwfMgr /addexclusion C: \Users\user\AppData\Local\Temp
fbwfmgr /addvolume D:
fbwfmgr /addexclusion D: \TaiYuan-Release-v1.2.10\systemlog.txt
fbwfmgr /addexclusion D: \程序信息记录.txt
fbwfmgr /addexclusion D: \data
fbwfmgr /addexclusion C: "\Program Files\PostgreSQL\14\data"
shutdown /r /t 0