#
# This file lets you post a HIT on Turk using the command line tools.
# This allows you to post HITs by telling Turk which URL to show to subjects
# inside the Turk window.
#
# 1. login to scorsese.wjh.harvard.edu
# 2. open the terminal on your computer and run these commands to post to the SANDBOX
# 		$ cd /Volumes/turk/experiments/cfm/Search9
#		$ python postHitSandbox_Search9.py turkHitParams.py
#
# This will only work if you have the boto toolbox for python installed on your computer,
# and if you are using python 2.7 (google "Anaconda python 2.7" to install on MAC).
#
# MAC Installation Instructions for boto tools:
# If you already have pip installed, then go to Terminal and type 'pip install boto'.
# If you don't have pip, try using easy_install to install pip first:
# 'easy_install pip'
#
# Alternatively, you can do this:
# $ git clone https://github.com/boto/boto.git
#
# then:
# $ cd boto
# $ sudo python setup.py install
#

# import boto tools
from boto.mturk.connection import MTurkConnection
from boto.mturk.question import ExternalQuestion
import boto.mturk.qualification as mtqu

# import modules for accessing system/os variables
import sys
import os

# helper modules for printing objects, e.g., pprint(vars(object))
from pprint import pprint

# actual urls
HOST = 'mechanicalturk.amazonaws.com'
PREVIEW = "https://www.mturk.com/mturk/preview"

# sandbox urls
# HOST = 'mechanicalturk.sandbox.amazonaws.com'
# PREVIEW = "https://workersandbox.mturk.com/mturk/preview"


# function that posts the hit
def PostHits_loop():
	# To post a HIT, first connect to Turk using our access codes:
	# The ACCESS_ID and SECRET_KEY are loaded before this function is called
	# (e.g., from alvarezlab import * );
	mtc = MTurkConnection(aws_access_key_id = ACCESS_ID,
                        aws_secret_access_key = SECRET_KEY,
                        host = HOST)

	for x in range(startHSet, endHSet+1):
		HSet = x
		urlForHIT = "https://scorsese.wjh.harvard.edu/turk/experiments/cfm/Search10/index_cmtrial_Search10.html?HSetNum=%d" % HSet

		# Now lets setup a structure for our external HIT. We need the URL we want to be
		# shown within the Turk window and also how tall we want the Turk iframe to be:
		q = ExternalQuestion(external_url=urlForHIT,
			frame_height=frameHeight)

		# And any qualifications we want people to have:
		qualifications = mtqu.Qualifications()

		qualifications.add(mtqu.PercentAssignmentsApprovedRequirement('GreaterThanOrEqualTo', percentAssignmentsApprovedRequirement))
		qualifications.add(mtqu.LocaleRequirement("EqualTo", localeRequirement))
		if (qualificationID != "NONE"):
			qualifications.add(mtqu.Requirement(qualificationID,"EqualTo",1,notifyWorkerOfQualification))

		# Post:
		theHIT = mtc.create_hit(question = q,
							  lifetime = minToSec(minutesBeforeHitExpires),
							  max_assignments = numAssignmentsToPost,
							  title = titleForWorkers,
							  description = descriptionForWorkers,
							  keywords = keywordsForWorkers,
							  qualifications = qualifications,
							  reward = pay,
							  duration = minToSec(minutesForUsersToFinish),
							  approval_delay = minToSec(minutesBeforeAutoApproved),
							  annotation = projectNameForRequesters)

		# get more info about the hit
		hit = mtc.get_hit(theHIT[0].HITId)

		# Print out the HIT's ID if all went well:
		# pprint(vars(hit[0]))
		# print "Experiment info:"
		# print HOST
		print "preview hit in HSet ", HSet, ": "
		# print urlForHIT, "\n"
		# print "HITId"
		# print theHIT[0].HITId, "\n"
		print PREVIEW + "?groupId=" + hit[0].HITGroupId, "\n"


def minToSec(min):
  return min * 60

def hourToSec(hr):
  return hr * 60 * 60

def yesno():
	yes = set(['yes','y', 'ye', '1'])
	no = set(['no','n','0'])

	choice = raw_input().lower()
	if choice in yes:
		return True
	elif choice in no:
		return False
	else:
	   sys.stdout.write("Please respond with 'y' for yes, or 'n' for no.\n")

def loadfile(fileName):
	f = open(fileName, 'rt')
	data = {}
	try:
		reader = csv.reader(f,quotechar='"',quoting=csv.QUOTE_ALL, skipinitialspace=True)
		for row in reader:
			print row
			data[row[0]] = row[1]
	finally:
		f.close()
		return data

def printvalues(array):
	for key, value in array.iteritems():
		print key, value


# 
# # get the name of the parameter file and the path to the experiment folder
# # fileName = os.getcwd() + "/" + sys.argv[1]
# paramFileName  = os.path.basename(sys.argv[1])
# pathToExperimentFolder = os.path.dirname(sys.argv[1])
# 
# # import the turkHitParams.py add the directory passed in by the user
# folderName = sys.path.append(pathToExperimentFolder)
# from turkHitParams import *
# 
# # check to make sure a valid lab name was provided
# if (lab == "alvarezlab"):
# 	from alvarezlab import *
# elif (lab == "konklab"):
# 	from konklab import *
# elif (lab == "defreitas"):
# 	from defreitas import *
# elif (lab == "conwell"):
# 	from conwell import *		
# else:
# 	print "problemo...lab must equal 'alvarezlab' or 'konklab'"
# 	exit()

from turkHitParams import *

pathToServerBotoFolder = ('../../../boto');
sys.path.append(pathToServerBotoFolder)  
# check to make sure a valid lab name was provided
if (lab == "alvarezlab"):
	from alvarezlab import *
elif (lab == "konklab"):
	from konklab import *
elif (lab == "defreitas"):
	from defreitas import *
elif (lab == "conwell"):
	from conwell import *		
else:
	print "problemo...lab must equal 'alvarezlab' or 'konklab'"
	exit()



# print out parameters for user to review
print "\n"
print "Parameters loaded from: "
print "	", sys.argv[1], "\n"
print "Lab paying for hit: "
print "	", lab, "\n"

print "Describe your Hit to Workers:"
print "	titleForWorkers: ", titleForWorkers
print "	descriptionForWorkers: ", descriptionForWorkers
print "	keywordsForWorkers: ", keywordsForWorkers, "\n"

print "Project title (workers don't see this):"
print "	projectNameForRequesters: ", projectNameForRequesters, "\n"

print "Your HIT setup:"
print "	pay: ", pay
print "	numAssignmentsToPost: ", numAssignmentsToPost
print "	minutesBeforeHitExpires: ", minutesBeforeHitExpires
print "	minutesForUsersToFinish: ", minutesForUsersToFinish
print "	minutesBeforeAutoApproved: ", minutesBeforeAutoApproved, "\n"

print "Additional Worker Qualifications:"
print "	percentAssignmentsApprovedRequirement: ", percentAssignmentsApprovedRequirement
print "	localeRequirement: ", localeRequirement
print "	qualifications: ", qualificationID, "\n"

print "Design layout:"
# print "	externalURL: ", urlForHIT
print "	frameHeight: ", frameHeight, "\n"

# prompt the user to confirm submission
print "Post Hit [y/n]?:"
print HOST, "\n"
confirm = yesno()
if confirm == True:
	print("You said 'yes'\n...posting to Turk now...\n");
	PostHits_loop()
else:
	print("...quitting without posting.\n");
