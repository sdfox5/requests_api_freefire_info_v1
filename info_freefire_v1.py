import requests
print("welcom on the bot to search 🔍 for information to uid: \n")
uid = int(input("Enter the uid for player to search information: \n"))
regoin =  input('''Enter regoin for uid: 
sg : Middle East and North Africa server.

IND: India server.

BR: Brazil server.

US: United States server.

TH: Thailand server.

VN: Vietnam server.

EU: Europe server.

ID: Indonesia server. \n''')
url = f"https://api-info-rzx.vercel.app/info/{uid}/{regoin}"
r = requests.get(url)
if r.status_code == 200:
    try:
        
        data = r.json()
        print("-+-+-+-+-+-+INFORMATION ACCOUNT+-+-+-+-+-+")
        print(f"accountId: {data['basicInfo']['accountId']}")
        print(f"nickname: {data['basicInfo']['nickname']}")
        print(f"level: {data['basicInfo']['level']}")
        print(f"exp: {data['basicInfo']['exp']}")
        print(f"bannerId: {data['basicInfo']['bannerId']}")
        print(f"headPic: {data['basicInfo']['headPic']}")
        print(f"rank: {data['basicInfo']['rank']}")
        print(f"rankingPoints: {data['basicInfo']['rankingPoints']}")
        print(f"role: {data['basicInfo']['role']}")
        print(f"badgeCnt: {data['basicInfo']['badgeCnt']}")
        print(f"badgeId: {data['basicInfo']['badgeId']}")
        print(f"seasonId: {data['basicInfo']['seasonId']}")
        print(f"liked: {data['basicInfo']['liked']}")
        print(f"lastLoginAt: {data['basicInfo']['lastLoginAt']}")
        print(f"csRank: {data['basicInfo']['csRank']}")
        print(f"csRankingPoints: {data['basicInfo']['csRankingPoints']}")
        print(f"maxRank: {data['basicInfo']['maxRank']}")
        print(f"csMaxRank: {data['basicInfo']['csMaxRank']}")
        print(f"createAt: {data['basicInfo']['createAt']}")
        
        print("-+-+-+-+-+-+-+-+-PROFILE INFORMATION+-+-+-+-+-+-+-+-")
        print(f"avatarId: {data['profileInfo']['avatarId']}")
        print(f"skinColor: {data['profileInfo']['skinColor']}")
        print(f"clothes: {data['profileInfo']['clothes']}")
        print(f"isSelected: {data['profileInfo']['isSelected']}")
        print(f"pvePrimaryWeapon: {data['profileInfo']['pvePrimaryWeapon']}")
        print(f"endTime: {data['profileInfo']['endTime']}")
        
        print("-+-+-+-+-+-+-+-+-+-+-CLAN INFORMATION+-+-+-+-+-+-")
        print(f"clanId: {data['clanBasicInfo']['clanId']}")
        print(f"captainId: {data['clanBasicInfo']['captainId']}")
        print(f"clanLevel: {data['clanBasicInfo']['clanLevel']}")
        print(f"capacity: {data['clanBasicInfo']['capacity']}")
        print(f"memberNum: {data['clanBasicInfo']['memberNum']}")
        
        print("-+-+-++-+-+-+-+-+-CAPTAIN INFORMATION+-+-+-+-+-+-+-+-+")
        print(f"accountId: {data['captainBasicInfo']['accountId']}")
        print(f"nickname: {data['captainBasicInfo']['nickname']}")
        print(f"level: {data['captainBasicInfo']['level']}")
        print(f"exp: {data['captainBasicInfo']['exp']}")
        print(f"bannerId: {data['captainBasicInfo']['bannerId']}")
        print(f"headPic: {data['captainBasicInfo']['headPic']}")
        print(f"rank: {data['captainBasicInfo']['rank']}")
        print(f"rankingPoints: {data['captainBasicInfo']['rankingPoints']}")
        print(f"role: {data['captainBasicInfo']['role']}")
        print(f"badgeCnt: {data['captainBasicInfo']['badgeCnt']}")
        print(f"badgeId: {data['captainBasicInfo']['badgeId']}")
        print(f"seasonId: {data['captainBasicInfo']['seasonId']}")
        print(f"liked: {data['captainBasicInfo']['liked']}")
        print(f"lastLoginAt: {data['captainBasicInfo']['lastLoginAt']}")
        print(f"csRank: {data['captainBasicInfo']['csRank']}")
        print(f"csRankingPoints: {data['captainBasicInfo']['csRankingPoints']}")
        print(f"maxRank: {data['captainBasicInfo']['maxRank']}")
        print(f"csMaxRank: {data['captainBasicInfo']['csMaxRank']}")
        print(f"createAt: {data['captainBasicInfo']['createAt']}")
        
        print("-+-+-+-+-+-+-+-+-+-+-+SOCIAL INFORMATION+-+-+-+-+-+-+-")
        print(f"accountId: {data['socialInfo']['accountId']}")
        print(f"language: {data['socialInfo']['language']}")
        print(f"signature: {data['socialInfo']['signature']}")
        print(f"rankShow: {data['socialInfo']['rankShow']}")        
        print("-+-+-+-+-DEV-+-+-+-+-++-+")
    except ValueError as e:
        print(f"Error parsing Json response: {e}")    
else:
    print ("api is stop or error on uid!")   