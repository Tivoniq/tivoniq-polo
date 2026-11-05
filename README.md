# TIVONIQ Core Polo, 3D viewer

An interactive 3D view of the TIVONIQ Core Polo. One static page, no build step, no tracking.

**Live:** https://tivoniq.github.io/tivoniq-polo/

## Use it

| Action | Mouse | Touch |
|---|---|---|
| Spin the shirt | drag | one finger |
| Zoom to a spot | scroll over it | pinch |
| Pan | shift-drag or right-drag | two fingers |
| Zoom in / reset | double-click | double-tap |

The bar at the bottom switches colour (Heather Grey, Midnight Navy, Carbon, Slate, Cloud), front and back view, breeze, collar and sleeve trim (auto, white, black, tonal), and a shake.

## How it works

- The shirt is real cloth simulation (position-based dynamics), meshed from the flat pattern of the size-M tech pack and draped over an invisible body. The collar, cuffs, placket and buttons are modelled in 3D.
- The upper body is rigid; only the lower body swings. Spin speed is limited so the cloth can never be thrown apart, and the page restores the last good drape if the cloth ever tangles.
- The simulation sleeps when nothing is moving, so an idle page uses no CPU or GPU.
- Rendering uses [three.js](https://threejs.org) 0.152.2, loaded from the jsDelivr CDN.

## Files

- `index.html`: the published page (self-contained apart from three.js).
- `src/polo-3d.src.html`: readable source. `src/build.py` fills the official logo files in from [`Tivoniq/tivoniq-brand`](https://github.com/Tivoniq/tivoniq-brand).

## Usage

© TIVONIQ. The TIVONIQ name and logo are trademarks of TIVONIQ. The logo files come unmodified from the brand repository and follow its usage guidelines.
