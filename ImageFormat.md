
File Format: defines how image data is stored on disk. Different formats have varying levels of compression, support for transparency, metadata, and other features. Common formats include JPEG, PNG, GIF, BMP, and TIFF.

Color Space: describes how colors are mathematically represented and encoded in an image. Different color spaces define colors based on different attributes, such as RGB, CMYK, HSV, Lab, and more.
Different color spaces define colors in different ways. 

Different color spaces have different advantages and use cases. For example, RGB is well-suited for displaying colors on screens, while Lab is often used for image editing due to its perceptual uniformity.

When you load an image using libraries like PIL or opencv, the color space might be converted to the internal color space of the library, which is suitable for the library's image processing functions. For example, opencv often uses BGR color order internally, while PIL and face_recognition typically uses RGB.

Same thing for when you load an image into memory using PIL (Pillow) or OpenCV, the library typically converts the image data from the file format on disk into an internal representation that the library uses for image processing. For example: In PIL (Pillow), the internal representation is the PIL.Image.Image object, while in opencv, the internal representation is a numpy array.
