


# author: CYX
# Created on 10/28/2023 6:58 PM
import curses
import time


class Baseclass():

    def __init__(self, x, y, tag, flag, emoji, step, printf_flag=False, endpoint=True):
        self.x = x
        self.y = y
        self.tag = tag
        self.flag = flag
        self.index = {"up": True, "down": True, "left": True, "right": True, 'empty': False}
        self.endpoint = endpoint
        self.printf_flag = printf_flag
        self.emoji = emoji
        self.step = step
        # self.color_pair = curses.color_pair(pad.inch(y,x) & curses.A_COLOR)
        # self.pretag = curses.pair_number(self.color_pair)

    def display(self, pad, height, width):
        pad.addstr(self.y, self.x, self.emoji, curses.color_pair(self.tag))
        self.index, count = self.detect(pad)
        # 调试模块-------------------------
        pad.addstr(1, 90, "Index:")
        pad.addstr(2, 90, "Up: {}".format(str(self.index["up"]).ljust(5)))
        pad.addstr(3, 90, "Down: {}".format(str(self.index["down"]).ljust(5)))
        pad.addstr(4, 90, "Left: {}".format(str(self.index["left"]).ljust(5)))
        pad.addstr(5, 90, "Right: {}".format(str(self.index["right"]).ljust(5)))
        pad.addstr(6, 90, "Count: {}   {}".format(self.step-count, self.flag))
        pad.addstr(7, 90, "x:{},y:{}".format(self.x,self.y))
        pad.addstr(7, 90, "x:{},y:{}".format(self.x,self.y))
        #-----------------------------------------

    def move(self, pad,key, height, width, map_data):
        # pad.addstr(0,0,str(key))
        # pad.refresh(0,0,0,0,5,5)
        # time.sleep(1000)
        if key != -1:
            # 判定移动方向
            movement = ''
            direction = {"up": [0, -1], "down": [0, 1], "left": [-1, 0], "right": [1, 0]}
            if key == curses.KEY_UP:
                movement = 'up'
            elif key == curses.KEY_DOWN:
                movement = 'down'
            elif key == curses.KEY_LEFT:
                movement = 'left'
            elif key == curses.KEY_RIGHT:
                movement = 'right'
            else:
                movement = 'empty'
            self.index, count = self.detect(pad) 
            # while 前处理一次
            

            
            #player移動尾跡處理
            if self.printf_flag == True:
                pad.addstr(self.y, self.x, "  ", curses.color_pair(4))
            else:
                pad.addstr(self.y, self.x, "  ", curses.color_pair(1))
            self.index, count = self.detect(pad)

            while (self.index[movement] == True):
                # if self.x == self.endpoint[0] and self.y == self.endpoint[1]:
                #     break
                # else:
                self.index, count = self.detect(pad)
                lx,ly = self.x,self.y
                self.x += direction[movement][0]
                self.y += direction[movement][1]
                self.display(pad, height, width)
                pad.refresh(0, 0, 2, 4, height - 1, width - 1)
                # 对map处理
                if self.printf_flag == True:
                    map_xline = list(map_data[self.y])
                    map_xline[self.x//2] = '0'
                    map_xline = ''.join(map_xline)
                    map_data[self.y] = map_xline
                # 循环or夺旗模式
                if self.printf_flag == True:
                    pad.addstr(self.y, self.x, "  ", curses.color_pair(4))
                else:
                    pad.addstr(self.y, self.x, "  ", curses.color_pair(1))
                time.sleep(0.05)
                pad.refresh(0, 0, 2, 4, height - 1, width - 1)
                if self.flag == False:
                    break
                    # time.sleep(1)
        

    def detect(self, pad):
        # 检测上方块的颜色
        color_up_1 = pad.inch(self.y - 1, self.x) & curses.A_COLOR
        color_up_2 = pad.inch(self.y - 1, self.x+1) & curses.A_COLOR
        self.index["up"] = False if (color_up_1 == curses.color_pair(2) or color_up_2 == curses.color_pair(2)) else True
        # 检测下方块的颜色
        color_down_1 = pad.inch(self.y + 1, self.x) & curses.A_COLOR
        color_down_2 = pad.inch(self.y + 1, self.x+1) & curses.A_COLOR
        self.index["down"] = False if (color_down_1 == curses.color_pair(2) or color_down_2 == curses.color_pair(2)) else True
        # 检测左方块的颜色
        color_left = pad.inch(self.y, self.x - 1) & curses.A_COLOR
        self.index["left"] = False if color_left == curses.color_pair(2) else True
        # 检测右方块的颜色
        color_right = pad.inch(self.y, self.x + 2) & curses.A_COLOR
        self.index["right"] = False if color_right == curses.color_pair(2) else True
        # 判斷周圍道路個數
        count = sum(1 for value in self.index.values() if value is False)-1
        self.flag = True if count >= 2 else False
    
        return self.index, count
    
    def detect_map(self,map_data):
        map_y = len(map_data)
        map_x = len(map_data[0])
        loop_flag = False
        break_flag= False
        for y in range(map_y):
            for x in range(map_x):
                if map_data[y][x] == ' ':
                    break_flag=True
                    loop_flag=True
                    break
            if break_flag: break
        return loop_flag









