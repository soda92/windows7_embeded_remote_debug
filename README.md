# windows7_embeded_remote_debug
Remote debug configurations for windows 7 embeded.

安装步骤

## 系统
1. 连接到无线网络
1. 安装证书
1. 安装三个补丁，卸载KB3126587(如果有的话)
1. 安装`.NET 4.8`（ndp48-web.exe)
1. 安装VCRedist、VS Remote Tools。
1. 安装FRP，使用winsw安装服务。

## 软件
1. 安装Chrome
1. 安装Notepad++
1. 下载安装PostgreSQL
1. 解压，设置powershell：
    ```
    Set-ExecutionPolicy RemoteSigned
    ```
    解压安装system_patch\Win7AndW2K8R2-KB3191566-x64.zip
    下载安装PowerShell 7
1. 安装字体
1. 安装WizTree，检查文件空间
1. 运行pypi脚本，根据`requirements.txt`安装包

## 测试
1. 运行platform_info.py，查看系统信息
1. 运行tts.py测试语音
