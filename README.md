# Personal Site

A static site built with Hugo.

## Image Processing

Images are automatically processed when you build the site:

- **Max width**: 800px (preserves aspect ratio)
- **High-DPI**: Generates both 1x and 2x versions
- **Orientation**: Automatically corrects EXIF rotation
- **Responsive**: Browser chooses best version

### Usage

Put images in the same folder as your markdown file:

```
content/blog/post-name/
├── index.md
├── image1.jpg
└── image2.png
```

Reference them normally in markdown:
```markdown
![Alt text](image.jpg)
```

### Build

```bash
hugo --minify
```

Images are automatically processed and optimized.