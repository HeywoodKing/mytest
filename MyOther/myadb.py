"""
原理说明
将手机点击到《跳一跳》小程序界面；
用Adb 工具获取当前手机截图，并用adb将截图pull上来
    adb shell screencap -p /sdcard/1.png
    adb pull /sdcard/1.png .
用matplot显示截图；
用鼠标点击起始点和目标位置，计算像素距离；
根据像素距离，计算按压时间；
用Adb工具点击屏幕蓄力一跳；
    adb shell input swipe x y x y time

"""