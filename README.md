# Hi, I'm Alessandro <img src="https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/spacer.png" width="30"/><img src="https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/psi-small.gif" height="50"/>

I'm Alessandro Candido, a theoretical physicist working in HEP, with a passion for coding and
computer science.

- Personal Website &nbsp; <a href="http://alecandido.github.io"><img src="https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/world-icon.png" height="30"/></a>
- Contact me &nbsp; <a href="mailto:candido.ale@gmail.com"><img src="https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/mail-icon.png" height="20"/></a>

<details>
  <summary> <b> Current Position </b> </summary>

## Current Position

<!--At the present time I'm a PhD student at the [University of-->
<!--Milan](https://www.unimi.it/en),-->
<!--a member of the [N3PDF](http://n3pdf.mi.infn.it/) team,-->
<!--and of the [NNPDF](http://nnpdf.mi.infn.it/) collaboration.-->

```yaml
position: PhD
supervisor: S. Forte
start_date: November, 2019
institutions:
  university: Università degli Studi di Milano
  affiliation: INFN
  team: N3PDF
  collaboration: NNPDF
```

<p align="center">
  <a href="https://www.unimi.it/en">
    <img
        src="https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/unimi_banner.png"
        alt="University of Milan"
        height="60"
      />
  </a>
  <img
      src="https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/spacer.png"
      width="40"
    />
  <a href="https://www.mi.infn.it/it/">
    <img
        src="https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/infn_logo.png"
        alt="INFN"
        height="60"
      />
  </a>
  <img
      src="https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/spacer.png"
      width="40"
    />
  <a href="http://n3pdf.mi.infn.it/">
    <img
        src="https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/n3pdf_logo.png"
        alt="N3PDF"
        height="60"
      />
  </a>
  <!--<img-->
      <!--src="https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/spacer.png"-->
      <!--width="40"-->
    <!--/>-->
  <!--<a href="https://erc.europa.eu/">-->
    <!--<img-->
        <!--src="https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/erc_logo1.png"-->
        <!--alt="ERC"-->
        <!--height="60"-->
      <!--/>-->
  <!--</a>-->
  <img
      src="https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/spacer.png"
      width="40"
    />
  <a href="http://nnpdf.mi.infn.it/">
    <img
        src="https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/nnpdf_logo.png"
        alt="NNPDF"
        height="30"
      />
  </a>
</p>

</details>

<details>
  <summary> <b> Education </b> </summary>

## Education

```yaml
Bachelor:
  title: Bachelor of Science (BSc), Physics
  university: University of Pisa (Unipi)
  grade: 110 cum laude
  start-date: September 2014
  finish-date: June 2017

Master:
  title: Master of Science (MSc), Theoretical Physics
  university: University of Pisa (Unipi)
  grade: 110 cum laude
  start-date: September 2017
  finish-date: October 2019
  thesis:
    title: Simplicial quantum gravity with dynamical gauge fields
    supervisor: M. D'Elia

Diploma di Licenza:
  title: Diploma di Licenza (1), Physics
  institution: Scuola Normale Superiore (SNS)
  grade: 100 cum laude (2)
  start-date: September 2014
  finish-date: July 2020
```

`(1)` Custom title by Scuola Normale Superiore, obtained by all the students that
complete the full course; somewhat parallel to a MSc, more on the [SNS
website](https://www.sns.it/it/scuola-normale-superiore/statuto-regolamenti-codice-etico)  
`(2)` Final grade has been introduced in 2020 at SNS

<p align="center">
  <a href="https://www.unipi.it/index.php/english">
    <img
        src="https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/unipi_banner.png"
        alt="University of Pisa"
        height="100"
      />
  </a>
  <img
      src="https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/spacer.png"
      width="80"
    />
  <a href="https://www.sns.it/en">
    <img
        src="https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/sns_banner.png"
        alt="Scuola Normale Superiore"
        height="100"
      />
  </a>
</p>

</details>

<details>
  <summary> <b> Academic Code Projects </b> </summary>

## Academic Code Projects

### PhD

```yaml
name: yadism - Yet Another DIS Module
subject:
  area: physics
  topic: HEP - QCD
supervisor: S. Forte
collaborators:
  - F. Hekhorn
description: |
  WIP
```

<p align="center">
  <a href="http://n3pdf.github.io/yadism">
    <img
        src="https://raw.githubusercontent.com/N3PDF/yadism/master/docs/logo/logo.png"
        alt="yadism"
        height="120"
      />
  </a>
  <img
      src="https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/spacer.png"
      width="40"
    />
  <a href="https://github.com/N3PDF/yadism">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=N3PDF&repo=yadism" />
  </a>
</p>

### Master Thesis

```yaml
name: CDT 2D
subject:
  area: physics
  topic: quantum gravity
  approach: asymptotic safety
supervisor: M. D'Elia
collaborators:
  - G. Clemente
description: |
  explore the space of discrete space-times in Einstein gravity applying a
  Markov Chain Monte Carlo approach, through the Metropolis-Hastings algorithm

  the considered space is made by Triangulations, suitable to approximate a
  generic space-time with a finite length scale (lattice spacing), with a
  time-sliced structure (so they are called Causal)
original: |
  in this project a 2D simulation has been implemented, with an original
  algorithm for gauge fields introduction (a U(1) gauge field is implemented,
  the algorithm is directly generalizable to SU(2) and U(N))
```

<p align="center">
  <a href="https://github.com/AleCandido/CDT_2D">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=alecandido&repo=cdt_2d" />
  </a>
</p>

</details>

<details>
  <summary> <b> Code Skills </b> </summary>

## Code Skills

</details>

<p>
<a href="https://alecandido.github.io">
  <img
     src="https://raw.githubusercontent.com/AleCandido/AleCandido/master/assets/plane.gif"
     height="200"
     />
</a>

<a href="https://github.com/anuraghazra/github-readme-stats">
  <img align="right" src="https://github-readme-stats.vercel.app/api?username=alecandido&show_icons=true" />
</a>
</p>
<!-- ![My github stats](https://github-readme-stats.vercel.app/api?username=alecandido&show_icons=true&hide_border=true&title_color=fff&icon_color=79ff97&text_color=9f9f9f&bg_color=151515) -->
