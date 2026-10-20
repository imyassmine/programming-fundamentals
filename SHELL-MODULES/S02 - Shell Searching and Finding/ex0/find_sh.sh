#!/bin/sh
find . -name "*.sh" | sed 's/.*\///;s/\.sh$//'
