@echo off
rem 设置编码为GBK，防止乱码
chcp 936>nul
rem trust-host选项和https协议有关，使用未加密的http协议需要此设置
set trusthost=mirrors.aliyun.com
rem index-url选项指明更新源
set indexurl=https://mirrors.aliyun.com/pypi/simple/
rem 升级pip
python -m pip install --upgrade pip -i %indexurl% --trusted-host %trusthost%
rem 安装pynput
pip install pynput -i %indexurl% --trusted-host %trusthost%
pause
