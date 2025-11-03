#import "@preview/cades:0.3.1": qr-code
#import "@preview/polylux:0.4.0": *

#let slidew(
  slide_title: str,
  title: str,
  course: str,
  author: str,

  body
) = {
  set page(
    margin: 2cm,
    footer: align(bottom,
      toolbox.full-width-block(fill: rgb("#035a75"), inset: 8pt)[
        #align(center)[
          #text(fill: white, 10pt, title + " - " + course + " - " + author)
        ]
      ]
    ),
  )

  heading(slide_title)

  v(1em)

  body
}

#let center_url(url) = {
  align(center)[ *#url* ]
}

#let url_with_qr(url, height: 65%) = {
  align(center)[
    #qr-code(url, height: height)
  ]
  center_url(url)
}
