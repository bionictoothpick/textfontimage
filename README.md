# text-font-image
## Community Node For InvokeAI

text font to text image node for InvokeAI, download a font to use (or if in font cache uses it from there), the text is always resized to the image size, but can control that with padding, optional 2nd line

* simple node textfontimage.py (Simple centered 2 line's of Texted)
* more advanced node advtextfontimage.py (gives you alot more control over text size and location)
* extrude node made by lillekemiker (keeping upto date here)

### Font dropdown (this fork)

The `local_font` dropdown lists fonts by name from:

* InvokeAI's fonts folder (`<invokeai root>/fonts`, set by `fonts_dir` in `invokeai.yaml`), including subfolders
* this node's `font_cache` folder
* installed system fonts (Windows: `C:\Windows\Fonts` and per-user fonts; Linux/macOS: the usual font folders)

To add a font, copy a `.ttf` or `.otf` file into one of those folders and restart InvokeAI. The list is built at startup.

This fork also gives `text_input_second_row` and `local_font_path` empty defaults, so the nodes run on InvokeAI 6.x without connecting those fields.

### Example workflows (this fork)

The [`workflows`](workflows) folder has two ready-made workflows. In InvokeAI, open **Workflows**, choose **Load from File** and pick a `.json` file.

**[Word Made of Leaves.json](workflows/Word%20Made%20of%20Leaves.json)** makes your word out of a material inside a full scene, for example LEAF made of leaves on a forest floor.

![Word Made of Leaves example](workflows/examples/word_made_of_leaves.png)

**[Word Made of Leaves - Transparent.json](workflows/Word%20Made%20of%20Leaves%20-%20Transparent.json)** makes the same image, then keeps only the letters. Everything outside the letter shapes is made transparent and the result is cropped to the word. The output is a transparent PNG, ready for logos, overlays and slides.

![Word Made of Leaves - Transparent example](workflows/examples/word_made_of_leaves_transparent.png)

How they work: Text Font to Image renders your word as white letters on black. The QRCode Monster ControlNet uses that image to guide an SD1.5 model, so the material forms the letters. The transparent version then turns the same letter image into a mask, applies it as the alpha channel and crops to the letters.

Fields you will change most:

| Field | Description |
| ----- | ----------- |
| 1. Your Word / Text Input | The word to make |
| Local Font | Font from the dropdown (default Arial Black). Bold, heavy fonts work best |
| 2. What the word is made of | The material, e.g. leaves, stones, flowers, wood grain. Describe the material only; mentioning "letters" tends to give plain solid letters |
| 3. Word strength / Control Weight | Default 1.15. Raise it (1.3 to 1.4) if the word is hard to read; lower it (about 1.0) for a more natural look |

Requirements:

* This node pack
* An SD1.5 model (the workflows were made with DreamShaper 8)
* The **QRCode Monster v2 (SD1.5)** ControlNet, available in InvokeAI's Model Manager under Starter Models

The model and font selections were saved on one install, so after loading a workflow, re-select the SD1.5 model, the ControlNet and the font if they show as missing.

Text Font to Image Node

| Fields                  | Description                                            |
| ------------------------ | ------------------------------------------------------ |
| text_input               | The text from which to generate an image               |
| text_input_second_row    | The second row of text to add below the first text     |
| second_row_font_size     | Font size for the second row of text (optional)        |
| font_url                | URL address of the font file to download               |
| local_font_path         | Local font file path (overrides font_url)              |
| local_font              | Font dropdown: InvokeAI's fonts folder, the node's font_cache folder and installed system fonts (overrides local_font_path and font_url) |
| image_width              | Width of the output image                              |
| image_height             | Height of the output image                             |
| padding                  | Padding around the text in pixels                       |
| row_gap                  | Gap between the two rows of text in pixels 

Advanced Text Font to Image Node

| Fields                  | Description                                            |
| ------------------------ | ------------------------------------------------------ |
| text_input               | The text from which to generate an image               |
| text_input_second_row    | The second row of text to add below the first text     |
| font_url                | URL address of the font file to download               |
| local_font_path         | Local font file path (overrides font_url)              |
| local_font              | Font dropdown: InvokeAI's fonts folder, the node's font_cache folder and installed system fonts (overrides local_font_path and font_url) |
| image_width              | Width of the output image                              |
| image_height             | Height of the output image                             |
| font_color_first         | Font color for the first row of text in HEX format     |
| x_position_first         | X position of the first row of text                    |
| y_position_first         | Y position of the first row of text                    |
| rotation_first           | Rotation angle of the first row of text (in degrees)   |
| font_size_first          | Font size for the first row of text                     |
| font_color_second        | Font color for the second row of text in HEX format    |
| x_position_second        | X position of the second row of text                   |
| y_position_second        | Y position of the second row of text                   |
| rotation_second          | Rotation angle of the second row of text (in degrees)  |
| font_size_second         | Font size for the second row of text                    |
| base_image               | An image to place the text onto      |

## Example Workflow
![image](https://github.com/mickr777/textfontimage/assets/115216705/e226a5e0-eadb-426a-89fe-3657c546d5ed)

## Examples
using Results after using the @LilleKemiker extrude node and depth controlnet

![710113a2-1915-43b2-ba9b-062c3338316a](https://github.com/mickr777/textfontimage/assets/115216705/3e591f7e-b86e-4fcf-810e-3caffb278936)
![ef420c9c-b780-45b9-b2d3-608ee6516785](https://github.com/mickr777/textfontimage/assets/115216705/32b47c93-f953-4d51-8ffa-cdb3bcc2a084)
![babd69c4-9d60-4a55-a834-5e8397f62610](https://github.com/mickr777/textfontimage/assets/115216705/46c3f2aa-c5fc-4fcf-9daf-49966ad98e73)
![9133eabb-bcda-4326-831e-1b641228b178](https://github.com/mickr777/textfontimage/assets/115216705/8c20f1e2-fd06-4256-a005-f56ccc4218ee)
![3f396f80-b448-4e40-a960-c7a68fae5623](https://github.com/mickr777/textfontimage/assets/115216705/7fb07189-4138-4f64-8cd3-3d61bb372b81)
![93a89944-14e3-49fc-97c2-8593f22abd30](https://github.com/mickr777/textfontimage/assets/115216705/d8ffe6ea-2545-4fad-b188-3730e6db9a8c)
![2f37c9fa-f677-45b6-aaec-c845994061d9](https://github.com/mickr777/textfontimage/assets/115216705/648202db-6bf2-465e-843b-d6b52393912f)
![4f9a3fa8-9be9-4236-8a3e-fcec66decd2a](https://github.com/mickr777/textfontimage/assets/115216705/e4c51693-4455-4f55-99fe-3bcaf38241de)
![e2fe744b-7988-4f8e-8fca-6a2ec0e51153](https://github.com/mickr777/textfontimage/assets/115216705/0990db3f-9235-4fc2-a8f6-f06d55c4d93d)
![a1593f97-8735-4f05-b79e-1a48c956fc92](https://github.com/mickr777/textfontimage/assets/115216705/f298b05b-51bb-4d8b-9266-6962640ce51c)
