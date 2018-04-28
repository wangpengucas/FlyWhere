#!/usr/bin/python3.4
# -*- coding:utf-8 -*-
# to do list:
#1.多线程抓取信息（如何防止被禁，如何类似分流抢票分流抓取）
import urllib.request
import json
import random
import time
import datetime
import operator
from lxml import etree

Airport_dict = {'JIQ': ['黔江', '黔江武陵山机场', '重庆市'], 'GOQ': ['格尔木', '格尔木机场', '青海省'], 'LJG': ['丽江', '丽江三义机场', '云南省'], 'HFE': ['合肥', '合肥新桥国际机场', '安徽省'], 'FUG': ['阜阳', '阜阳西关机场', '安徽省'], 'LCX': ['龙岩', '连城冠豸山机场', '福建省'], 'ZQZ': ['张家口', '张家口宁远机场', '河北省'], 'IQN': ['庆阳', '庆阳机场', '甘肃省'], 'XNT': ['邢台', '邢台褡裢机场', '河北省'], 'SHP': ['秦皇岛', '秦皇岛山海关机场', '河北省'], 'JXA': ['鸡西', '鸡西兴凯湖机场', '黑龙江省'], 'AKA': ['安康', '安康五里铺机场', '陕西省'], 'XFN': ['襄阳', '襄阳刘集机场', '湖北省'], 'KHH': ['高雄', '高雄国际机场', '台湾省'], 'OHE': ['漠河', '漠河古莲机场', '黑龙江省'], 'GYS': ['广元', '广元盘龙机场', '四川省'], 'YNZ': ['盐城', '盐城南洋机场', '江苏省'], 'LUM': ['德宏', '德宏芒市机场', '云南省'], 'JIC': ['金昌', '金昌金川机场', '甘肃省'], 'KJH': ['黔东南', '凯里黄平机场', '贵州省'], 'HUZ': ['惠州', '惠州平潭机场', '广东省'], 'YIC': ['宜春', '宜春明月山机场', '江西省'], 'DGM': ['东莞', '东莞机场', '广东省'], 'XUZ': ['徐州', '徐州观音机场', '江苏省'], 'FOC': ['福州', '福州长乐国际机场', '福建省'], 'FUO': ['佛山', '佛山沙堤机场', '广东省'], 'CGQ': ['长春', '长春龙嘉国际机场', '吉林省'], 'TYN': ['太原', '太原武宿国际机场', '山西省'], 'YIH': ['宜昌', '宜昌三峡机场', '湖北省'], 'KJI': ['布尔津', '布尔津喀纳斯机场', '新疆维吾尔自治区'], 'CSX': ['长沙', '长沙黄花国际机场', '湖南省'], 'WNH': ['文山', '文山普者黑机场', '云南省'], 'TEN': ['铜仁', '铜仁凤凰机场', '贵州省'], 'SHE': ['沈阳', '沈阳桃仙国际机场', '辽宁省'], 'YZY': ['张掖', '张掖甘州机场', '甘肃省'], 'HZG': ['汉中', '汉中西关机场', '陕西省'], 'DNH': ['敦煌', '敦煌机场', '甘肃省'], 'SYX': ['三亚', '三亚凤凰国际机场', '海南省'], 'XMN': ['厦门', '厦门高崎国际机场', '福建省'], 'ERL': ['二连浩特', '二连浩特赛乌苏机场', '内蒙古自治区'], 'BSD': ['隆阳', '保山云瑞机场', '云南省'], 'KOW': ['赣州', '赣州黄金机场', '江西省'], 'THQ': ['天水', '天水麦积山机场', '甘肃省'], 'CKG': ['重庆', '重庆江北国际机场', '重庆市'], 'TNA': ['济南', '济南遥墙国际机场', '山东省'], 'BJS': ['北京', '北京首都国际机场', '北京'], 'NAO': ['南充', '南充高坪机场', '四川省'], 'TNH': ['通化', '通化三源浦机场', '吉林省'], 'DAX': ['达州', '达州河市机场', '四川省'], 'HDG': ['邯郸', '邯郸机场', '河北省'], 'LYA': ['洛阳', '洛阳北郊机场', '河南省'], 'HSN': ['舟山', '舟山普陀山机场', '浙江省'], 'CNI': ['长海', '长海大长山岛机场', '辽宁省'], 'BPL': ['博尔塔拉', '博乐阿拉山口机场', '新疆维吾尔自治区'], 'NZH': ['满洲里', '满洲里西郊机场', '内蒙古自治区'], 'RHT': ['阿拉善右旗', '阿拉善右旗巴丹吉林机场', '内蒙古自治区'], 'NNY': ['南阳', '南阳姜营机场', '河南省'], 'HEK': ['黑河', '黑河机场', '黑龙江省'], 'PVG': ['上海', '上海浦东国际机场', '上海市'], 'WUZ': ['梧州', '梧州长洲岛机场', '广西壮族自治区'], 'LYI': ['临沂', '临沂沭埠岭机场', '山东省'], 'EJN': ['额济纳旗', '额济纳旗桃来机场', '内蒙古自治区'], 'NGQ': ['阿里', '阿里昆莎机场', '西藏自治区'], 'TGO': ['通辽', '通辽机场', '内蒙古自治区'], 'TVS': ['唐山', '唐山三女河机场', '河北省'], 'YBP': ['宜宾', '宜宾菜坝机场', '四川省'], 'KMG': ['昆明', '昆明长水国际机场', '云南省'], 'DAT': ['大同', '大同云冈机场', '山西省'], 'TCG': ['塔城', '塔城机场', '新疆维吾尔自治区'], 'LLV': ['吕梁', '吕梁机场', '山西省'], 'CIF': ['赤峰', '赤峰玉龙机场', '内蒙古自治区'], 'CTU': ['成都', '成都双流国际机场', '四川省'], 'YIN': ['伊宁', '伊宁机场', '新疆维吾尔自治区'], 'ZHA': ['湛江', '湛江机场', '广东省'], 'KHN': ['南昌', '南昌昌北国际机场', '江西省'], 'LDS': ['伊春', '伊春林都机场', '黑龙江省'], 'HYN': ['台州', '台州路桥机场', '浙江省'], 'HMI': ['哈密', '哈密机场', '新疆维吾尔自治区'], 'TCZ': ['腾冲', '腾冲驼峰机场', '云南省'], 'DSN': ['鄂尔多斯', '鄂尔多斯伊金霍洛机场', '内蒙古自治区'], 'WUS': ['南平', '武夷山机场', '福建省'], 'BAV': ['包头', '包头二里半机场', '内蒙古自治区'], 'JNZ': ['锦州', '锦州小岭子机场', '辽宁省'], 'NBS': ['白山', '长白山机场', '吉林省'], 'JGD': ['大兴安岭', '加格达奇机场', '黑龙江省'], 'KCA': ['库车', '库车龟兹机场', '新疆维吾尔自治区'], 'HZH': ['黎平', '黎平机场', '贵州省'], 'NTG': ['南通', '南通兴东机场', '江苏省'], 'KRL': ['库尔勒', '库尔勒机场', '新疆维吾尔自治区'], 'DDG': ['丹东', '丹东浪头机场', '辽宁省'], 'AEB': ['百色', '百色巴马机场', '广西壮族自治区'], 'BHY': ['北海', '北海福成机场', '广西壮族自治区'], 'JGN': ['嘉峪关', '嘉峪关机场', '甘肃省'], 'SWA': ['揭阳', '揭阳潮汕机场', '广东省'], 'WUX': ['无锡', '苏南硕放国际机场', '江苏省'], 'NLT': ['新源', '新源那拉提机场', '新疆维吾尔自治区'], 'JHG': ['西双版纳', '西双版纳嘎洒国际机场', '云南省'], 'DCY': ['稻城', '稻城亚丁机场', '四川省'], 'HLD': ['呼伦贝尔', '呼伦贝尔海拉尔机场', '内蒙古自治区'], 'SHA': ['上海', '上海虹桥国际机场', '上海市'], 'DYG': ['张家界', '张家界荷花国际机场', '湖南省'], 'JGS': ['吉安', '井冈山机场', '江西省'], 'TXN': ['黄山', '黄山屯溪机场', '安徽省'], 'AAT': ['阿勒泰', '阿勒泰机场', '新疆维吾尔自治区'], 'WEH': ['威海', '威海国际机场', '山东省'], 'YNJ': ['延边', '延吉朝阳川机场', '吉林省'], 'HRB': ['哈尔滨', '哈尔滨太平国际机场', '黑龙江省'], 'YCU': ['运城', '运城机场', '山西省'], 'AVA': ['安顺', '安顺黄果树机场', '贵州省'], 'LHW': ['兰州', '兰州中川机场', '甘肃省'], 'KWE': ['贵阳', '贵阳龙洞堡国际机场', '贵州省'], 'MIG': ['绵阳', '绵阳南郊机场', '四川省'], 'HET': ['呼和浩特', '呼和浩特白塔国际机场', '内蒙古自治区'], 'CGO': ['郑州', '郑州新郑国际机场', '河南省'], 'XNN': ['西宁', '西宁曹家堡机场', '青海省'], 'CAN': ['广州', '广州白云国际机场', '广东省'], 'YUS': ['玉树', '玉树巴塘机场', '青海省'], 'KGT': ['康定', '甘孜康定机场', '四川省'], 'ENH': ['恩施', '恩施许家坪机场', '湖北省'], 'XIL': ['锡林浩特', '锡林浩特机场', '内蒙古自治区'], 'ACX': ['黔西南', '兴义机场', '贵州省'], 'CHG': ['朝阳', '朝阳机场', '辽宁省'], 'NNG': ['南宁', '南宁吴圩国际机场', '广西壮族自治区'], 'XIY': ['西安', '西安咸阳国际机场', '陕西省'], 'RLK': ['巴彦淖尔', '巴彦淖尔天吉泰机场', '内蒙古自治区'], 'WEF': ['潍坊', '潍坊机场', '山东省'], 'PZI': ['攀枝花', '攀枝花保安营机场', '四川省'], 'DIG': ['迪庆', '迪庆香格里拉机场', '云南省'], 'CZX': ['常州', '常州奔牛机场', '江苏省'], 'BPX': ['昌都', '昌都邦达机场', '西藏自治区'], 'ENY': ['延安', '延安二十里堡机场', '陕西省'], 'ZUH': ['珠海', '珠海金湾机场', '广东省'], 'HGH': ['杭州', '杭州萧山国际机场', '浙江省'], 'HKG': ['香港', '香港国际机场', '香港特别行政区'], 'JUZ': ['衢州', '衢州机场', '浙江省'], 'JZH': ['九寨沟', '九寨黄龙机场', '四川省'], 'JNG': ['济宁', '济宁曲阜机场', '山东省'], 'CIH': ['长治', '长治王村机场', '山西省'], 'TSN': ['天津', '天津滨海国际机场', '天津市'], 'AXF': ['阿拉善左旗', '阿拉善左旗巴彦浩特机场', '内蒙古自治区'], 'LLF': ['永州', '永州零陵机场', '湖南省'], 'LYG': ['连云港', '连云港白塔埠机场', '江苏省'], 'HLH': ['乌兰浩特', '乌兰浩特机场', '内蒙古自治区'], 'CGD': ['常德', '常德桃花源机场', '湖南省'], 'YTY': ['扬州', '扬州泰州机场', '江苏省'], 'MFM': ['澳门', '澳门国际机场', '澳门特别行政区'], 'ZHY': ['中卫', '中卫沙坡头机场', '宁夏回族自治区'], 'SUN': ['遂宁', '遂宁机场', '四川省'], 'BFJ': ['毕节', '毕节飞雄机场', '贵州省'], 'TAO': ['青岛', '青岛流亭国际机场', '山东省'], 'TSA': ['台北', '台北松山机场', '台湾省'], 'MXZ': ['梅州', '梅县长岗岌机场', '广东省'], 'WUA': ['乌海', '乌海机场', '内蒙古自治区'], 'YNT': ['烟台', '烟台莱山国际机场', '山东省'], 'LZO': ['泸州', '泸州蓝田机场', '四川省'], 'WUH': ['武汉', '武汉天河国际机场', '湖北省'], 'NGB': ['宁波', '宁波栎社国际机场', '浙江省'], 'TPE': ['桃园', '桃园国际机场', '台湾省'], 'YIW': ['金华', '义乌机场', '浙江省'], 'JJN': ['泉州', '泉州晋江机场', '福建省'], 'SJW': ['石家庄', '石家庄正定国际机场', '河北省'], 'ZAT': ['昭通', '昭通机场', '云南省'], 'HAK': ['海口', '海口美兰国际机场', '海南省'], 'HIA': ['淮安', '淮安涟水机场', '江苏省'], 'URC': ['乌鲁木齐', '乌鲁木齐地窝堡国际机场', '新疆维吾尔自治区'], 'DQA': ['大庆', '大庆萨尔图机场', '黑龙江省'], 'UYN': ['榆林', '榆林榆阳机场', '陕西省'], 'LZH': ['柳州', '柳州白莲机场', '广西壮族自治区'], 'LNJ': ['临沧', '临沧机场', '云南省'], 'LLB': ['黔南', '荔波机场', '贵州省'], 'JDZ': ['景德镇', '景德镇罗家机场', '江西省'], 'AKU': ['阿克苏', '阿克苏机场', '新疆维吾尔自治区'], 'FYN': ['富蕴', '富蕴机场', '新疆维吾尔自治区'], 'TLQ': ['吐鲁番', '吐鲁番交河机场', '新疆维吾尔自治区'], 'JMU': ['佳木斯', '佳木斯东郊机场', '黑龙江省'], 'WNZ': ['温州', '温州龙湾国际机场', '浙江省'], 'GYU': ['固原', '固原六盘山机场', '宁夏回族自治区'], 'KHG': ['喀什', '喀什机场', '新疆维吾尔自治区'], 'NDG': ['齐齐哈尔', '齐齐哈尔三家子机场', '黑龙江省'], 'DLC': ['大连', '大连周水子国际机场', '辽宁省'], 'INC': ['银川', '银川河东国际机场', '宁夏回族自治区'], 'MDG': ['牡丹江', '牡丹江海浪机场', '黑龙江省'], 'HSC': ['韶关', '韶关桂头机场', '广东省'], 'IQM': ['且末', '且末机场', '新疆维吾尔自治区'], 'NKG': ['南京', '南京禄口国际机场', '江苏省'], 'WXN': ['万州', '万州五桥机场', '重庆市'], 'LZY': ['林芝', '林芝米林机场', '西藏自治区'], 'KWL': ['桂林', '桂林两江国际机场', '广西壮族自治区'], 'SZX': ['深圳', '深圳宝安国际机场', '广东省'], 'LXA': ['拉萨', '拉萨贡嘎机场', '西藏自治区'], 'HTN': ['和田', '和田机场', '新疆维吾尔自治区'], 'DLU': ['大理', '大理机场', '云南省'], 'RKZ': ['日喀则', '日喀则和平机场', '西藏自治区'], 'AOG': ['鞍山', '鞍山腾鳌机场', '辽宁省'], 'JIU': ['九江', '九江庐山机场', '江西省'], 'KRY': ['克拉玛依', '克拉玛依机场', '新疆维吾尔自治区'], 'SYM': ['普洱', '普洱思茅机场', '云南省'], 'JUH': ['池州', '池州九华山机场', '安徽省'], 'AQG': ['安庆', '安庆天柱山机场', '安徽省'], 'DOY': ['东营', '东营胜利机场', '山东省'], 'XIC': ['西昌', '西昌青山机场', '四川省'], 'YIE': ['阿尔山', '阿尔山伊尔施机场', '内蒙古自治区'], 'ZYI': ['遵义', '遵义新舟机场', '贵州省'], 'HJJ': ['怀化', '怀化芷江机场', '湖南省'], 'GXH': ['甘南', '甘南夏河机场', '甘肃省']}
Error_Code_Dict = {"101": "有直飞", "102": "无直飞!请去携程查看时间是否合适^_^", "103": "不通航!选择其他目的地^_^", "104": "json数据有误！请联系作者"}

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False
    def __iter__(self):
        #Return the match method once, then stop
        yield self.match
        raise StopIteration
    def match(self, *args):
        #Indicate whether or not to enter a case suite
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

def function_101(jsonData, R_DCity1):
    Airplane_info_dict = {}
    for json in jsonData["fis"]:
        Airplane_info_list = []
        Airplane_dcity1 = json["dcn"]
        if Airplane_dcity1 != Airport_dict[R_DCity1][0]:
            print(Airport_dict[R_DCity1][0])
            continue
        Airplane_num = json["fn"]
        Airplane_price = json["lp"]
        Airplane_acity1 = json["acn"]
        Airplane_dt = json["dt"]
        Airplane_at = json["at"]
        # scs = json['scs'][1]['fdp']
        # print(scs)
        Airplane_info_list.append(Airplane_price)
        Airplane_info_list.append(Airplane_dcity1)
        Airplane_info_list.append(Airplane_dt)
        Airplane_info_list.append(Airplane_acity1)
        Airplane_info_list.append(Airplane_at)
        Airplane_info_dict[Airplane_num] = Airplane_info_list
    # 估计用这个工具的也没人买20000的机票,哈哈
    air_price = 20000
    low_price_num = ""
    if Airplane_info_dict == {}:
        return {}
    for air_num in Airplane_info_dict:
        # print(Airplane_info_dict[air_num], end='')
        if Airplane_info_dict[air_num][0] < air_price:
            air_price = Airplane_info_dict[air_num][0]
            low_price_num = air_num
    result = []
    result.append(Airplane_info_dict[low_price_num][0])
    result.append(low_price_num)
    result.append(Airplane_info_dict[low_price_num][1:])
    return result


def get_url(R_DCity1, R_ACity1, R_DDate1):
    '''获取重要的参数
    date:日期，格式示例：2016-05-13
    '''
    # url='http://flights.ctrip.com/booking/hrb-sha-day-1.html?ddate1=%s'%R_DDate1
    DCity1 = "DCity1=" + R_DCity1
    ACity1 = "&ACity1=" + R_ACity1
    DDate1 = "&SearchType=S&DDate1=" + R_DDate1
    url = 'http://flights.ctrip.com/booking/' + R_DCity1.lower() +'-' + R_ACity1.lower() + '-day-1.html?ddate1=%s' % R_DDate1
    res = urllib.request.urlopen(url).read()
    tree = etree.HTML(res)
    pp = tree.xpath('''//body/script[1]/text()''')[0].split()
    parameter_list = pp[3].split("&")
    LogToken = parameter_list[-2][9:]
    r = pp[-1][27:len(pp[-1]) - 3]
    CK_original = parameter_list[-1][3:35]

    character_5 = CK_original[5]
    CK = CK_original[0:4]+CK_original[6:14]+character_5+CK_original[15:]
    rk = pp[-1][18:24]
    num = random.random()*10
    num_str = "%.15f"%num
    rk = num_str+rk

    URL = 'http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?' + DCity1 + ACity1 + DDate1 + "&IsNearAirportRecommond=0"+"&LogToken="+LogToken+"&rk="+ rk +"&CK="+CK+"&r="+r

    return URL


def get_jsonData(R_DCity1,R_ACity1,R_DDate1):

    # R_DCity1 = input("请输入出发城市：")
    # R_ACity1 = input("请输入到达城市：")
    #R_DDate1 = input("请输入出发时间,例 2018-04-05：")
    URL=get_url(R_DCity1, R_ACity1, R_DDate1)
    # URL = 'http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?' + DCity1 + ACity1 + DDate1 + "&IsNearAirportRecommond=0&LogToken=de3918259c91445aa9eb58650ed06c33&rk=9.496725553444126154954&CK=EAD9495B23756516CBFF2A95830F8153&r=0.581329311067284837881120"
    Referer = "http://flights.ctrip.com/booking/" + R_DCity1.lower() + "-" + R_ACity1.lower() + "-day-1.html?ddate1=" + R_DDate1
    # print(URL)
    # print(Referer)
    # url = 'http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=WUX&ACity1=SYX&SearchType=S&DDate1=2018-04-05&IsNearAirportRecommond=0&LogToken=6fe396dd9cea4087b18334c4a9bddb26&rk=4.912464433994882105209&CK=DAD9DFFCBC918E84872E8D0E0E4019BB&r=0.58130895120885566075113'
    headers = {
        "Host": "flights.ctrip.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
        # "Referer": "http://flights.ctrip.com/booking/wux-syx-day-1.html?ddate1=2018-04-05",
        "Referer": Referer,
        "Connection": "keep-alive",
    }

    res = urllib.request.Request(URL, headers=headers)
    res = urllib.request.urlopen(res).read().decode("gb2312", errors='ignore')
    jsonData = json.loads(res)
    Error_Info = jsonData["Error"]
    if Error_Info is None:
        Error_Code = 101
    else:
        Error_Code = Error_Info["Code"]
    return jsonData, Error_Code, R_DCity1

def get_low_price(R_DCity1,R_ACity1,R_DDate1):
    jsonData, Error_Code, DCity = get_jsonData(R_DCity1, R_ACity1, R_DDate1)
    # print(Error_Code)
    for case in switch(Error_Code):
        if case(101):
            Airplane_info_dict = function_101(jsonData, DCity)
            if Airplane_info_dict == []:
                print("返回值为空！可能是查询条件有误，未取得数据。")
                return []
            return Airplane_info_dict
        if case(102):
            # 102暂时没发现，可能是携程已改版
            print(Error_Code_Dict["102"])
            return []
        if case(103):
            # 此处不能直接提示不通航，应该检查是否有中转航班
            print(Error_Code_Dict["103"])
            return []
        if case(104):
            print(Error_Code_Dict["104"])
            return []
        if case():  # default, could also just omit condition or 'if True'
            print('输入有误！')
            return []
    return []



def Info_Menu():
    print('''
****************************************************************************
    欢迎使用FlyWhere！突然想去浪，钱包又太瘪？FlyWhere告诉你哪便宜飞哪！
    Version:1.0  
    Authon:king
    使用说明：
    ① 爬取数据来源于携程,暂时只支持查询直飞,请根据结果去携程订票
    ② 基于python3开发,请确定运行环境为python3.X版本
    ③ 因字符编码问题,此工具暂时只可在linux下运行
****************************************************************************
    请选择(1/2/q)：
    1.选定出发地和目的地。根据出发时间范围，筛选出机票最便宜的五个日期。
    2.选定出发地和出发日期。根据目的地列表，筛选出机票最便宜的五个目的地。
    q/Q)退出。
    ''')

def Date1_check(DDate1):
    DDate1 = str(DDate1)
    if DDate1.strip()=='':
        return False
    if len(DDate1) != 8:
        print("请输入8位日期(yyyymmdd)！")
        return False
        # return [False, "请输入8位日期(yyyymmdd)！"]
    try:
        time.strptime(DDate1, "%Y%m%d")
    except:
        print("日期不合法！")
        return False
        # return [False, "日期不合法！"]
    Current_time = time.strftime("%Y%m%d")
    now_time = datetime.datetime.strptime(Current_time, "%Y%m%d")
    DDate_time = datetime.datetime.strptime(DDate1, "%Y%m%d")
    if operator.eq(now_time, DDate_time):
        return True
    timedelta = int(str(DDate_time - now_time).split()[0])
    if timedelta < 0:
        print("不能早于当前日期！")
        return False
        # return [False, "不能早于当前日期！"]
    if timedelta > 365:
        print("查询时间请不要超过一年！")
        return False
        # return [False, "查询时间请不要超过一年！"]
    return True


def Date2_check(DDate1,DDate2):
    DDate2 = str(DDate2)
    if DDate2.strip()=='':
        return False
    if len(DDate2) != 8:
        print("请输入8位日期(yyyymmdd)！")
        return False
        # return [False, "请输入8位日期(yyyymmdd)！"]
    try:
        time.strptime(DDate2, "%Y%m%d")
    except:
        print("日期不合法！")
        return False
        # return [False, "日期不合法！"]
    Current_time = time.strftime("%Y%m%d")
    now_time = datetime.datetime.strptime(Current_time, "%Y%m%d")
    DDate1_time = datetime.datetime.strptime(DDate1, "%Y%m%d")
    DDate2_time = datetime.datetime.strptime(DDate2, "%Y%m%d")
    if operator.eq(DDate1_time, DDate2_time):
        return True
    timedelta_now = int(str(DDate2_time - now_time).split()[0])
    timedelta = int(str(DDate2_time - DDate1_time).split()[0])
    if timedelta < 0:
        print("不能早于当前日期！")
        return False
        # return [False, "不能早于当前日期！"]
    if timedelta_now > 365:
        print("查询时间请不要超过一年！")
        return False
        # return [False, "查询时间请不要超过一年！"]
    return True

def getEveryDay(begin_date,end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list


def Get_Lowest_date():
    DCity=""
    ACity=""
    DDate1=""
    DDate2=""

    print("机场列表:")
    num = 0
    for key in Airport_dict:
        print(str(num)+"."+key + ":" + Airport_dict[key][0] + " " + Airport_dict[key][1] + " " + Airport_dict[key][2])
        num = num + 1
    while DCity not in Airport_dict.keys():
        DCity = input("请输入出发地机场简称：").upper()
        if DCity not in Airport_dict.keys():
            print("输入出发地机场代码有误！请检查！")

    while ACity not in Airport_dict.keys() or operator.eq(DCity,ACity):
        ACity = input("请输入目的地机场简称：").upper()
        if DCity not in Airport_dict.keys():
            print("输入目的地机场代码有误！请检查！")
        if operator.eq(DCity,ACity):
            print("出发地与目的地相同！请重新输入！")

    while not Date1_check(DDate1):
        DDate1 = input("请输入起始时间,格式 yyyymmdd(直接回车表示从今天开始查询)：")
        if DDate1.strip()=="":
            DDate1=time.strftime("%Y%m%d")
            break

    while not Date2_check(DDate1, DDate2):
        DDate2 = input("请输入结束时间,格式 yyyymmdd(直接回车表示跟起始时间相同)：")
        if DDate2.strip()=="":
            DDate2=DDate1
            break

    DDate1 = DDate1[0:4] + "-" + DDate1[4:6] + "-" + DDate1[6:]
    DDate2 = DDate2[0:4] + "-" + DDate2[4:6] + "-" + DDate2[6:]
    date_range = getEveryDay(DDate1, DDate2)
    top_lowest_date = [[]]
    for ddate in date_range:
        top_lowest_date.append(get_low_price(DCity, ACity, ddate))
    if top_lowest_date==[]:
        return -1
    elif top_lowest_date[0]==[]:
        return -1
    top_lowest_date = sorted(top_lowest_date, key=lambda x: int(x[0]))
    count = 0
    for lowest_date in top_lowest_date:
        if count < 5:
            print(lowest_date)
            count = count + 1
        else:
            break
    return 0

def Get_Lowest_city():
    print("机场列表:")
    num = 0
    for key in Airport_dict:
        print(str(num)+"."+key + ":" + Airport_dict[key][0] + " " + Airport_dict[key][1] + " " + Airport_dict[key][2])
        num = num + 1


if __name__=="__main__":
    q_flag = 0
    while(1):
        cmd = 0
        if cmd == 'q' or cmd == 'Q' or q_flag==1:
            break
        Info_Menu()
        cmd = input()
        if cmd == 'q' or cmd == 'Q' or q_flag==1:
            break
        while (cmd != '1' and cmd != '2'):
            print("input("+cmd+"):"+"输入错误，请重新输入，或者Ctrl+z退出")
            Info_Menu()
            cmd = input()
            if cmd == 'q' or cmd == 'Q':
                q_flag = 1
                break
        for case in switch(cmd):
            if case("1"):
                Get_Lowest_date()
                cmd = input("按任意键回车返回主菜单,q/Q退出")
                if cmd == 'q' or cmd == 'Q':
                    q_flag = 1
                    break
                else:
                    break
            if case("2"):
                Get_Lowest_city()
                break
            if case():
                break

