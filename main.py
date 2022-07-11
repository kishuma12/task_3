# simvol_EU = 'ASDFGHJKLZXCVBNMPOIUYTREWQ'
# simvol_RU = 'ФЫВАПРОЛДЖЭЮБЬТИМСЧЯЙЦУКЕНГШЩЗХЪ'
# shagshifra = int(input('encryption step: '))
# message = input('message for encryption: ').upper()
# itog = ''
# language = input('choose a language RU/EU: ')
#
# if language == 'RU':
#
#
#     for i in message:
#         mest = simvol_RU.find(i)
#         new_mest = mest + shagshifra
#
#         if i in simvol_RU:
#            itog += simvol_RU[new_mest]
#
#         else:
#             itog += i
# else:
#     for i in message:
#         mest = simvol_EU.find(i)
#         new_mest = mest + shagshifra
#
#         if i in simvol_EU:
#             itog += simvol_EU[new_mest]
#         else:
#             itog += i
#
#
#
# print(itog)
















 # msg = input('')
 # LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
 #
 # for k in range(len(LETTERS)):
 #     transformation = ''
 #     for s in msg:
 #         if s in LETTERS:
 #             n = LETTERS.find(s)
 #             n = n - k
 #             if n < 0:
 #                 n = n + len(LETTERS)
 #             transformation = transformation + LETTERS[n]
 #
 #         else:
 #             transformation = transformation + s
 # print('Hacking k #%s: %s' % (k, transformation))