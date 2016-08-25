import requests, json

class SlackAPI():
	def __init__(self, token):
		self.TOKEN = token
		self.domain = 'https://slack.com/api/'

	def has_error(self, response_dict, log="An error ocurred:"):
		if response_dict['ok']:
			return False
		else:
			print(log)
			print(response_dict['error'])
			return True
	
	def api_method(self, method, extra_params={}):
		"""executes any method and returns a dictionary"""
		params = {'token': self.TOKEN}
		params.update(extra_params)
		response_dict = json.loads(requests.get(
                                        self.domain + 'channels.list',
                                        params=params
                                ).text)
		return response_dict

	def get_channel_list(self):
		"""returns updated channel list"""
		response_dict = self.api_method('channels.list')
		if not self.has_error(response_dict, log='Error getting channel list:'):
			self.channel_list = response_dict["channels"]
			return self.channel_list
		else:			
			return None

	def get_channel_name(self, channel_id):
		"""returns the channel name when given an id"""
		self.channel_list = self.get_channel_list()
		for channel in self.channel_list:
			if channel["id"] == channel_id:
				return channel["name"]

	def get_channel_id(self, channel_name):
		"""returns the channel id when given a name"""
		self.channel_list = self.get_channel_list()
		for channel in self.channel_list:
			if channel["name"] == channel_name:
				return channel["id"]

