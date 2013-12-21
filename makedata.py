# -*- coding: utf-8 -*-
import csv;

# 入力ファイル
ifn = open("010010-99999-1934")
reader = csv.reader(ifn)

# 出力ファイル
ofn = open("010010-99999-1934.csv", "w")
writer = csv.writer(ofn)

# 各レコードに対して項目を抽出しファイルに出力する
writer.writerow(["usaf_id","wban_id","year","month","day","hour","minute","latitude","longitude","height","calllet","qcpname","winddir","winddir_qcode","winddir_tcode","windspeed","windspeed_qcode","lcloud","lcloud_dcode","lcloud_ccode","visdist","visdist_qcode","visdist_vcode","visdist_qvcode","temp","temp_qcode","dptemp","dptemp_qcode","pressure","pressure_qcode"])
for row in reader:
	for elem in row:
		usaf_id = elem[4:10] # USAF気象情報ステーション識別子
		wban_id = elem[11:16]	# WBAN気象情報ステーション識別子
		year = elem[15:19] # 観測年
		month = elem[19:21]	# 観測月
		day = elem[21:23]	# 観測日
		hour = elem[23:25] # 観測時間
		minute = elem[25:27] # 観測分
		latitude = long(elem[28:34])/1000 # 緯度
		longitude = long(elem[35:41])/1000	# 経度
		height = elem[46:51] # 標高
		calllet = elem[51:56] # 呼出符号識別子
		qcpname = elem[56:60] # 品質プロセス名
		winddir = elem[60:63] # 風向き
		winddir_qcode = elem[63:64] # 風向きの品質コード
		winddir_tcode = elem[64:65] # 風向きのタイプコード
		windspeed = elem[65:70] # 風速
		windspeed_qcode = elem[70:71] # 風速の品質コード
		lcloud = elem[71:76] # 雲低高度
		lcloud_qcode = elem[76:77] # 雲低高度の品質コード
		lcloud_dcode = elem[77:78] # 雲低高度の決定コード
		lcloud_ccode = elem[78:79] # 雲低高度のCAVOKコード
		visdist = elem[79:84] # 視界
		visdist_qcode = elem[84:85] # 視界の品質コード
		visdist_vcode = elem[85:86] # 視界の変数コード
		visdist_qvcode = elem[86:87] # 視界の品質変数コード
		temp = long(elem[87:92])/10 # 気温
		temp_qcode = elem[92:93] # 気温の品質コード
		dptemp = long(elem[93:98])/10 # 露点気温
		dptemp_qcode = elem[98:99] # 露点気温の品質コード
		pressure = long(elem[99:104])/10 # 気圧
		pressure_qcode = elem[104:105] # 気圧の品質コード
		writer.writerow([usaf_id,wban_id,year,month,day,hour,minute,latitude,longitude,height,calllet,qcpname,winddir,winddir_qcode,winddir_tcode,windspeed,windspeed_qcode,lcloud,lcloud_dcode,lcloud_ccode,visdist,visdist_qcode,visdist_vcode,visdist_qvcode,temp,temp_qcode,dptemp,dptemp_qcode,pressure,pressure_qcode])

ifn.close()
ofn.close()
