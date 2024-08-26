
# Using Backends in TStickers

TStickers supports multiple backends for converting sticker formats. You can choose between
`rlottie-python` and `pyrlottie` depending on your needs and system compatibility. Here’s a brief
guide on how to use and select these backends.

## Available Backends

- **pyrlottie**: in my testing this seems to be a little faster at converting telegram stickers
- **rlottie-python**: this backend has broader system compatibility, though seems to be a little
  slower on my machine™

## How to Specify a Backend

You can specify the backend you want to use by using the `-b` or `--backend` option in your
TStickers command.

### Command Syntax

```bash
tstickers -b BACKEND [other options]
```

### Examples

1. **Using `rlottie-python` Backend:**

   If you want to use the `rlottie-python` backend, run:

   ```bash
   tstickers -b rlottie-python -t YOUR_BOT_TOKEN -p https://t.me/addstickers/YourStickerPack
   ```

   This command uses the `rlottie-python` backend to process the sticker pack specified by the URL.

2. **Using `pyrlottie` Backend:**

   To use the `pyrlottie` backend, execute:

   ```bash
   tstickers -b pyrlottie -t YOUR_BOT_TOKEN -p https://t.me/addstickers/YourStickerPack
   ```

   This command processes the sticker pack using the `pyrlottie` backend.

## Choosing the Right Backend

- **Performance:** Test both backends to see which one performs better for your specific needs.
- **Compatibility:** If you are having trouble with the default then try `rlottie-python`.

Note if performance is important then you may want to explore the other options  `--frameskip` and
`--scale`. These will change the quality of the output image though!
