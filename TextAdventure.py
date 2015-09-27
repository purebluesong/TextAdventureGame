#-*- coding: utf-8 -*-
#@sprout
#第一个参数是打印文本
#第二个参数是选择这条线以后出现的对话
#第三个参数是其指向的新路线
#下面是一个例子

#计算机对话，第二个参数的第一项如果是-1表示故事结束
cpt_msg = open("cpt_msg.txt").read().splitlines()

live_in_net_cpt_msg = []

#这里对话和后面数字间用‘|’分开，-1我设置为在文件中为‘#’，偷个懒@mooc@sprout
for cpt_line in cpt_msg:
	params = cpt_line.split('|')
	talk = []
	talk.append(params[0])
	if params[1]=='#':
		talk.append([-1])
	else:
		nums = []
		for item in params[1:]:
			nums.append(int(item))
		talk.append(nums)
		live_in_net_cpt_msg.append(talk)

#玩家对话，第二个参数如果是-1，表示故事结束
ply_chs = open("ply_chs.txt").read().splitlines()

live_in_net_ply_chs = []
#玩家对话后面直接接数字//数字可能超出个位数，所以也仿照上面的用|分开了@mooc@sprout
for ply_line in ply_chs:
	params = ply_line.split('|')
	talk = []
	talk.append(params[0])
	talk.append(int(params[1]))
	live_in_net_ply_chs.append(talk)


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
	output('Please choose your storys: ')
	i=0
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
		output(story[1][choosednum][0])
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