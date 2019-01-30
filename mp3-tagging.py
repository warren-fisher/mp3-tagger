from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
from os import listdir
from os.path import isfile, join
from unittest import TestCase 

class _mp3(MP3File): 
	
	def __init__(self, path, name): 
		self.path = path 
		self.name = name  
		
	def parse_name(self): 
	
	def tag(self):
		""" 
		Take a MP3 file object and a dictionary and set all MP3 tags. 
		"""
		for key, value in self.tags.items():
			self.key = value 	
		mp3.save() 
	
	def 
	
class _album(): 
	
	def __init__(self): 

class _artist(): 
	
	def __init__(self): 
	
class mp3_testing(TestCase):
	
	def setUp(self): 
		self.mp3 = _mp3() 
	
	def test_int(self):
		"""
		Set any ids that are comprised of numbers only to None. 
		"""
		ids = {} 
		for id_key, id_value in id_dict.items():
			try: 
				int(id_value) 
				int(id_value[1:])
			except:
				ids[id_key] = id_value
		return ids
	
	def test_invalid_str(self):
		""" 
		Set any tags with a complete banned string within to None. Returns a dictionary of tags. 
		"""
		ids = {}
		for invalid in invalid_list:
			for id_key, id_value in id_dict.items(): 
				try: 
					if invalid in id_value: 
						id_value = None
					ids[id_key] = id_value
				except TypeError:
					pass 
		return ids
	
	def test_NONE_type(self):
		ids = {}
		for id_key, id_value in id_dict.items():
			if id_value != None: 
				ids[id_key] = id_value
		return ids 

def parse_name(str, split_char=' '): 
	""" 
	Parse a name in string format, attempt to find possible MP3 tags in a set of music files with naming scheme as follows. 
	'[artist][song]' where it is possible that some names are corrupt or do not follow the naming scheme. 
	Use various tests to invalidate any tags that do not apply. 
	"""
 
	ignore_tag = ['.com']
	bracket_index = [] 
	ids = {'artist':None, 'song':None}
	
	for ci in range(len(str)): 
		if str[ci] in ['[',']']: 
			bracket_index.append(ci)
	
	if len(bracket_index) < 2: 
		pass 
		
	elif len(bracket_index) in [2,3]: 
		ids['artist'] = str[bracket_index[0]+1:bracket_index[1]]
	
	elif len(bracket_index) == 4:
		ids['artist'] = str[bracket_index[0]+1:bracket_index[1]]
		ids['song'] = str[bracket_index[2]+1:bracket_index[3]]
		
	ids = test_invalid_str(ignore_tag, ids)
	ids = test_int(ids)
	for key, value in ids.items(): 
		ids[key] = remove_whitespace(value, split_char) 
	
	return ids 

def remove_whitespace(str, split_char): # split_char is the character used in place of whitespace  
	try: 
		str = split_char.join(str.split())
		if str not in [None, '']:
			return str
	except AttributeError: 	
		return 
	return
	
def tag_music(mp3, dict):
	""" 
	Take a MP3 file object and a dictionary and set all MP3 tags. 
	"""
	for key, value in dict.items():
		mp3.key = value 		
	mp3.save() 
	
def test_invalid_str(invalid_list, id_dict):
	""" 
	Set any tags with a complete banned string within to None. Returns a dictionary of tags. 
	"""
	ids = {}
	for invalid in invalid_list:
		for id_key, id_value in id_dict.items(): 
			try: 
				if invalid in id_value: 
					id_value = None
				ids[id_key] = id_value
			except TypeError:
				pass 
	return ids
	
def test_int(id_dict):
	"""
	Set any ids that are comprised of numbers only to None. 
	"""
	ids = {} 
	for id_key, id_value in id_dict.items():
		try: 
			int(id_value) 
			int(id_value[1:])
		except:
			ids[id_key] = id_value
	return ids

def remove_NONE(id_dict): 
	ids = {}
	for id_key, id_value in id_dict.items():
		if id_value != None: 
			ids[id_key] = id_value
	return ids 

accepted_artists = []	
mypath = './'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))] 
for file in onlyfiles: 
	if file[-4:] == '.mp3': 
		mp3 = MP3File(file) 
		tags = remove_NONE(parse_name(file))
		try:
			if tags['artist'] in accepted_artists:
				tag_music(mp3, {'artist':tags['artist']})
				tags.pop('artist', None)
		except KeyError: 
			pass 
		if tags == {}: # Catch any empty ids, continue to next 
			continue
		print('{} : {}'.format(file, tags))
		user_option = input("Are these tags correct? y/n ")
		if user_option.lower() == 'y':
			tag_music(mp3, tags) 
			try: 
				accepted_artists.append(tags['artist']) # We do not want to auto-accept duplicate song names, only artist names
			except KeyError: 
				pass
