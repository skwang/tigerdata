from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from models import *

def index(request):
	context_dict = {'logged_in': request.user.is_authenticated()}
	return render(request, 'tigredata/index.html', context_dict)

def get_dorm_list(request):
	if HallList.objects.all():
		return JsonResponse({'dorm_list': HallList.objects.all()[0].halls})
	else:
	 	return JsonResponse({'dorm_list': ['Error', 'Database', 'Has', 'No', 'List', 'Help!']})

def checkAdj(room1, room2):
	length = len(room1)
	value = 1
	if room1[0] == room2[0]:
		if room1[1] == room2[1]:
			return 5
		elif abs(int(room1[1]) - int(room2[1])) == 1:
			return 1
	return -1
	# for i in range(0, length):
	# 	if abs(int(room1[i]) - int(room2[i])) == 1:
	# 		value += 1
	# 	elif room1[i] == room2[i]:
	# 		value += 2
	# if value == 1:
	# 	return -1
	# else:
	# 	return value


def get_dorm_graph(request):
	from random import randrange
	import math

	if request.method == "GET":
		query = request.GET['dorm']
		students = Student.objects.filter(hall=query)

		majortable = {}
		majorindex = 0
		roomtable = {}
		nodetable = {}

		nodes = []
		links = []

		nodeindex = 0

		for student in students:
			if student.major not in majortable:
				majortable[student.major] = majorindex
				majorindex += 1
			snode = {"name": student.netid, "group":majortable[student.major]}
			nodetable[student.netid] = nodeindex
			nodeindex += 1
			nodes.append(snode)
			if student.room not in roomtable:
				roomtable[student.room] = [snode]
			else:
				ls = roomtable[student.room]
				ls.append(snode)
				roomtable[student.room] = ls

		for roomkey in roomtable.keys():
			room = roomtable[roomkey]
			# link the nodes in a room together
			for snode in room:
				for othernode in room:
					if snode == othernode: 
						continue
					links.append({
									"source": nodetable[snode["name"]], 
									"target": nodetable[othernode["name"]],
									"value": 10
								})
			# link the rooms together
			# for otherkey in roomtable.keys():
			# 	otherroom = roomtable[otherkey]
			# 	if room == otherroom:
			# 		continue
			# 	roomAdj = checkAdj(roomkey, otherkey)
			# 	if roomAdj > 0:
			# 		snode = room[0]
			# 		othernode = otherroom[0]
			# 		#for snode in room:
			# 			#for othernode in otherroom:
			# 		links.append({
			# 						"source": nodetable[snode["name"]], 
			# 						"target": nodetable[othernode["name"]],
			# 						"value": roomAdj
			# 					})



		graph = {"nodes":nodes, "links":links}

		'''	
		# random graph of 100 nodes
		nnodes = 100
		nodes = []
		links = []

		for i in range(0, nnodes):
			nodes.append({"name": str(i), "group": int(i*7/nnodes)})

		for i in range(0, int(nnodes*1.15)):
			source = i % nnodes
			target = int(math.log(1 + randrange(nnodes), 1.3))
			value = 10.0 / (1 + abs(source - target))
			links.append({"source": source, "target": target, "value": value * value})

		graph = {"nodes":nodes, "links":links}
		'''
	return JsonResponse(graph)