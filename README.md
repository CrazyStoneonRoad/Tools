# Tools
Some tools for remote sensing object detection.

# `./DIOR/`
Dealing with the DIOR remote sensing object detection data set.
- `AddKeys`: DIOR annotation files lack some keys. This may cause error in some codes. This file converts `.xml` files from `path` to `Opth`. NOTE: Put this file under `.../DIOR/`.
- `get_class`: To train models on DIOR, class names should be exactly correct. This file is used to get class names from `.xml` files.
