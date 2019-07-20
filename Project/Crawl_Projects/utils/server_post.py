# -*- coding: utf-8 -*-
# @Time : 2019/7/15 9:50
# @Author : Quantum_Ran
# @Email : ai.ei.ui@live.cn
# @File : server_post.py
# @Software: PyCharm
def postData_to_dict(s):
    list1 = s.split('&')
    ret = {L.split('=')[0]: L.split('=')[1] for L in list1}
    return ret


def postCookies_to_dict(s):
    list1 = s.split(';')
    ret = {L.split('=')[0]: L.split('=')[1] for L in list1}
    return ret


# str1 = 'udid=1b6ae2bcf7ef5283&openudid=1b6ae2bcf7ef5283&device_model=OPPO%20R11&os=Android&os_version=5.1.1&resolution=1440000&device_brand=OPPO%20&offset=0'
# postData_to_dict(str1)

str1 = 'logged_in=no; _octo=GH1.1.406723403.1563410251; _ga=GA1.2.843926955.1563410254; has_recent_activity=1; _gat=1; tz=Asia%2FShanghai; _gh_sess=QzRiUHkrdHpIbnN6Z3JuZXY5RFlJaFYzeDNoWGpEMDRqV1pQMUxVeGM5WTBnVVZqQndjcUJxQVpqY0FPSkk0UDNZOXZXdWxQNEVVUW9waEplSXgyWW01bC94NHZ4NmxiditMb0xHcGFLQVArTlVNdThKT3RZb0wvZGoxcmhIMlo3K1ZXZjgxemt3UUV2eWZzdDRFOEVodWMydG9vR2lFTStWdjNpaU4rUkhlYTVtaUJlNjk4alZQRy9KclQwMkk4U0pNTmNCZXBBVkhZQ2NKOEhnOXI2cCtuRGhIcmJTclNYUlJGWk1aMFRFSWNHdVRnd25rMUIxQ2FBUDlGalJ6enZZR2NMaHFLQzdSK3JoUWtrMUN6M0JyYzUwODR1bE5SRkR5UzBVNEJvQ2NBWGliYkNBd2ROU0FaNHpNYjdRV0Z0SzFNQ3FvVCsrOFNxa3o1TE1nOGk5WURXRklYWlozaDVHSXNqOFYxMmZZSlU5bVo4cFh5Wmd0byt0Y2wyQjhvdnFlS0Z0cXVWN0djTVdiV1Nxd0F2OFZRRHBldzhMcUZEeWJmcjUydmY3dHV4cDBrazhYd1pYalBOcDhzaG01WTNXS3ZRSFh0dDdLbGgyZDdlOGVtSjA3UzltMlZiWEh2eVo1S3h0bnl4L009LS1yQWRyblptVzVlbjlpMHlZdkZoU3B3PT0%3D--746b0ecd1f9ce7eeb2c097124c48b128d80052eb'
# print(postCookies_to_dict(str1))
