#-*- coding: utf-8 -*-
#第一个参数是打印文本
#第二个参数是选择这条线以后出现的对话
#第三个参数是其指向的新路线
#下面是一个例子

#计算机对话，第二个参数的第一项如果是-1表示故事结束
live_in_net_cpt_msg = [
		['help!\nhelp!\nhelp!\n',[0,1]],
		['thanks god,finally someone to help me out\n',[2]],
		['oh my god!',[-1]],
	]
#玩家对话，第二个参数如果是-1，表示故事结束
live_in_net_ply_chs = [
		['what\'s wrong?',1],
		['is this joking?',1],
        ['Sorry i am coding,we speak later',2],
	]

#每一个故事都是这样的一个列表,第一项表示AI对话，第二项表示玩家选择
story_live_in_net = [live_in_net_cpt_msg,live_in_net_ply_chs]



story_test = []

#这是所有的故事，每加一个故事要在这里加一个字典项
storys={'live in net':story_live_in_net,'test':story_test}

#输入接口，便于修改成sdk的形式
def input(msg=''):
	return raw_input(msg)

#输出接口
def output(msg=''):
	print msg

#游戏开始时选择故事的部分
def choose_story():
	print 'Please choose your storys: '
	i=0
	story = None
	for item in storys.keys():
		i+=1
		output(str(i)+':'+item)
	return storys[storys.keys()[int(input('Please input the number'))-1]]

#剧情分支部分
def get_next_message_from_story(story,num):
	output(story[0][num][0])
	i=0
	for point in story[0][num][1]:
		output(str(i)+':'+story[1][point][0])
		i+=1
	choosednum = story[0][num][1][int(input('your choose:'))]
	if choosednum<0:
		return -1
	return story[1][choosednum][1]


#入口函数，虽然没必要，但是遵循习惯吧
def main():
	story = choose_story()
	num = 0
	while num>-1:
		num = get_next_message_from_story(story,num)

main()