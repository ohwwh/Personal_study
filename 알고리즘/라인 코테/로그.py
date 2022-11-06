def isvalid(str):
    l = 0
    if len(str) > 100:
        return (0)
    strlst = list(str.split())
    if len(strlst) != 12:
        return (0)
    if strlst[0] != 'team_name':
        return (0)
    if strlst[3] != 'application_name':
        return (0)
    if strlst[6] != 'error_level':
        return (0)
    if strlst[9] != 'message':
        return (0)
    l = l + len('team_name') + len('application_name') + len('error_level') + len('message')
    for i in range(4):
        if strlst[3 * i + 1] != ':':
            return (0)
    l += 4
    for i in range(4):
        if strlst[3 * i + 2].isalpha() == 0:
            return (0)
        l += len(strlst[3 * i + 2])
    if len(str) - l != 11:
        return (0)
    else:
        return (1)
            

def solution(logs):
    answer = 0
    for str in logs:
        if isvalid(str) == 0:
            answer += 1
    return answer

logs = ["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", " team_name : db application_name : dbtest error_level : info message : test", "team_name : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]
s = solution(logs)