#MenuTitle: Set Export Paths to Adobe Fonts Folder
# -*- coding: utf-8 -*-
__doc__="""
Sets the OpenType font and Variable Font export paths to the Adobe Fonts Folder.
"""

import subprocess

def executeCommand( command, commandArgs ):
	commandExecution = subprocess.Popen( command.split(" ")+commandArgs, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
	output, error = commandExecution.communicate()
	returncode = commandExecution.returncode
	return returncode, output, error

adobeFontsFolder = "/Library/Application Support/Adobe/Fonts"

# Make sure the folder actually exists:
pathSegments = adobeFontsFolder.split("/")[1:]
path = ""
for pathPart in pathSegments:
	path += "/%s" % pathPart
	returncode, output, error = executeCommand( "cd", [path] )
	if returncode != 0 and "No such file or directory" in error:
		print "Creating directory: %s" % path
		returncode, output, error = executeCommand( "mkdir", [path] )
		if returncode != 0:
			print "   Returncode: %s\n   Output: %s\n   Error: %s" % ( returncode, output, error )

# Changing the export paths for Glyphs:
settings = ( "GXExportPath", "OTFExportPath" )
for setting in settings:
	print "Setting %s to %s:" % (setting, adobeFontsFolder),
	try:
		Glyphs.defaults[setting] = adobeFontsFolder
		print "OK."
	except Exception as e:
		print "\nTRACEBACK:"
		import traceback
		print traceback.format_exc()
		print "\nEXCEPTION:"
		print e
