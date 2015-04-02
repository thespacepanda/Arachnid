# Overview

Arachnid is both a general web spider and a reddit bot. It consumes links from subreddits specified in a config file (config.py), and goes N links deep on those pages (specified in the same config.py) looking for pdf files. When it finds a link to a pdf file it downloads it to its working directory.

# Architechture

Arachnid is divided into several constituent parts, namely:
- the ContentConsumer, which recursively gathers URLs from a single page (each link out is treated as the root of a new tree, decrementing N; once N reaches 0 no new links are followed), and reduces them to a flat list of URLs
- the TargetFilter, which removes all URLs which are not pdf files
- and the TargetConsumer, which queues the target URLs for download in the background
