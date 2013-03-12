#MenuTitle: Align Selection to Baseline
"""Align selected paths (and parts of paths) in the frontmost layer to the Baseline."""

import GlyphsApp

Doc = Glyphs.currentDocument
# FontMaster = Doc.selectedFontMaster()
selectedLayer = Doc.selectedLayers()[0]
# layerWidth = selectedLayer.width

try:
	selection = selectedLayer.selection()
	lowestY = min( ( n.y for n in selection ) )

	Font.disableUpdateInterface()

	for thisNode in selection:
		thisNode.y -= lowestY

	Font.enableUpdateInterface()
	
except Exception, e:
	print "Error: Nothing selected in frontmost layer?"
	print e