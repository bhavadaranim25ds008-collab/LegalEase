# 1. Brainstorming & Ideation — LegalEase

## Team
| # | Name | Email |
|---|------|-------|
| 1 | Bhavadarani M. | bhava.darani.m.25ds008@gmail.com |
| 2 | Akila P | akila.p.25ds002@gmail.com |
| 3 | Devi Sri B | devi.sri.b25ds010@gmail.com |
| 4 | Meenatchi M | meenatchi.m.25ds023@gmail.com |

## Problem Statement
Drafting a legal document (agreement, contract, NDA) from scratch is slow and confusing for people without legal training. They often start from unsuitable templates or pay for simple drafts.

## Idea
A simple web app where the user enters only **four things** — document type, parties, terms & conditions, and effective date — and an AI model produces a structured legal document with numbered sections and standard clauses.

## Objective
Build a simple and useful AI-assisted system that helps users generate structured legal documents from the information they provide.

## Ideas Considered
| Idea | Decision |
|------|----------|
| Fixed template library with fill-in fields | Rejected — not flexible for different document types |
| Chatbot that asks questions step by step | Rejected — slower for the user |
| **Single form → Gemini generates the full document** | **Selected** — fastest, only four inputs |
| Export options (TXT / DOCX / PDF) | Selected — documents must be usable outside the app |
| Preview + inline editing before download | Selected — AI output should be reviewable by the user |

## Target Users
Students, freelancers, small business owners and anyone who needs a first draft of a common legal document quickly.

## Expected Outcome
An AI-generated legal document based on the user's input, shown in the interface, editable, and downloadable as TXT, DOCX or PDF.

> **Note:** LegalEase generates draft documents for convenience. Output should be reviewed by a qualified legal professional before use.
