from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
print(img)

# O/P: python3 images.py
# <PIL.JpegImagePlugin.JpegImageFile image mode = RGB size = 640x640 at 0x106F4DB90 >

print(dir(img))

# O/P: ['_Image__transformer', '__array_interface__', '__class__', '__copy__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format
# __', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__r
# educe__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_close_exclusive_fp_after_loading'
# , '_copy', '_crop', '_dump', '_ensure_mutable', '_exclusive_fp', '_exif', '_expand', '_get_safe_box', '_getexif', '_getmp', '_min_frame', '_new', '_open', '_repr_png
# _', '_seek_check', '_size', 'alpha_composite', 'app', 'applist', 'bits', 'category', 'close', 'convert', 'copy', 'crop', 'custom_mimetype', 'decoderconfig', 'decoder
# maxblock', 'draft', 'effect_spread', 'entropy', 'filename', 'filter', 'format', 'format_description', 'fp', 'frombytes', 'get_format_mimetype', 'getbands', 'getbbox'
# , 'getchannel', 'getcolors', 'getdata', 'getexif', 'getextrema', 'getim', 'getpalette', 'getpixel', 'getprojection', 'height', 'histogram', 'huffman_ac', 'huffman_dc
# ', 'icclist', 'im', 'info', 'layer', 'layers', 'load', 'load_djpeg', 'load_end', 'load_prepare', 'load_read', 'mode', 'palette', 'paste', 'point', 'putalpha', 'putda
# ta', 'putpalette', 'putpixel', 'pyaccess', 'quantization', 'quantize', 'readonly', 'reduce', 'remap_palette', 'resize', 'rotate', 'save', 'seek', 'show', 'size', 'sp
# lit', 'tell', 'thumbnail', 'tile', 'tobitmap', 'tobytes', 'toqimage', 'toqpixmap', 'transform', 'transpose', 'verify', 'width'
