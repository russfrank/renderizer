class plugin:
  
  def __init__ (self, desc):
    """Initialized for each 'group' that is being rendered.  Handed the 'desc'
    object, which is the full output description (ie, this group's decoded
    yaml data)."""
    print 'plugin initializing'

  def beforeRender (self, sourceImage, tempFilename, outputConfig, pluginConfig):
    """Called before rendering every image"""
    print 'beforeRender ', sourceImage

  def afterRender (self, sourceImage, tempFilename, outputConfig, pluginConfig):
    """Called after rendering every image"""
    print 'afterRender ', sourceImage
