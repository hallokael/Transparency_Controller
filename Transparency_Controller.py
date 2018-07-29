import win32gui
import win32con
import re
import copy
width=2560
height=1440
app_list=[]
MAX=25
trans=185
old_hw=-3246234
score=0
wait=0.1
name_list = {
    b'',
    b'Msg',
    b'GDI+ Window',
    b'Default IME',
    b'Sogou_TSF_UI',
    b'HintWnd',
    b'MSCTFIME UI',
    b'Animate Manager',
    b'CircleDot',
    b'EVRVideoHandler',
    b'Program Manager',
    b'MSTaskListWClass',
    b'Task Switching',
    b'Network Flyout',
    b'Battery Meter',
    b'wpscenter',
    b'STATIC',
    b'nsAppShell:EventWindow',
    b'Hidden Window',
    b'RaUI\xe4\xbf\xa1\xe6\x81\xaf',
    b'CiceroUIWndFrame',
    b'BroadcastListenerWindow',
    b'Task Host Window',
    b'BluetoothNotificationAreaIconWindowClass',
    b'Cortana',
    b'Start'
    # b'KAccountWnd_Kso_classname_qingSdk',
    # b'minisite expansion window',
    # b'Windows Defender',
    # b'AfterSome',
    # b'MagicianTray',
    b'QQ'
}

import threading
def fun_timer():
    global old_hw
    global score
    hw=win32gui.GetForegroundWindow()
    go=False
    if hw==old_hw:
        score=score+1
        if score>=10:
            score=0
            go=True
    else:
        go=True
    old_hw=hw
    if not go :
        global timer
        timer = threading.Timer(wait, fun_timer)
        timer.start()
        return
    try:
        name = win32gui.GetWindowText(hw).encode('utf-8')
        if name in name_list:
            global timer
            timer = threading.Timer(wait, fun_timer)
            timer.start()
            return
        left, top, right, bottom = win32gui.GetWindowRect(hw)
    except Exception as e:
        print('dclks',e)
        try:
            app_list.remove(hw)
            global timer
            timer = threading.Timer(wait, fun_timer)
            timer.start()
            return
        except Exception as e:
            print('asd',e)
            global timer
            timer = threading.Timer(wait, fun_timer)
            timer.start()
            return
    global flag
    flag=0
    for index in range(len(app_list)):
        if app_list[index] == hw:
            print(1,index)
            for i in range(index,0,-1):
                print('iii',i)
                app_list[i]=app_list[i-1]
            app_list[0]=hw
            flag=flag+1
            break
    if flag==0:
        if app_list==[]:
            app_list.append(hw)
            print(2)
        else:
            print(3)
            if len(app_list)<MAX:
                temp=app_list[len(app_list) - 1]
                app_list.append(temp)

            for i in range(len(app_list)-1,0, -1):
                app_list[i] = app_list[i - 1]
            app_list[0] = hw

    display_space = [[0 for _ in range(-5,20)] for _ in range(-5,20)]
    print(app_list)
    for app in app_list:
        try:
            name = win32gui.GetWindowText(hw).encode('utf-8')
            if name in name_list:
                print('in_list')
                global timer
                timer = threading.Timer(wait, fun_timer)
                timer.start()
                return
            left, top, right, bottom = win32gui.GetWindowRect(app)
        except Exception as e:
            print('sdadw',e)
            try:
                app_list.remove(app)
                continue
            except Exception as e:
                print('xxax',e)
                continue
        global haha
        haha=0
        if left<-100 or right >width+100 or top<-100 or bottom>height+100:
            continue
        bound=[0,0,0,0]
        bound[0]=int(left/width*15)
        bound[1] = int(right / width * 15)
        bound[2] = int(top / height * 15)
        bound[3] = int(bottom / height * 15)

        for i in range(4):
            if bound[i]>14:
                bound[i]=14
            if bound[i]<1:
                bound[i]=1
        for i in range(bound[0],bound[1]):
            for j in range(bound[2],bound[3]):
                if display_space[i][j]==0:
                    display_space[i][j]=1
                    haha=haha+1
        try:
            s = win32gui.GetWindowLong(app, win32con.GWL_EXSTYLE)
            win32gui.SetWindowLong(app, win32con.GWL_EXSTYLE, s | win32con.WS_EX_LAYERED)
            if haha==0:
                win32gui.ShowWindow(app, win32con.SW_MINIMIZE)
                print(app,'mini',name)
            else:
                # print(app)
                win32gui.SetLayeredWindowAttributes(app, 0, trans, win32con.LWA_ALPHA)
                print(app,'fade',name)
        except Exception as e:
            print('xXAXAX',e)
            try:
                app_list.remove(app)
                continue
            except Exception as e:
                print('xadea',e)
                continue

    global timer
    timer = threading.Timer(wait, fun_timer)
    timer.start()

timer = threading.Timer(wait, fun_timer)
timer.start()

