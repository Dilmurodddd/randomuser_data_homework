import get_data

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    
a=get_data.get_data("randomuser_data.json")
b=''


# for birinchi in a:
#     if birinchi=="username":
#         b+=birinchi+'\n'
#     for ikkinchi in a[birinchi]:
#         if ikkinchi=="username":
#             b+=ikkinchi+'\n'
#         for uchinchi in a[birinchi][ikkinchi]:
#             if uchinchi=="username":
#                 b+=uchinchi+'\n'
#             for tortinchi in a[birinchi][ikkinchi][uchinchi]:
#                 if tortinchi=="username":
#                     b+=tortinchi+'\n'
#                 for beshinchi in a[birinchi][ikkinchi][uchinchi][tortinchi]:
#                     if beshinchi=="username":
#                         b+=beshinchi+'\n'
# for birinchi in a:
#     if birinchi=="username":
#         b+=birinchi+'\n'
#     for ikkinchi in a[birinchi]:
#         if ikkinchi=="username":
#             b+=ikkinchi+'\n'
#         q=0
#         while q<len(ikkinchi):
#             for uchunchi in a[birinchi][ikkinchi][q]:
#                 if uchunchi=="username":
#                     b+=uchunchi+'\n'
            
#             q+=1
#             for tortinchi in a[birinchi][ikkinchi][q][uchunchi]:
#                 if tortinchi=="username":
#                     b+=tortinchi+'\n'
#                 for beshinchi in a[birinchi][ikkinchi][q][uchunchi][tortinchi]:
#                     if beshinchi=="username":
#                         b+=beshinchi+'\n'


# print(b)
b=''
d=''
for birinchi in a:
    if birinchi=="results":
        b=birinchi
c=len(a[b])
for ikkinchi in range(c):
    d+=a[b][ikkinchi]['login']['username']+'\n'

print(d)


































