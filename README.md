<div align="center">
  <img src="frontend/public/logo.png" alt="Citizens Advice" width="100" height="100" />
  <h1>Citizens Advice SORT</h1>
  <h3>Junior Developer Practical</h3>
</div>

A small full-stack app: a **FastAPI** backend (Python) and a **Next.js** frontend (TypeScript).

The app shows answers to advisers' questions, along with the sources each answer is based on. Your job is to finish it. [TASK.md](TASK.md) explains what to build.

## Project structure

```
junior-developer/
├── backend/                 FastAPI app (Python, managed with uv)
│   ├── app/                 The API, including GET /data
│   └── data/mock.json       The questions, answers and sources
├── frontend/                Next.js app (TypeScript, Tailwind)
│   ├── app/page.tsx         The home page
│   └── components/          Content.tsx shows one item from the data
├── Makefile                 Shortcut commands (install, dev)
├── SETUP.md                 How to install the tools and get the app running
└── TASK.md                  What to build
```

## The task

[TASK.md](TASK.md) has the full instructions.

**Backend.** In the backend, you need to:

1. Work out which sources each answer cites, and replace each `<ref>` with a link.
2. Get a favicon for each source's website.
3. Redact the client's name, email and phone number from each question.

**Frontend.** In `Content.tsx`, show each item:

1. The redacted question.
2. The answer, with working citation links.
3. Every source, cited and not cited, with its favicon.


## The solution

**Backend**
For the backend functionality, I added sources with the link, a favicon for each link and  redacted the names, emails and phone numbers. 

With the link I replaced the ref tag with a href tag with the source link and the source name as the text to display for the link.

For the favicon I used a computed field and propery value to add the favicon url to the class object of source to use it in the content.tsx file.

I used regex for the phone numbers I checked all sets of numbers in 3 or less chunks. For the email I just replaced all words with the @ character in the list. This could be made more robust as there are a few edge cases where someone mistypes a @ symbol so maybe a regex to check for a .com or something similar maybe be better.

For the redacting of the names I hardcoded all the names into a list, so the question can check for names to redact this information going from full names first then to first and second. However I would have liked to not hardcode this information as in a real world application this creates a lot of effort, but maybe this information maybe stored in a database given peoples login or using the context to see if its a name.

**Frontend.**

Retrieved all needed information from the backend such as links, favicons and the redacted information.

Looped through each source to add its link and favicon. Added the links in bold and italic so it would stand out. Also added converted the href given in a string to actual html tag using `dangerouslySetInnerHTML={{ __html: content }}` to render the string of the href link.

Changed the css colour to a lighter colour so the favicons will show for the citizens advice website link.


## Getting set up

Follow [SETUP.md](SETUP.md) to install the tools you need and get the app running. The first run downloads the redaction model, [fastino/GLiNER2-Guardrails-PII-Multi](https://huggingface.co/fastino/GLiNER2-Guardrails-PII-Multi) (about 1.2 GB).

```bash
make install
make dev
```

| What | URL |
|---|---|
| Backend | http://localhost:8000 |
| API docs | http://localhost:8000/docs |
| Frontend | http://localhost:3000 |

> If you have any problems or are unsure about any of the steps please email technology@casort.org
