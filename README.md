Android系统UI自动化测试项目
=
框架架构：
![](https://pic1.zhimg.com/80/v2-259b92e129cdbdd95c38e38b1b480cec_1440w.jpg)
<br>
<br>`效果：自己试了才知道！！！`<br> 
<br>使用方法：<br> 
1、使用requirements.txt对依赖库进行安装：<br>
```
pip3 install -r requirements.txt 
```
<br>2、项目使用的是Python3.7（可自行调整）<br> 
<br>3、最好使用Pycharm管理项目，方便修改<br> 
<br>4、Pycharm使用的是Venv虚拟环境，即其Python包是独立的，便于将项目集成包放入requirements移植到其它地方<br> 
<br>5、通过run_test.py定义需要执行的测试包当前是Fota测试包<br>
```
"""
    @description:main函数，主要运行函数
"""
if __name__ == '__main__':
    print("脚本开始测试，Fota checklist模块测试正在运行中……")
    for i in range(30):
        print("这是第{}次测试该脚本".format(i))
        fota_checklist_test_module()
        sleep(1)
        print("This is {} times running and time is {}".format(str(i), time.strftime("%Y%m%d_%H%M%S")))
    print("脚本测试结束，请检查测试结果")
```
<br>6、测试完成后生成的报告可浏览器打开查看<br> 
```
subprocess.Popen(
        args=["allure", "generate", "./temp/need_data[{}_{}]/".format(time.strftime("%Y%m%d_%H%M%S"), device_), "-o",
              "./report/test_report[{}_{}]/".format(time.strftime("%Y%m%d_%H%M%S"), device_),
              "--clean"],
        shell=False).communicate()[0]
```
<br>目前项目已实现功能：<br> 
<br>1、批量管理设备：安装应用、应用授权<br> 
<br>2、基于Pytest进行测试包测试<br> 
<br>3、对Android系统应用通过Page划分集中管理<br> 

<br>可能出现的问题：<br> 
<br>1、首先对于pip3的报错使用该命令解决：<br>
```
sudo easy_install pip
```
<br>如果出现通过pip3安装模块后，py运行还是失败的，使用pycharm的interpreter里面搜索对应模块再安装即可<br> 
<br>2、# 本项目已修改源码：<br>
<br>路径：/Users/cgt/Library/Python/3.7/lib/python/site-packages/poco/drivers/android/uiautomation.py"<br> 
```
print("still waiting for uiautomation ready.")
```
```
self.adb_client.shell('am start -n {}/.TestActivity'.format(PocoServicePackage))<br>
``` 
<br>3、# 兼容Pycharm使用相对路径存在同目录下文件找不到问题：<br> 
<br>修改Edit configurations -> 将Working directory改成当前项目目录即可<br> 
<br>4、#airtest操作API<br> 
<br>以下func大部分可单独运行：<br> 
<br>a.单独调用 - 当前Device<br> 
<br>b.指定device调用 - 控制不同设备（主要API选择）<br> 
<br>Airtest的API的用法，它提供了一些方法的封装，同时还对接了图像识别等技术，但Airtest也有局限性，不能根据DOM树
<br>来选则对应但节点，依靠图像识别也有一定不精确之处，所以还需要另一个库Poco<br> 
<br>5、遇到Python找不到，IntFlag时，unset PYTHONPATH<br> 
<br>6、```"ImportError: sys.meta_path is None, Python is likely shutting down"``` <br>
<br>这个报错是能忽略的，是因为poco报错后就退出了，主线程回收垃圾，剩下的子线程抛了这个错，是可以忽略的。<br> 
<br>7、有些输入密码等界面因为Android安全机制保护，需要特别注意看是否能够获取到元素控件<br> 
<br>8、# 修改源文件：<br> 
<br>a.规避sys.meta_path is None, Python is likely shutting down问题导致的报错<br> 
<br>/Users/cgt/PycharmProjects/AutomationProject/venv/lib/python3.7/site-packages/hrpc/object_proxy.py<br> 
``` 
try:    
    self._client__.evaluate(RpcObjectProxy(self._uri__, self._client__, action), wait_for_response=False)<br> 
except Exception as ex:
    print(ex)
``` 
<br>9、Settings控制：<br> 
<br>a、使用adb shell svc控制一些开关、wifi等<br> 
<br>settings put和get有局限<br> 
<br>b、注意流的开启和关闭对资源的消耗<br> 

<br>`最后提到：`<br> 
`对于UI测试，不能覆盖所有的case，只能尽可能去转化一些case，不要为了自动化而自动化！！！`<br> 


