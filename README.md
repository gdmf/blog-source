This repository contains everything needed to generate my [blog](http://gdmf.github.com). It uses [Pelican](http://docs.getpelican.com/en/latest/), a static site generator written in Python.

The blog content is pushed to my Github Pages using [ghp-import](https://github.com/davisp/ghp-import) (install using [pip](https://pip.pypa.io/en/stable/)).

Changes to the blog are pushed to this 'blog-source' repo. If performed correctly, the following incantations will publish the contents of the output folder to gdmf.github.io. If not invoked correctly, doom will inevitably befall the user.

```bash
pelican content -o output -s publishconf.py
ghp-import output
git push git@github.com:gdmf/gdmf.github.io.git gh-pages:master
```


