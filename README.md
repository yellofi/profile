# Yunseob Hwang — Profile

Personal profile and selected technical seminars, separate from the Tech Archive.

## Content

- About / Experience / Selected Work: based on `yellofi/tech-archive/docs/profile.md` as read on 2026-10-12.
- Insights: selected seminar titles and year-month dates transcribed from the supplied file-list screenshot.
- Achievements: publication, patent and recognition summaries from the same profile source. Counts retain the source wording; registered/filed totals should not be added without confirming overlap.
- TabPFN is marked scheduled for 2026-10-15.

## Connect slides

The current page is a showcase shell. No PDFs are included. Rows intentionally show “Slides pending” rather than dead View links.

For each seminar, upload its public version and replace the title's div with an anchor to its viewer page; replace the status span with a View link to the same page. Keep `data-seminar` on the row so search continues to work.

Prefer page images in a custom viewer if the original PDF should not be hosted. A browser PDF viewer cannot enforce download prevention. Do not imply download protection from hidden toolbar buttons.

## Run

This is a buildless static HTML page, using relative links for future local assets. Open index.html or serve the repository with `python -m http.server 8000`.

Default language is Korean; existing English toggle is retained. Selected Work and achievement details currently retain the Korean source text in both language modes. Seminar titles and topics are English.

## Validation

10 seminar rows; unique element IDs; internal navigation targets; JavaScript syntax checked. Browser visual QA was unavailable in this environment.
