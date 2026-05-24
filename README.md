# CelebClock

## Screenshot

![CelebClock screenshot](imgs/celebclockscreenshot.jpg)

## Current Goal
Build and curate a minute-based celebrity pointing image set for the clock, with clear tracking for source, copyright status, local filename, and download state.

## Consolidated Minute List (sorted by minute)

| Minute | Celebrity | Category | URL | Copyright Name | Copyright Link | Filename | Downloaded |
|---|---|---|---|---|---|---|---|
| 0 | Uncle Sam | Icon | [source](https://upload.wikimedia.org/wikipedia/commons/d/df/Uncle_Sam_%28pointing_finger%29.png) | U.S. Government / Public Domain | [Wikimedia file](https://commons.wikimedia.org/wiki/File:Uncle_Sam_(pointing_finger).png) | 00-unclesam.png | [ ] |
| 0 | Marilyn Monroe | Actor | [source](https://m.media-amazon.com/images/I/41GG7QCm3yL._AC_.jpg) | UNKNOWN |  | 00-marilynmonroe.jpg | [ ] |
| 0 | Jackie Chan (2nd) | Actor | [source](https://i.pinimg.com/736x/b0/fe/7a/b0fe7ad5ece0c175d3e43311ba245040.jpg) | UNKNOWN |  | 00-jackiechan2.jpg | [ ] |
| 7 | Muhammad Ali | Athlete | [source](https://preview.redd.it/muhammad-ali-finger-pointing-joe-frazier-1974-v0-jewmue4g6wg71.jpg?width=1080&crop=smart&auto=webp&s=7ec28592ef3754515f56356a098f254d2b16ec84) | UNKNOWN |  | 07-muhammadali.jpg | [x] |
| 8 | David Bowie | Musician | image provided (no URL stored) | UNKNOWN |  | 08-davidbowie.jpg | [ ] |
| 9 | Meryl Streep | Actor | [source](https://media.vanityfair.com/photos/54ea998073b710d476cfec15/master/w_1600,c_limit/patricia-arquette-acceptance-speech.png) | UNKNOWN |  | 09-merylstreep.jpg | [ ] |
| 10 | Denzel Washington | Actor | [source](https://www.goldderby.com/wp-content/uploads/2017/11/denzel-washington-roman-j-israel-esq.jpg?w=620&h=360&crop=1) | UNKNOWN |  | 10-denzelwashington.jpg | [ ] |
| 10 | Barack Obama (2nd) | Government | [source](https://compote.slate.com/images/b0a7a633-9ee5-4be9-b063-2075ad1e4290.jpg?crop=5000%2C3200%2Cx0%2Cy0&width=840) | UNKNOWN |  | 10-barackobama2.jpg | [ ] |
| 13 | Denzel Washington (2nd) | Actor | [source](https://variety.com/wp-content/uploads/2013/08/denzel-washington-broadway-return.jpg?w=1000&h=562&crop=1&resize=681%2C383) | UNKNOWN |  | 13-denzelwashington2.jpg | [ ] |
| 15 | Donald Trump | Government | [source](https://www.politico.com/dims4/default/resize/630/quality/90/format/webp?url=https%3A%2F%2Fstatic.politico.com%2Fda%2Fe3%2F78e5ac7340359c644708d3681102%2F181113-donald-trump-pointing-gty-773.jpg) | UNKNOWN |  | 15-donaldtrump.jpg | [ ] |
| 16 | Audrey Hepburn | Actor | [source](https://media.gettyimages.com/id/129921506/photo/audrey-hepburn-in-how-to-steal-a-million.jpg?s=1024x1024&w=gi&k=20&c=_Hdmho3zO5GThYpipU1kqHV3bBLrQoTZlYBayD2CvX0=) | UNKNOWN |  | 16-audreyhepburn.jpg | [ ] |
| 18 | Hillary Clinton | Government | [source](https://www.politico.com/dims4/default/resize/630/quality/90/format/webp?url=http%3A%2F%2Fs3-origin-images.politico.com%2F2015%2F08%2F19%2F150818_hillary_clinton_gty_1160.jpg) | UNKNOWN |  | 18-hillaryclinton.jpg | [ ] |
| 19 | Beyonce | Musician | [source](https://static01.nyt.com/images/2012/10/16/arts/16artsbeat-beyonce/16artsbeat-beyonce-blog480.jpg) | UNKNOWN |  | 19-beyonce.jpg | [ ] |
| 30 | Barack Obama | Government | [source](https://waterfordwhispersnews.com/wp-content/uploads/2014/06/Obama-Pointing.gif) | UNKNOWN |  | 30-barackobama.gif | [ ] |
| 40 | Elvis Presley | Musician | [source](https://gcp-na-images.contentstack.com/v3/assets/bltea6093859af6183b/blt8ece2b5f1e16431f/6988d91f8fd2eed8e63585b9/elvis-in-heart-america.jpg?branch=production&width=750&quality=75&auto=webp&crop=3:2) | UNKNOWN |  | 40-elvispresley.jpg | [ ] |
| 45 | Cate Blanchett | Actor | [source](https://img.buzzfeed.com/buzzfeed-static/static/2022-10/27/8/asset/17e6421eaf05/sub-buzz-1753-1666858987-4.jpg?downsize=600:*&output-format=auto&output-quality=auto) | UNKNOWN |  | 45-cateblanchett.jpg | [ ] |
| 45 | ET | Film | [source](https://pbs.twimg.com/media/Ey2wWl-U4AMA5D3?format=jpg&name=small) | UNKNOWN |  | 45-et.jpg | [ ] |

## Notes
- Only one image is currently local/downloaded: minute 7 (`imgs/ali_7.jpg`).
- Minutes not listed above still require source candidates.
- Unknown copyright rows are intentionally marked `UNKNOWN` until validated.

## Setup Folder
The new setup workflow is in [setup/](setup):
- [setup/ai-instructions.md](setup/ai-instructions.md)
- [setup/data/celebMinutes.json](setup/data/celebMinutes.json)
- [setup/js/workflowState.js](setup/js/workflowState.js)
- [setup/js/runWorkflow.js](setup/js/runWorkflow.js)
- [setup/js/nonRepeatingPicker.js](setup/js/nonRepeatingPicker.js)

Run the summary script:

```bash
cd setup
npm run workflow:summary
```
