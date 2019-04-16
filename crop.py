import sys

from PIL import Image
import cv2

import os
import os.path


batch_info_1 = {
	"srcdir":"/home/eroux/BUDA/Incoming/ffy/004/1/",
	"dstdir":"output/W0FFY004/images/W0FFY004-I0FFY004/",
	"leftlimit":517,
	"rightlimit":4686,
	"firstfolnum":1,
	"horlimits" : [
		(418,918),
		(896,1441),
		(1424,1941),
		(1941,2464),
		(2453,2981)
	],
	"resizefactor":0.80,
	"outformat":'TIFF'
}


batch_info_2 = {
	"srcdir":"/home/eroux/BUDA/Incoming/ffy/004/2/",
	"dstdir":"output/W0FFY004/images/W0FFY004-I0FFY004/",
	"leftlimit":350,
	"rightlimit":4900,
	"firstfolnum":61,
	"horlimits" : [
		(324,951),
		(863,1506),
		(1407,2034),
		(1941,2617),
		(2462,3194)
	],
	"resizefactor":0.80,
	"outformat":'JPEG'
}

batch_info_3 = {
	"srcdir":"/home/eroux/BUDA/Incoming/ffy/004/3/",
	"dstdir":"output/W0FFY004/images/W0FFY004-I0FFY004/",
	"leftlimit":467,
	"rightlimit":4800,
	"firstfolnum":136,
	"horlimits" : [
		(918,1451),
		(1451,1952),
		(1952,2617)
	],
	"resizefactor":0.80,
	"outformat":'JPEG'
}

batch_info_4 = {
	"srcdir":"/home/eroux/BUDA/Incoming/ffy/003/1/",
	"dstdir":"output/W0FFY003/images/W0FFY003-I0FFY003/",
	"leftlimit":379,
	"rightlimit":4725,
	"firstfolnum":1,
	"horlimits" : [
		(318,920),
		(742,1391),
		(1171,1890),
		(1655,2360),
		(2221,2876),
		(2560,3289)
	],
	"resizefactor":0.80,
	"outformat":'JPEG',
	"mode": "L"
}

batch_info_5 = {
	"srcdir":"/home/eroux/BUDA/Incoming/ffy/003/2/",
	"dstdir":"output/W0FFY003/images/W0FFY003-I0FFY003/",
	"leftlimit":379,
	"rightlimit":4725,
	"firstfolnum":193,
	"horlimits" : [
		(412,872),
		(828,1364),
		(1296,1824),
		(1696,2320),
		(2200,2964)
	],
	"resizefactor":0.80,
	"outformat":'JPEG',
	"mode": "L"
}

batch_info_6 = {
	"srcdir":"/home/eroux/BUDA/Incoming/ffy/002/1/",
	"dstdir":"output/W0FFY002/images/W0FFY002-I0FFY002/",
	"leftlimit":263,
	"rightlimit":4905,
	"firstfolnum":1,
	"firstfolside":'a',
	"lastfolnum":72,
	"lastfolside":'a',
	"horlimits" : [
		(456,1193),
		(1072,1836),
		(1748,2513),
		(2408,3168)
	],
	"resizefactor":0.80,
	"outformat":'JPEG',
	"mode": "L"
}

batch_info_7 = {
	"srcdir":"/home/eroux/BUDA/Incoming/ffy/002/2/",
	"dstdir":"output/W0FFY002/images/W0FFY002-I0FFY002/",
	"leftlimit":263,
	"rightlimit":4905,
	"firstfolnum":69,
	"firstfolside":'b',
	"lastfolnum":76,
	"lastfolside":'b',
	"horlimits" : [
		(456,1193),
		(1072,1836),
		(1748,2513),
		(2408,3168)
	],
	"resizefactor":0.80,
	"outformat":'JPEG',
	"mode": "L"
}

batch_info_72 = {
	"srcdir":"/home/eroux/BUDA/Incoming/ffy/002/22/",
	"dstdir":"output/W0FFY002/images/W0FFY002-I0FFY002/",
	"leftlimit":263,
	"rightlimit":4905,
	"firstfolnum":77,
	"firstfolside":'a',
	"lastfolnum":161,
	"lastfolside":'a',
	"horlimits" : [
		(274,912),
		(835,1523),
		(1435,2128),
		(2034,2733),
		(2645,3288)
	],
	"resizefactor":0.80,
	"outformat":'JPEG',
	"mode": "L"
}

batch_info_8 = {
	"srcdir":"/home/eroux/BUDA/Incoming/ffy/002/3/",
	"dstdir":"output/W0FFY002/images/W0FFY002-I0FFY002/",
	"leftlimit":373,
	"rightlimit":5010,
	"firstfolnum":157,
	"firstfolside":'b',
	"lastfolnum":251,
	"lastfolside":'a',
	"horlimits" : [
		(274,912),
		(835,1523),
		(1435,2128),
		(2034,2733),
		(2645,3288)
	],
	"resizefactor":0.80,
	"outformat":'JPEG',
	"mode": "L"
}

batch_info_9 = {
	"srcdir":"/home/eroux/BUDA/Incoming/ffy/002/4/",
	"dstdir":"output/W0FFY002/images/W0FFY002-I0FFY002/",
	"leftlimit":373,
	"rightlimit":5010,
	"firstfolnum":247,
	"firstfolside":'b',
	"lastfolnum": 336,
	"lastfolside": 'b',
	"horlimits" : [
		(274,912),
		(835,1523),
		(1435,2128),
		(2034,2733),
		(2645,3288)
	],
	"resizefactor":0.80,
	"outformat":'JPEG',
	"mode": "L"
}

batch_info_10 = {
	"srcdir":"/home/eroux/BUDA/Incoming/ffy/002/5/",
	"dstdir":"output/W0FFY002/images/W0FFY002-I0FFY002/",
	"leftlimit":337,
	"rightlimit":5010,
	"firstfolnum":337,
	"firstfolside":'a',
	"lastfolnum": 371,
	"lastfolside": 'b',
	"horlimits" : [
		(274,912),
		(835,1523),
		(1435,2128),
		(2034,2733),
		(2645,3288)
	],
	"resizefactor":0.80,
	"outformat":'JPEG',
	"mode": "L"
}

batch_info_11 = {
	"srcdir":"/home/eroux/BUDA/Incoming/ffy/002/6/",
	"dstdir":"output/W0FFY002/images/W0FFY002-I0FFY002/",
	"leftlimit":373,
	"rightlimit":5010,
	"firstfolnum":372,
	"firstfolside":'a',
	"horlimits" : [
		(731,1358),
		(1495,2056),
		(2155,2744)
	],
	"resizefactor":0.80,
	"outformat":'JPEG',
	"mode": "L"
}

batch_info_12 = {
	"srcdir":"/home/eroux/BUDA/Incoming/ffy/001/1/",
	"dstdir":"output/W0FFY001/images/W0FFY001-I0FFY001/",
	"leftlimit":120,
	"rightlimit":4894,
	"firstfolnum":1,
	"firstfolside":'a',
	"lastfolnum": 72,
	"lastfolside": 'b',
	"horlimits" : [
		(390,1077),
		(995,1836),
		(1665,2540),
		(2408,3162)
	],
	"resizefactor":0.80,
	"outformat":'JPEG',
	"mode": "L"
}

batch_info_13 = {
	"srcdir":"/home/eroux/BUDA/Incoming/ffy/001/2/",
	"dstdir":"output/W0FFY001/images/W0FFY001-I0FFY001/",
	"leftlimit":197,
	"rightlimit":4966,
	"firstfolnum":73,
	"firstfolside":'a',
	"lastfolnum": 144,
	"lastfolside": 'b',
	"horlimits" : [
		(390,1077),
		(995,1836),
		(1665,2540),
		(2408,3162)
	],
	"resizefactor":0.80,
	"outformat":'JPEG',
	"mode": "L"
}

batch_info_14 = {
	"srcdir":"/home/eroux/BUDA/Incoming/ffy/001/3/",
	"dstdir":"output/W0FFY001/images/W0FFY001-I0FFY001/",
	"leftlimit":120,
	"rightlimit":4894,
	"firstfolnum":145,
	"firstfolside":'a',
	"lastfolnum": 216,
	"lastfolside": 'b',
	"horlimits" : [
		(390,1077),
		(995,1836),
		(1665,2540),
		(2408,3162)
	],
	"resizefactor":0.80,
	"outformat":'JPEG',
	"mode": "L"
}

batch_info_15 = {
	"srcdir":"/home/eroux/BUDA/Incoming/ffy/001/4/",
	"dstdir":"output/W0FFY001/images/W0FFY001-I0FFY001/",
	"leftlimit":120,
	"rightlimit":4894,
	"firstfolnum":213,
	"firstfolside":'b',
	"lastfolnum": 280,
	"lastfolside": 'b',
	"horlimits" : [
		(390,1077),
		(995,1836),
		(1665,2540),
		(2408,3162)
	],
	"resizefactor":0.80,
	"outformat":'JPEG',
	"mode": "L"
}

def run_batch(bi):
	list_dir = os.listdir(bi["srcdir"])
	list_dir = sorted(list_dir)
	i = bi["firstfolnum"]
	side = 'a'
	if "firstfolside" in bi:
		side = bi["firstfolside"]
	nbfolioperimg = len(bi["horlimits"])
	os.makedirs(bi["dstdir"], exist_ok=True)
	lasti=0
	lastside = 'a'
	for imfn in list_dir:
		#print(bi["srcdir"]+imfn)
		im = Image.open(bi["srcdir"]+imfn)
		if "mode" in bi and im.mode != bi["mode"]:
			im = im.convert(bi["mode"])
		initiali = i
		for holim in bi["horlimits"]:
			box = (bi["leftlimit"], holim[0], bi["rightlimit"], holim[1])
			imres = im.crop(box)
			if "resizefactor" in bi and bi["resizefactor"] != 1:
				newdim = (int(imres.width*bi["resizefactor"]),int(imres.height*bi["resizefactor"]))
				imres = imres.resize(newdim, Image.ANTIALIAS)
			#print("saving ", outfn)
			if "outformat" not in bi or bi["outformat"] == 'JPEG':
				quality=75
				if "outquality" in bi:
					quality=int(100*bi["outquality"])
				outfn = bi["dstdir"]+("%03d"%i)+side+".jpg"
				imres.save(outfn, 'JPEG', quality=quality, optimize=True, progressive=True)
			elif bi["outformat"] == 'TIFF':
				outfn = bi["dstdir"]+("%03d"%i)+side+".tif"
				imres.save(outfn, 'TIFF', compression="tiff_deflate")
			lasti = i
			lastside = side
			i += 1
		if side == 'a':
			i = initiali
			side = 'b'
		else:
			side = 'a'
	if "lastfolnum" in bi:
		if lasti != bi["lastfolnum"] or lastside != bi["lastfolside"]:
			print("error: last is ",lasti,lastside,", should be ",bi["lastfolnum"],bi["lastfolside"])

def normalize_dir(dirname, prefix):
	list_dir = os.listdir(dirname)
	list_dir = sorted(list_dir)
	i = 1
	for filename in list_dir:
		extension = os.path.splitext(filename)[1]
		newname = prefix + ("%0.4d" % i) + extension
		if newname != filename:
			os.rename(dirname+filename, dirname+newname)
		i += 1

#run_batch(batch_info_1)
run_batch(batch_info_2)
run_batch(batch_info_3)
run_batch(batch_info_4)
# run_batch(batch_info_5)
# run_batch(batch_info_6)
# run_batch(batch_info_7)
# run_batch(batch_info_72)
# run_batch(batch_info_8)
# run_batch(batch_info_9)
# run_batch(batch_info_10)
# run_batch(batch_info_11)
# run_batch(batch_info_12)
# run_batch(batch_info_13)
# run_batch(batch_info_14)
# run_batch(batch_info_15)

# normalize_dir("output/W0FFY001/images/W0FFY001-I0FFY001/", "I0FFY001")
# normalize_dir("output/W0FFY002/images/W0FFY002-I0FFY002/", "I0FFY002")
# normalize_dir("output/W0FFY003/images/W0FFY003-I0FFY003/", "I0FFY003")
# normalize_dir("output/W0FFY004/images/W0FFY004-I0FFY004/", "I0FFY004")
#normalize_dir("output/W0FFY005/images/W0FFY005-I0FFY005/", "I0FFY005")
#normalize_dir("output/W0FFY006/images/W0FFY006-I0FFY006/", "I0FFY006")
#normalize_dir("output/W0FFY007/images/W0FFY007-I0FFY007/", "I0FFY007")