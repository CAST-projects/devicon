## Optimize SVG files

See https://github.com/svg/svgo

```
npm -g install svgo
```

Then

```
svgo -f ./path/to/folder/with/svg/files -o ./path/to/folder/with/svg/output
```

## How to generate SVG containing all images

See https://www.npmjs.com/package/svg-join for the package reference.

To create the original icons, please run the command line:
```
svg-join -s "./*/*-original.svg" -o ../originalicons -n original-icons
```

To create the plain icons, please run the command line:
```
svg-join -s "./*/*-plain.svg" -o ../plainicons -n plain-icons
```
