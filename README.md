# Critical Data Website

This is the source code for the Critical Data website.
The website uses [Hugo](https://gohugo.io/), a static website engine, with the [Universal theme](http://themes.gohugo.io/hugo-universal-theme/).

# Building the website locally

Hugo makes it fairly easy to prototype the website locally. The steps are:

1. [Install Hugo](https://gohugo.io/#action)
2. Clone this repository recursively: `git clone --recursive git@github.com:MIT-LCP/critical-data.git`
3. Serve the website locally by running the following command in the root folder of this repository: `hugo serve`. More information on how Hugo works can be found [here](https://gohugo.io/overview/introduction/).

# Deployment

The website is hosted on webserver. Add webserver as a remote and use git push to deploy the website.
