[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT TITLE AND LOGO -->

# Django Portfolio Website

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#development">Development</a></li>
    <li><a href="#deployment">Deployment</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About

[![Product Name Screen Shot][website-screenshot]][website-url]

In this project I will be showing my step by step process for building a Django Portfolio Website. Django—an open-source web framework that's designed on top of Python—can help you quickly bring your website ideas to life. I plan to illustrate my undestanding of Django for web development, by building my own website from the ground up. I will create a database, design the layout for your website, and add and update URL paths. Then I will connect my Django portfolio website to Postgres, and add static files, URLs and more.

<!-- KEY OBJECTIVES -->

### Key objectives:

- Setting up URLs in Django project
- Creating models in Django
- Connecting Django project to Postgres
- Adding static images
- Designing the layout for website
- Creating object views
- Updating URL paths

<!-- GETTING STARTED -->

## Getting Started

Here are some instructions on how to get this project up and running. First you will need some some prerequsites to manage a local virtual environment. Bellow is a list of _'Bare Minimums'_ you need to follow along with this project.

- **[Python](https://www.python.org/downloads/)** 3.9.1
- **[Pip](https://pip.pypa.io/en/stable/installing/)** 21.0.1
- **[Anaconda](https://www.anaconda.com/products/individual)**

### Here is how we install them:

- Check if `python` and `pip` are installed

  ```sh
  python --version
  python -m pip --version
  ```

- If `python` is notinstalled, you can download it from the [Python website](https://www.python.org/downloads/). If `pip` is not installed, run the following command or [check out](https://pip.pypa.io/en/stable/installing/)

  ```sh
  python get-pip.py pip==21.0.1
  ```

### Installations:

1. Create a directory for the project, then download or clone project the project into the directory by simply run the following command in your terminal

   ```sh
   mkdir project
   cd project
   git clone https://github.com/TobiAdeniyi/django-portfolio-website
   ```

2. Install and activate the virtual environment, using `pip` as so

   ```sh
   python -m venv portfolio_website_environment
   source portfolio_website_environment/bin/activate
   python -m pip install requirements.txt
   pip list
   ```

   Or alternatively, if you have **Anaconda** installed, create and activate a virtual environment, using `conda`, by running the following command

   ```sh
   conda env create -f environment.yml
   conda activate portfolio_website_environment
   conda env list
   ```

3. **TODO**

<!-- DEVELOPMENT -->

## Development

#### TODO

<!-- DEPLOYMENT -->

### Deployment

#### TODO

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [Best README Temlate](https://www.webpagefx.com/tools/emoji-cheat-sheet)
- [LinkedIn Learn](https://www.linkedin.com/learning/building-a-personal-portfolio-with-django/starting-a-new-project-in-django?contextUrn=urn%3Ali%3AlyndaLearningPath%3A5d546c44498e876bef6651ba)
- [EMOJI CHEAT SHEET](https://www.webfx.com/tools/emoji-cheat-sheet/)
- [Bootstrap v5.0](https://getbootstrap.com/docs/5.0/getting-started/download/)
- [jQuery v3.6.0](https://jquery.com/download/)
- [Popper v2.x](https://popper.js.org/docs/v2/)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/TobiAdeniyi/django-portfolio-website.svg?style=for-the-badge
[contributors-url]: https://github.com/TobiAdeniyi/django-portfolio-website/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TobiAdeniyi/django-portfolio-website.svg?style=for-the-badge
[forks-url]: https://github.com/TobiAdeniyi/django-portfolio-website/network/members
[stars-shield]: https://img.shields.io/github/stars/TobiAdeniyi/django-portfolio-website.svg?style=for-the-badge
[stars-url]: https://github.com/TobiAdeniyi/django-portfolio-website/stargazers
[issues-shield]: https://img.shields.io/github/issues/TobiAdeniyi/django-portfolio-website.svg?style=for-the-badge
[issues-url]: https://github.com/TobiAdeniyi/django-portfolio-website/issues
[license-shield]: https://img.shields.io/github/license/TobiAdeniyi/django-portfolio-website?style=for-the-badge
[license-url]: https://github.com/TobiAdeniyi/django-portfolio-website/blob/main/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/tobiloba-adeniyi/
[website-screenshot]: images/projects/django_portfolio_website.png
[website-url]: https://git.heroku.com/tobi-django-portfolio-website.git
