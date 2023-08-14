# from outline_vpn.outline_vpn import OutlineVPN
#
#
#
# client = OutlineVPN(api_url="https://89.191.228.149:19361/pC4f3hrpzlZGs6FewsKEAw",
#                     cert_sha256="5C462B3CA1DCA4BC67BA596F085755AF2C257F891FB5E76591F58DF3F93B0CC9")
#
# # новый ключ
# new_key = client.create_key()
#
# # перебор ключей
# for key in client.get_keys():
#     print(key)
#
# # задать имя ключу
# client.rename_key(new_key.key_id, "new_key")
#
# # Удалить ключ
# # client.delete_key(new_key.key_id)

from yoomoney import Client
token = "4100118274246347.6F7E4954B8AA50CBF8D237C8376750CE703656A9442B680152B0DF8DE8815B81C72037EE023C6079ADAD272E49447A8C9C93B1889727BE00D67539507B18847B7083EBE0F4806782519D183A611BFE9BEC2C60C994A2B2502E62F55DDFA2E28E031E72F0C3402F0CC64D808696496553B2925DE671DDE3A080FEEC2DF85D1645"
client = Client(token)
user = client.account_info()
print("Account number:", user.account)
print("Account balance:", user.balance)
print("Account currency code in ISO 4217 format:", user.currency)
print("Account status:", user.account_status)
print("Account type:", user.account_type)
print("Extended balance information:")
for pair in vars(user.balance_details):
    print("\t-->", pair, ":", vars(user.balance_details).get(pair))
print("Information about linked bank cards:")
cards = user.cards_linked
if len(cards) != 0:
    for card in cards:
        print(card.pan_fragment, " - ", card.type)
else:
    print("No card is linked to the account")