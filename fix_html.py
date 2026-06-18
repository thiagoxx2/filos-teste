with open("js/related-courses.js", "r", encoding="utf-8") as f:
    js = f.read()

# Replace:
#           <div class="courses-paginated" id="related-courses-paginated">
#              ${pagesHtml}
#           </div>
#           
#           ${arrowsHtml}
# With:
#           <div class="courses-paginated" id="related-courses-paginated" style="position: relative;">
#              ${pagesHtml}
#              ${arrowsHtml}
#           </div>

js = js.replace(
    '<div class="courses-paginated" id="related-courses-paginated">\n             ${pagesHtml}\n          </div>\n          \n          ${arrowsHtml}',
    '<div class="courses-paginated" id="related-courses-paginated">\n             ${pagesHtml}\n             ${arrowsHtml}\n          </div>'
)

with open("js/related-courses.js", "w", encoding="utf-8") as f:
    f.write(js)
