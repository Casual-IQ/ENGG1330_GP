#Enter python3 main.py to run the gameqq
#Group project from C3-1
#hint:don't try to hit the wall which will reduce your remaining try times
#enjoy playing :) if you like it plz give us high score :)
#use ↑↓←→ key to control your character
#press q to go back to menu while playing
#Ctrl+C to quit or select the Exit buttom and p
#remember to copy the module
import curses
from module import base
import threading
import time
#     


map_example=[  
    "**************",
    "**  a        *",
    "** ********* *",
    "** ***** b * *",
    "** ***** *   *",
    "** ***** *****",
    "**   c   *****",
    "**************"
]

statement='''
A catastrophic VIRUS is sweeping across the Emoji Kindom.
You are now acting as a Emoji Warrrior to find a CURE for all emojis.
Walk along the streets to reach the cure in limited steps.
Or the virus will REACH YOU FIRST.
Use ↑↓←→ to move your hero.
'''

cover_win = [
"██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗██╗",
"╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║██║",
" ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║██║",
"  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║╚═╝",
"   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║██╗",
"   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝"                                      
    ]   
cover_lose=[   '██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗████████╗██╗',
               '╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝╚══██╔══╝██║',
               ' ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗   ██║   ██║',
               '  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║   ██║   ╚═╝',
               '   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║   ██║   ██╗',
               '   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝'
               ]

cover_begin=[
"██╗   ██╗██╗██████╗ ██╗   ██╗███████╗     ██████╗  ██████╗", 
"██║   ██║██║██╔══██╗██║   ██║██╔════╝    ██╔════╝ ██╔═══██╗",
"██║   ██║██║██████╔╝██║   ██║███████╗    ██║  ███╗██║   ██║",
"╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║    ██║   ██║██║   ██║",
" ╚████╔╝ ██║██║  ██║╚██████╔╝███████║    ╚██████╔╝╚██████╔╝",
"  ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝     ╚═════╝  ╚═════╝" 
]


press_bottom_hint="Press any bottom to back to menu"
cover_gg=[
"██████╗   ██████╗  ██████╗ ██████╗      ██████╗  █████╗ ███╗   ███╗███████╗",
"██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝",
"██║  ███╗██║   ██║██║   ██║██║  ██║    ██║  ███╗███████║██╔████╔██║█████╗  ",  
"██║   ██║██║   ██║██║   ██║██║  ██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ",  
"╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗",
" ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝"]

drawing1=[
";;;;;;;;;;;;+*+**+;;;;;;;",
";;;;;;;;;;+*;***+??::;;;;",
";;;;;;?;;++*+*+*+*;;+;;;;",
";;;;;:;*;*+?**+***++*+;;;",
";;;;;;;+***++++;;+***+::;",
";;;;;*++;+*****+++;+++*+;",
";;;+++*++*????***+++***+:",
";;;+**+**?*????**+++;+;;;",
";;;;**+*??*?????*+++;+**+",
";;;****???????****+++++*+",
";;+******????????**++*++;",
";;;+****??**????**++;+*+;",
";;;:;+**??**??*?****+**??",
";;;****+*?????*****+**+;+",
";;;++*++***?*??****+**;:;",
";;;:;;;**++++*?***++??*+;",
";;;;;+?***+++++++**+;**+;",
";;;;;*+;+**+****+***;;;:;",
";;;;;;;:+**+?*?**+**+:;;;",
";;;;;;;;++;;*+?;*;;;;;;;;",
";;;;;;;;;;;;+;+;*;:;;;;;;"]


drawing2=[
';;;;;;++++++++++;;;;',
';;;;;;*;;;;;;;*+;;;;',
';;;;;;+++++++++;;;;;',
';;;;;;+*;;;;;*+;;;;;',
';;;;;;+*;;;;;*+;;;;;',
';;;;;;;*;;;;;*+;;;;;',
';;;;;;+*;;;;;++;;;;;',
';;;;;;*+;;;;;+*;;;;;',
';;;;;+*;;;;;;;*+;;;;',
';;;;;*+;;;;;;;+*;;;;',
';;;;+*+;;++++++*;;;;',
';;;;***++*******+;;;',
';;;+*************;;;',
';;;******+++*****+;;',
';;+******+;;+*****;;',
';;********++******+;',
';+*****************;',
';**********++******+',
'+?*********++*******',
'++++++++++++++++++++']


map_data1 = [
    "************",
    "*         p*",
    "* ****** * *",
    "*     f* * *",
    "****** * * *",
    "******     *",
    "************"
]

#flag
map_data2=[  
    "**************",
    "**p          *",
    "** ********* *",
    "** *****f  * *",
    "** ***** *   *",
    "** ***** *****",
    "**       *****",
    "**************"
]


map_data8=[  
    "*********************",
    "*       *   *       *",
    "* * *** * * * *** * *",
    "* * * * * *** * * * *",
    "* * * *         * * *",
    "* * * *********** * *",
    "*p* *             * *",
    "*** * ************* *",
    "* * * *           * *",
    "* * * * ********* * *",
    "* * *           * * *",
    "* * * ********* * * *",
    "* *   *         * * *",
    "* * *********** * * *",
    "* * *           * * *",
    "* * * *********** * *",
    "*   *             * *",
    "***** ************* *",
    "*f    *             *",
    "*********************"
]#12

map_data9=[  
"***************************************",
"*p      *           *               *f*",
"* ***** * ********* * ************* * *",
"* *   * * *       * * *           * * *",
"* * * * * * ***** * * * ********* * * *",
"* * * * * * *   * * * * *       * * * *",
"* * * * * * * * * * * * ***** * * * * *",
"* * * * * * * * * * * * *   * * * * * *",
"* * * * * * * * * * * * *** * * * * * *",
"* * * * * * * * * * * *     * * * * * *",
"* * * * * * * * * * * ***** * * * * * *",
"* * * * * * * * * * *       * * * * * *",
"* * * * * * * * * * ********* * * * * *",
"* * * * * * * * * * *       * * * * * *",
"* * * * * * * * * * ******* * * * * * *",
"* * * * * * * * * *     *   * * * * * *",
"* * * * * * * * * ***** * * * * * * * *",
"* * * * * * * * *     * * * * * * * * *",
"* * * * * * * ***** * * * * * * * * * *",
"* * * * * *       * * * * * * * * * * *",
"* * * * * ******* * * *** * * * * * * *",
"*   * *           * *     *   *   *   *",
"***************************************"
]#33


#go through all squares
map_data3=[
    "*************",
    "**     ******",
    "** **********",
    "*           *",
    "*********** *",
    "* *         *",
    "* * ***** * *",
    "* *       * *",
    "* ******* * *",
    "*         *p*",
    "*************"
]
#all
map_data4=[
    "*************",
    "******* *****",
    "*****   *****",
    "***** *******",
    "***   *   ***",
    "*** *** * ***",
    "*** *p  * ***",
    "*** * *** ***",
    "*     * *   *",
    "* ***** *** *",
    "*       *   *",
    "*************"
]
#get diamonds
map_data5=[
    "*****************",
    "*   *           *",
    "* * * * *********",
    "* *   * *       *",
    "* ************* *",
    "*             * *",
    "* ********* *** *",
    "*p        *     *",
    "*****************"
]
#get diamonds
map_data6=[
    "*********************",
    "********** **********",
    "********** **********",
    "****     * *     ****",
    "**** * * * * *** ****",
    "*    * * *   * *    *",
    "**** * ******* * ****",
    "**** *        p  ****",
    "********** **********",
    "********** **********",
    "*********************"
]
#flag
map_data7=[
    "*************",
    "****** ******",
    "****** ******",
    "****     ****",
    "**** *** ****",
    "**** *p* ****",
    "**** * * ****",
    "*      *    *",
    "** ****** ***",
    "** ****** ***",
    "**    *** ***",
    "*************"
]
map_data10 = [
    "************************",
    "*                      *",
    "*p******************** *",
    "*                    * *",
    "* ************ *** * * *",
    "* *            *   * * *",
    "* * ********** * * * * *",
    "* * *        * * * * * *",
    "* * ******** * * * * * *",
    "* *        * * * * * * *",
    "* * ****** * * * * * * *",
    "* * *    * * * * * * * *",
    "* * * **** * * * * * * *",
    "* * *      * * * * * * *",
    "* * ******** * * * * * *",
    "* *          * * * * * *",
    "* * ******** * * * * * *",
    "* *          *   *   * *",
    "* ******************** *",
    "*                      *",
    "************************"
]
map_data11 = [
"********************************************************",    
"***********************  ***********  ******************",
"*********************     *********     ****************",
"******   ************            **    *****************",
"********     ****   **************** *******************",
"*******               *            *    ******   *******",
"***********           * ********** *       **      *****",
"**********            *          * *           *********",
"*********    ******************* * *          **********",
"**** ***     *                 * * *          **********",
"**           * ******* ******* * * *          ***   ****",
"***          * *   * * *   * * * * *                  **",
"******       * * * * * * * * * * * *              ******",
"******       * * * * * * * * * * * *            ********",
"*******      * * * * * * * * * * * *            ********",
"*******      * * * * * * * * * * * *             *   ***",
"**           * * * * * * *   * * * *                 ***",
"*            * * * * * * ***** * * *          ****   ***",
"**   ****    * * * * * *       * * *         ***********",
"**********   *   *   * ********* * *        ************",
"************ ******* *           * *         ***********",
"******** **        * * *********** *    **      ********",
"*******      ****  * *             * ******    *********",
"********    ******** ************* *********************",
"******************** ************* *   *****************",
"******************      f*p        **  ******************",
"********************************************************"
]


map_list=[map_data1,map_data2,map_data3,map_data4,map_data5,map_data6,map_data7,map_data8,map_data9,map_data10,map_data11]
map_step_list=[4,5,19,28,24,32,11,12,33,38,14]

class operation(threading.Thread):
    def run(self):
        global pad_height
        global pad_width
        global stdscr
        global pad
        global player
        global pad_pos_y
        global pad_pos_x
        global pad_display_height
        global pad_display_width
        global screen_height
        global screen_width
        global key_count
        global endpoint
        global win_flag
        global game_flag
        global lose_flag
        global press_bottom_hint

        win_flag = False
        lose_flag = False

        while True:
            # 获取屏幕尺寸
            screen_height, screen_width = stdscr.getmaxyx()

            # 计算 pad 显示的区域
            pad_display_height = min(screen_height, pad_height)
            pad_display_width = min(screen_width, pad_width)
            player.display(pad, screen_height, screen_width)
            # 刷新 pad 显示的区域
            pad.refresh(pad_pos_y, pad_pos_x, 2, 4, pad_display_height - 1, pad_display_width - 1)
            
            curses.flushinp()#清空输入队列
            key = pad.getch()
            # 获取用户输入
            player.move(pad, key,screen_height, screen_width, map_data)
            # 处理用户输入
            if key == ord('q'):
                break
            if key != -1:
                key_count += 1
            if key_count > map_step:
                lose_flag = True
            
            remaining_step = map_step-key_count+1

            # 调试模块-------------------------
            pad.addstr(0, 90, f"remaining try:{remaining_step}".ljust(20," "))
            pad.addstr(8, 90, f"{endpoint}")
            pad.addstr(9, 90,"press q or Ctrl+C to exit")
            #  -----------------------------------------
            if (player.x == endpoint[0] and player.y == endpoint[1]) or player.detect_map(map_data) == False:
                win_flag = True
            #     #game_flag = True
            
            if win_flag == True:
                init()
                pad.refresh(pad_pos_y, pad_pos_x, 2, 4, pad_display_height - 1, pad_display_width - 1)
                #pad.addstr(screen_height // 2, screen_width // 2 - 4, "You win!",curses.color_pair(1))
                #pad.addstr(screen_height // 2+1, screen_width // 2 - 8, "Press any bottom to exit",curses.color_pair(1))
                pad.addstr(0, curses.COLS // 2 - len(press_bottom_hint) // 2, press_bottom_hint)
                for i, line in enumerate(cover_win):
                    pad.addstr(i + 2, curses.COLS // 2 - len(line) // 2, line)
                pad.refresh(pad_pos_y, pad_pos_x, 2, 4, pad_display_height - 1, pad_display_width - 1)
                stdscr.refresh()
                stdscr.getch()# press any bottom to exit
                time.sleep(1)
                pad.clear()
                win_flag == False
                break
            
            if lose_flag == True:
                init()
                pad.refresh(pad_pos_y, pad_pos_x, 2, 4, pad_display_height - 1, pad_display_width - 1)
                pad.addstr(0, curses.COLS // 2 - len(press_bottom_hint) // 2, press_bottom_hint)
                for i, line in enumerate(cover_lose):
                    pad.addstr(i + 2, curses.COLS // 2 - len(line) // 2, line)
                pad.refresh(pad_pos_y, pad_pos_x, 2, 4, pad_display_height - 1, pad_display_width - 1)
                stdscr.refresh()
                stdscr.getch()# press any bottom to exit
                time.sleep(1)
                pad.clear()
                win_flag == False
                break


            # 限制 pad 显示的位置在合法范围内
            pad_pos_y = max(0, min(pad_pos_y, pad_height - pad_display_height))
            pad_pos_x = max(0, min(pad_pos_x, pad_width - pad_display_width))

##------------------------------------------封装函数----------------------------------------------
def init():
    global pad
    global stdscr
    stdscr = curses.initscr()#初始化面板
    pad = curses.newpad(1000, 1000)
    curses.start_color()
    curses.use_default_colors()
    # curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)#初始化颜色2
    # curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)#初始化颜色1
    # curses.init_pair(3, curses.COLOR_RED, curses.COLOR_RED)#初始化间隔颜色
    curses.cbreak()#不必回车即可读取
    pad.keypad(True)#启用键盘响应，可调用上下键等
    curses.curs_set(False)#关闭光标显示
    curses.flushinp()#清空输入队列
    curses.noecho()#关闭字符回显
    pad.clear()#清空面板
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)#我们将鼠标事件的掩码设置为包括所有的鼠标事件（curses.ALL_MOUSE_EVENTS）以及报告鼠标位置的能力（curses.REPORT_MOUSE_POSITION）

def end():
    curses.flushinp()#清空输入队列
    pad.keypad(False)#关闭键盘响应，可调用上下键等
    curses.echo()#开启字符回显
    curses.curs_set(True)#开启车光标显示
    curses.nocbreak()#需要回车才可读取
    pad.clear()#清空面板
    curses.endwin()#鲨掉窗口



def draw_menu(pad):
    global pad_height
    global pad_width
    global pad_pos_y
    global pad_pos_x
    global pad_display_height
    global pad_display_width
    global screen_height
    global screen_width
    global key_count
    global endpoint
    global win_flag
    global game_flag
    global emoji
    global drawing1
    global cover_gg
    global cover_begin

    game_flag = True
    
    pad_pos_y = 0
    pad_pos_x = 0


    menu_options = ["Start", "Exit"] 
    selected_option = 0
    drawing1_height=len(drawing1)
    drawing1_width=len(drawing1[0])
    
    while True:
        pad.clear()
        screen_height, screen_width = stdscr.getmaxyx()
        pad_display_height = min(screen_height, pad_height)
        pad_display_width = min(screen_width, pad_width)
        # 绘制菜单选项
        for i, option in enumerate(menu_options):
            if i == selected_option:
                pad.addstr(i+10, 80, option, curses.color_pair(2))
            else:
                pad.addstr(i+10, 80, option, curses.color_pair(1))
        

        # 在 pad 上绘制virus
        for y in range(drawing1_height):
            for x in range(drawing1_width):
                if drawing1[y][x] == ';':
                    pass
                elif drawing1[y][x] == '?':
                    pad.addstr(y, x * 2, "  ", curses.color_pair(5))

                elif drawing1[y][x] == '*':
                    pad.addstr(y, x * 2, "  ", curses.color_pair(4))

                else:
                    pad.addstr(y, x * 2, "  ", curses.color_pair(6))
        
        for i, line in enumerate(cover_begin):
            pad.addstr(i + 2, curses.COLS // 2 - len(line) // 2, line)

        # 刷新 pad 显示
        pad.refresh(pad_pos_y, pad_pos_x, 2, 4, pad_display_height - 1, pad_display_width - 1)

        # 键盘输入检测
        key = pad.getch()

        # 处理键盘输入
        if key == curses.KEY_UP:
            selected_option = (selected_option - 1) % len(menu_options)
        elif key == curses.KEY_DOWN:
            selected_option = (selected_option + 1) % len(menu_options)
        elif key == curses.KEY_ENTER or key == 10:  # 处理回车键
            if selected_option == 0:
                emoji=choose_character(pad,pad_pos_y, pad_pos_x,screen_height, screen_width, pad_display_height, pad_display_width)
                map_num=choose_map(pad,pad_pos_y, pad_pos_x,screen_height, screen_width, pad_display_height, pad_display_width)
                pad.clear()
                break
            elif selected_option == 1:
                game_flag = False
                #stdscr.addstr(screen_height // 2, screen_width // 2 - 6, "Good Game!")
                #stdscr.addstr(screen_height // 2+1, screen_width // 2 - 12, "Press any bottom to exit")
                pad.refresh(pad_pos_y, pad_pos_x, 2, 4, pad_display_height - 1, pad_display_width - 1)
                #pad.addstr(0, curses.COLS // 2 - len(press_bottom_hint) // 2, press_bottom_hint)
                for i, line in enumerate(cover_gg):
                    pad.addstr(i + 2, curses.COLS // 2 - len(line) // 2, line)
                pad.refresh(pad_pos_y, pad_pos_x, 2, 4, pad_display_height - 1, pad_display_width - 1)
                time.sleep(3)
                #stdscr.refresh()

                stdscr.getch() # press any bottom to exit
                stdscr.clear()
                # 加入一点结束的东西
                break
    # 刷新 pad 显示
    pad.refresh(pad_pos_y, pad_pos_x, 2, 4, pad_display_height - 1, pad_display_width - 1)


def choose_character(pad,pad_pos_y, pad_pos_x,screen_height, screen_width, pad_display_height, pad_display_width):
    global map_example,statement

    menu_options = ["😅","😇","😍","🤡"] 
    selected_option = 0    
    start_row = (pad_display_height - len(menu_options)) // 2
    start_col = (pad_display_width - max(len(option) for option in menu_options)) // 2
    map_height=len(map_example)
    map_width=len(map_example[0])
    while True:
        pad.clear()
        screen_height, screen_width = stdscr.getmaxyx()
        pad_display_height = min(screen_height, pad_height)
        pad_display_width = min(screen_width, pad_width)
        pad.addstr(1, 70, 'Choose your character', curses.color_pair(1))
        for y in range(map_height):
            for x in range(map_width):
                if map_example[y][x] == '*':
                    pad.addstr(y, x * 2, "  ", curses.color_pair(2)) 
                elif map_example[y][x] == 'a':
                        pad.addstr(y, x * 2, "😅", curses.color_pair(1))
                        endpoint = [x*2,y]
                elif map_example[y][x] == 'b':
                        pad.addstr(y, x * 2, "💊", curses.color_pair(1))
                        endpoint = [x*2,y]
                elif map_example[y][x] == 'c':
                        pad.addstr(y, x * 2, "🦠", curses.color_pair(1))
                        endpoint = [x*2,y]
                else:
                    pad.addstr(y, x * 2, '  ', curses.color_pair(1))
        pad.addstr(10, 6, statement, curses.color_pair(1))
        # Draw menu options
        for i, option in enumerate(menu_options):
            if i == selected_option:
                pad.addstr(start_row + i, start_col, option, curses.color_pair(2))
            else:
                pad.addstr(start_row + i, start_col, option, curses.color_pair(1))

        # Refresh pad display
        pad.refresh(pad_pos_y, pad_pos_x, 2, 4, pad_display_height - 1, pad_display_width - 1)

        # Keyboard input handling
        key = pad.getch()

        # Process keyboard input
        if key == curses.KEY_UP:
            selected_option = (selected_option - 1) % len(menu_options)
        elif key == curses.KEY_DOWN:
            selected_option = (selected_option + 1) % len(menu_options)
        elif key == curses.KEY_ENTER or key == 10:  # Handle Enter key
            return menu_options[selected_option]
    # Refresh pad display
    pad.refresh(pad_pos_y, pad_pos_x, 2, 4, pad_display_height - 1, pad_display_width - 1)

def choose_map(pad,pad_pos_y, pad_pos_x,screen_height, screen_width, pad_display_height, pad_display_width):
    global map_data
    global map_list
    global map_step
    global cover_gg
    global drawing2
    menu_options = [" 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10","11", "exit"] 
    selected_option = 0    
    start_row = (pad_display_height - len(menu_options)) // 2
    start_col = (pad_display_width - max(len(option) for option in menu_options)) // 2
    drawing2_height=len(drawing2)
    drawing2_width=len(drawing2[0])
    while True:
        pad.clear()
        screen_height, screen_width = stdscr.getmaxyx()
        pad_display_height = min(screen_height, pad_height)
        pad_display_width = min(screen_width, pad_width)
        
        pad.addstr(1, 60, 'Choose your map', curses.color_pair(1))
        #pad.addstr(2, 60, str(selected_option), curses.color_pair(1))

        # Draw menu options
        for y in range(drawing2_height):
                for x in range(drawing2_width):
                    if drawing2[y][x] == ';':
                        pass
                    elif drawing2[y][x] == '+':
                        pad.addstr(y, x * 2, "  ", curses.color_pair(5))
                    elif drawing2[y][x] == '*':
                        pad.addstr(y, x * 2, "  ", curses.color_pair(6))
                   

        for i, option in enumerate(menu_options):
            if i == selected_option:
                pad.addstr(start_row + i, start_col, option, curses.color_pair(2))
            else:
                pad.addstr(start_row + i, start_col, option, curses.color_pair(1))

        # Refresh pad display
        pad.refresh(pad_pos_y, pad_pos_x, 2, 4, pad_display_height - 1, pad_display_width - 1)

        # Keyboard input handling
        key = pad.getch()

        # Process keyboard input
        if key == curses.KEY_UP:
            selected_option = (selected_option - 1) % len(menu_options)
        elif key == curses.KEY_DOWN:
            selected_option = (selected_option + 1) % len(menu_options)
        elif key == curses.KEY_ENTER or key == 10:  # Handle Enter key
  
            if selected_option == len(menu_options)-1:
                game_flag = False
                #stdscr.addstr(screen_height // 2, screen_width // 2 - 6, "Good Game!")
                #stdscr.addstr(screen_height // 2+1, screen_width // 2 - 12, "Press any bottom to exit")
                #pad.addstr(0, curses.COLS // 2 - len(press_bottom_hint) // 2, press_bottom_hint)
                for i, line in enumerate(cover_gg):
                    pad.addstr(i + 2, curses.COLS // 2 - len(line) // 2, line)
                pad.refresh(pad_pos_y, pad_pos_x, 2, 4, pad_display_height - 1, pad_display_width - 1)
                time.sleep(3)
                #stdscr.refresh()
                stdscr.getch() # press any bottom to exit
                stdscr.clear()
                raise KeyboardInterrupt
                # 加入一点结束的东西
                break
            else:   
                # map_num = selected_option
                # map_data = map_list[map_num]
                pad.clear()
                map_data=map_list[selected_option]
                map_step=map_step_list[selected_option]
                return selected_option
        
        
    # Refresh pad display
    pad.refresh(pad_pos_y, pad_pos_x, 2, 4, pad_display_height - 1, pad_display_width - 1)

#-----------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    global pad_height
    global pad_width
    global stdscr
    global pad
    global player
    global pad_pos_y
    global pad_pos_x
    global key_count
    global endpoint 
    global printf_flag


    init()
    # 定义颜色对
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_CYAN)

    # 创建一个 pad


    pad_height = 500
    pad_width = 500
    pad = curses.newpad(pad_height, pad_width)
    pad.keypad(True)
    pad_pos_y = 0
    pad_pos_x = 0
    
    draw_menu(pad)
    

    
    
    while game_flag:
        printf_flag = False
        endpoint = [0,0]
        map_height = len(map_data)
        map_width = len(map_data[0])
        # 在 pad 上绘制地图
        for y in range(map_height):
            for x in range(map_width):
                if map_data[y][x] == '*':
                    pad.addstr(y, x * 2, "  ", curses.color_pair(2))
                elif map_data[y][x] == 'f':
                    pad.addstr(y, x * 2, "💊", curses.color_pair(1))
                    endpoint = [x*2,y]


                elif map_data[y][x] == 'p':
                    pad.addstr(y, x * 2, " ", curses.color_pair(1))
                    initpoint = [x*2,y]
                else:
                    pad.addstr(y, x * 2, "  ", curses.color_pair(1))
        pad.refresh(pad_pos_y, pad_pos_x, 2, 4, pad_display_height - 1, pad_display_width - 1)
        # 初始显示的位置
        if endpoint == [0,0]:
            printf_flag = True

        player = base.Baseclass(initpoint[0],initpoint[1],1,flag=True,emoji=emoji,step=map_step,printf_flag=printf_flag,endpoint=endpoint)
        key_count = 0
        
        
        
        #多线程模块
        mainthing = operation()
        # mainthing.get(stdscr)
        mainthing.start()
        mainthing.join()
        choose_map(pad,pad_pos_y, pad_pos_x,screen_height, screen_width, pad_display_height, pad_display_width)


try: 
    main()

except KeyboardInterrupt:
    pad.clear()

finally:
    # 还原终端设置
    end()





