from twilio.rest import TwilioRestClient

account_sid = "AC5cee1632d29552cb2efcbfd906614d55" # Your Account SID from www.twilio.com/console
auth_token  = "6beeec3c351f6e0e6bfbdec791f5617a"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Crush your enemies, see them driven before you, and hear the lamentation of their women!",
    to="+917-306-0541",    # Replace with your phone number
    from_="+13476258127") # Replace with your Twilio number

print(message.sid)
