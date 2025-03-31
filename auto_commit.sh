#!/bin/bash
git add .
git commit -m "💸 Auto Log: $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main
