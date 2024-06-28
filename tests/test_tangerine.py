from tangerine import InteractiveSecretProvider, TangerineClient

secret_provider = InteractiveSecretProvider()
client = TangerineClient(secret_provider)

with client.login():
    accounts = client.list_accounts()

#with client.login():
#