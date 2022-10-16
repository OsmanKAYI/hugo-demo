---
title: "HUGO"
date: 2022-10-16T13:54:41+03:00
draft: false
cover:
      image: img/Hugo.png 
      alt: "This is a post image"
      caption: "This is a caption"
tags: ["html", "css"]
categories: ["tech"]
---
- Hugo is a Static Site Generator
- Dynamic Websites -- DB-Php-JS
- Static Websites -- HTML-CSS into JS
- The steps will be followed as below.

## INSTALL
- `brew install hugo`

  ```
  NOTE: If you don't have homebrew on your system, follow the steps explained in the link below.

    - https://www.how2shout.com/linux/how-to-install-brew-ubuntu-20-04-lts-linux/
  ```
- `hugo new site "site-name" -f yml`
  - `-f yml` is obtional and just to change default settings.

### THEME
- It is the folder that contains all of your themes.
- Every theme its own features to design website. 
- You can use [Hugo Themes](https://themes.gohugo.io) to download a theme.
- After you choose one of the themes, you can follow the steps being explained in every items to download the theme [Ex: PaperMod Theme](https://github.com/adityatelange/hugo-PaperMod/wiki/Installation).

- Open the project
  - `code .` opens your recent folder in VSCode.

- Go to 'config.yml' file
  - Place the theme in your project
    ```
    baseURL: http://example.org/
    languageCode: en-us
    title: Demo for Hugo
    theme: `PaperMod`
    ```
- To open up the server: `localhost:1313`
  - `hugo server`

- When you want to change the html or css structure of your theme, to not to be effected by the updating the theme, you can copy the contents of theme's html or css file under the layouts folder with the same folder structure and name.

### CONTENT
- It is the place where all of your actual content (artical, pages, and etc.) will be posted.
- `hugo new posts/"fileName".md` is to create a post (markDown file) inside of a posts folder.

### LAYOUTS
- It is usually for themes overwrite.
- Actually themes come with its own layouts folder which holds all the html files.

### STATIC
- It is for all the static assets like images.
- To add an image on your page
  - Be sure that the image you will use is under the 'static' folder.
  - Make the head of your post like below:
    ```
    title: "HUGO"
    date: 2022-10-16T13:54:41+03:00
    draft: false
    cover:
      image: 
      alt: "This is a post image"
      caption: "This is a caption"
    ```

## PUBLISH YOUR HUGO WEBSITE WITH `netlify`
- `hugo` command lets you to build your site. It is going to create 'public' folder with all of your html, css, image, assets, and etc.
- This public folder is deleted and the following steps are done:
  - `git init` allows you to create a github repository in your folder.
  - `touch .gitmodules` allows you to create '.gitmodules' file in the same folder because it is needed to add "themes/'chosenThemeName'" as a submodule which will make it easier to update once we have all of these files in github.