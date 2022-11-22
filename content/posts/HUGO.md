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
- Hugo is a Static Site Generator.
- Dynamic Website requires database(DB), Php, and JavaScript(JS).
- Static Website requires HTML & CSS into JavaScript(JS).
- The steps will be followed as below.

## INSTALL
- Use `brew install hugo` command to install hugo in your computer. 
  - You can find the lates release [here](https://github.com/gohugoio/hugo/releases).
  - `sudo dpkg -i hugo_0.104.3_linux-amd64.deb` lets you to install related hugo version. 

**NOTE:** If you don't have homebrew on your system, follow the steps explained in the [link](https://www.how2shout.com/linux/how-to-install-brew-ubuntu-20-04-lts-linux/).
  
- Use `hugo new site "site-name" -f yml` command to create a new site.
  - `-f yml` is obtional and just to change default settings.

### THEME
- It is the folder that contains all of your themes.
- Every theme has its own features to design website. 
- You can use [Hugo Themes](https://themes.gohugo.io) to download a theme.
- After you choose one of the themes, you can follow the steps being explained in every items to download the theme [Ex: PaperMod Theme](https://github.com/adityatelange/hugo-PaperMod/wiki/Installation).

- Open the project
  - `code .` opens your recent folder in VSCode.

- Go to `config.yml` file
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

- `hugo mod get -u` updates your theme with newest version.

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
  - `touch .gitmodules` allows you to create '.gitmodules' file in the same folder because it is needed to add `themes/'chosenThemeName'` as a submodule which will make it easier to update once we have all of these files in github.
  - Edit the content of `.gitmodules` file as follows
    ```
    [submodule "themes/"chosenThemeName"]
    path = themes/"chosenThemeName"
    url = "https://github.com/adityatelange/hugo-PaperMod.git"
    ```
  - Commit and publish your project on github.
  - Then go to the `netlify.com` and connect with your github account.
  - Click `New site from Git` and choose `GitHub`.
  - Then choose the repository you want to build your site on it.
  - Set a `Build command` according to your project name (as preferred) and `Publish directory` as `public` in `Basic build settings`.
  - Set `New variable` as follows:
    - `Key` --> HUGO_VERSION
    - `Value` --> the result of `hugo version` command on your computer (**Ex:**`0.104.3`).
  - Click on `Deploy site`.
  - After deploying process is done, copy your website link and past into the `baseURL` part in the `config.yml` file (**Ex:**`baseURL: "https://osmankayi.netlify.app"`).
  - After every change, the files must be submitted to the github and netlify will be doing rest of the work by itself to see the newest version of the project.

**NOTE:** If you want to exercise with some big data and see how fast Hugo is, you can use [generate-articles.py](https://gist.github.com/jaden/1ce5a7192d8ee8e4c112#file-generate-articles-py) file.

## HOW TO CHANGE THEME
- Download [go](https://www.cyberciti.biz/faq/how-to-install-gol-ang-on-ubuntu-linux/). If you want to check whether you have `go` or not, you can use `go version` command.
- Initialise modules for your website:  
  - If you're managing your project on GitHub
  `hugo mod init github.com/<username>/<repo-name>`
  - If you're managing your project locally
  `hugo mod init my-project`
- Create `config/_default/module.toml` to add the theme into your configuration and add the following:
```
  [[imports]]
path = "github.com/nunocoracao/blowfish/v2"
```
- `hugo server` starts your server and automatically downloads the theme.

## BUILD STATIC PAGES
- `hugo -D` command lets you to build static pages under `./public/` by default (`-d/--destination` flag to change it, or set `publishdir``in the config file).