import sys

from PIL import Image
import cv2

import os
import os.path

fixlist3 = ["006a", "012b", "018b", "024b", "032b", "040a", "050b", "054a", "060a", "069a", "075a", "084b", "090b", "100b", "108b", "118b", "126b", "135a", "178b",
"006b", "014a", "021b", "027b", "033a", "040b", "051a", "054b", "060b", "070a", "075b", "087a", "093a", "102a", "112a", "120a", "129a", "150a", "180b",
"010a", "015a", "022a", "028a", "033b", "046a", "051b", "057a", "063a", "072a", "078a", "087b", "094a", "102b", "112b", "120b", "132a", "150b", "186a",
"010b", "017b", "023b", "030a", "034a", "046b", "052a", "057b", "064a", "072b", "078b", "088a", "096a", "105a", "114a", "123b", "132b", "156b", "186b",
"012a", "018a", "024a", "030b", "039a", "048b", "052b", "058a", "068a", "074a", "084a", "090a", "096b", "108a", "117a", "126a", "133a", "159a", "036a", "036b", "042a",
"042b", '048a', "081a", "081b", "082a", "082b", "106a", "111a", "116a", "138a", "138b", "144a", "144b", "171a", "162a", "162b", "174a", "174b", "192a", "192b", "009a", "009b",
"015b", "016a", "016b", "022b", "027a", "028b", "034b", "035a", "035b", "038a", "038b", "045a", "045b", "050a", "053b", "056a", "058b", "062a", "064b", "066a", "066b", "068b",
"069b", "070b", "071a", "076a", "076b", "080a", "081a", "086b", "088b", "092a", "093b", "100a", "104a", "106b", "110a", "110b", "114b", "118a", "122a", "123a", "124a",
"124b", "128a", "128b", "129b", "130a", "130b", "131a", "134a", "135b", "136a", "136b", "142a", "147a", "148a", "154a", "156a", "160a", "165b", "166b", "168b", "170a", "170b",
"171b", "172b", "172a", "177a", "177b", "178a", "179b", "180a", "036a", "036b", "039b", "041a", "044b", "047a", "053a", "059a", "060b", "063b", "065a", "077a", "080b", 
"086a", "094b", "095a", "098a", "099a", "105b", "111b", "113a", "116b", "117b", "132a", "137a", "141a", "141b", "146a", "160b", "168a", "173b", "180b", "189b", "190b",
"020b", "021a"]

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
	"outformat":'JPEG'
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
	# there is a duplication of 302 a so we add 5 to the expectation
	"lastfolnum": 306,
	"lastfolside": 'a',
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

batch_info_92 = {
	"srcdir":"/home/eroux/BUDA/Incoming/ffy/002/42/",
	"dstdir":"output/W0FFY002/images/W0FFY002-I0FFY002/",
	"leftlimit":373,
	"rightlimit":5010,
	"firstfolnum":307,
	"firstfolside":'a',
	# there is a duplication of 302 a so we add 5 to the expectation
	"lastfolnum": 341,
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

# because of previous duplication, we add ten to everything
batch_info_10 = {
	"srcdir":"/home/eroux/BUDA/Incoming/ffy/002/5/",
	"dstdir":"output/W0FFY002/images/W0FFY002-I0FFY002/",
	"leftlimit":337,
	"rightlimit":5010,
	"firstfolnum":347,
	"firstfolside":'a',
	"lastfolnum": 381,
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
	"firstfolnum":382,
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
			filenameprefix = ("%03d"%i)+side
			if filenameprefix in fixlist3:
				box = (bi["leftlimit"], holim[0]+175, bi["rightlimit"], holim[1])
			imres = im.crop(box)
			if "resizefactor" in bi and bi["resizefactor"] != 1:
				newdim = (int(imres.width*bi["resizefactor"]),int(imres.height*bi["resizefactor"]))
				imres = imres.resize(newdim, Image.ANTIALIAS)
			#print("saving ", outfn)
			if "outformat" not in bi or bi["outformat"] == 'JPEG':
				quality=75
				if "outquality" in bi:
					quality=int(100*bi["outquality"])
				outfn = bi["dstdir"]+filenameprefix+".jpg"
				imres.save(outfn, 'JPEG', quality=quality, optimize=True, progressive=True)
			elif bi["outformat"] == 'TIFF':
				outfn = bi["dstdir"]+filenameprefix+".tif"
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

# run_batch(batch_info_1)
# run_batch(batch_info_2)
# run_batch(batch_info_3)
# run_batch(batch_info_4)
# run_batch(batch_info_5)
# run_batch(batch_info_6)
# run_batch(batch_info_7)
# run_batch(batch_info_72)
# run_batch(batch_info_8)
# run_batch(batch_info_9)
# run_batch(batch_info_92)
# run_batch(batch_info_10)
# run_batch(batch_info_11)
# run_batch(batch_info_12)
# run_batch(batch_info_13)
# run_batch(batch_info_14)
# run_batch(batch_info_15)

normalize_dir("output/W0FFY001/images/W0FFY001-I0FFY001/", "I0FFY001")
normalize_dir("output/W0FFY002/images/W0FFY002-I0FFY002/", "I0FFY002")
# normalize_dir("output/W0FFY003/images/W0FFY003-I0FFY003/", "I0FFY003")
# normalize_dir("output/W0FFY004/images/W0FFY004-I0FFY004/", "I0FFY004")
#normalize_dir("output/W0FFY005/images/W0FFY005-I0FFY005/", "I0FFY005")
#normalize_dir("output/W0FFY006/images/W0FFY006-I0FFY006/", "I0FFY006")
#normalize_dir("output/W0FFY007/images/W0FFY007-I0FFY007/", "I0FFY007")