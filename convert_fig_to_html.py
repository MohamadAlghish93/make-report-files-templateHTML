def convert_fig_to_html(fig):
  """ Convert Matplotlib figure 'fig' into a <img> tag for HTML use using base64 encoding. """
  import urllib
  from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
  import StringIO
  
  canvas = FigureCanvas(fig)
  png_output = StringIO.StringIO()
  canvas.print_png(png_output)
  data = png_output.getvalue().encode('base64')
  
  return '<img src="data:image/png;base64,{}">'.format(urllib.quote(data.rstrip('\n')))