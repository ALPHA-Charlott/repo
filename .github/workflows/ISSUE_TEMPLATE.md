---
title: "RELEASE {{env.GH_REL}} {{date | date('dddd, MMMM Do YYYY, h:mm:ss a') }}"
labels:  new-release
---
Oh no! A new release just arrives: {{ payload.sender.login }}.
checkout out the release page {{env.GH_REL_URL}}
