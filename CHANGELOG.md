# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-websecurityscanner/#history

## [0.4.0](https://www.github.com/googleapis/python-websecurityscanner/compare/v0.3.0...v0.4.0) (2020-01-30)


### Features

* **websecurityscanner:** add finding types; add vulnerable headers; update docstrings (via synth) ([#9380](https://www.github.com/googleapis/python-websecurityscanner/issues/9380)) ([34f192e](https://www.github.com/googleapis/python-websecurityscanner/commit/34f192eb890945636cab82e1a0fef9c33d7c8eb3))

## 0.3.0

07-24-2019 17:56 PDT


### Implementation Changes
- Allow kwargs to be passed to create_channel (via synth). ([#8413](https://github.com/googleapis/google-cloud-python/pull/8413))
- Retry code 'idempotent' for ListCrawledUrls, add empty lines (via synth). ([#8079](https://github.com/googleapis/google-cloud-python/pull/8079))

### New Features
- Add 'client_options' support, update list method docstrings (via synth). ([#8531](https://github.com/googleapis/google-cloud-python/pull/8531))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))

### Documentation
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Add compatibility check badges to READMEs. ([#8288](https://github.com/googleapis/google-cloud-python/pull/8288))

### Internal / Testing Changes
- Pin black version (via synth). ([#8603](https://github.com/googleapis/google-cloud-python/pull/8603))
- Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))
- Declare encoding as utf-8 in pb2 files (via synth).  ([#8373](https://github.com/googleapis/google-cloud-python/pull/8373))
- Add disclaimer to auto-generated template files. ([#8337](https://github.com/googleapis/google-cloud-python/pull/8337))
- Suppress checking 'cov-fail-under' in nox default session (via synth). ([#8258](https://github.com/googleapis/google-cloud-python/pull/8258))
- Fix coverage in 'types.py' (via synth). ([#8172](https://github.com/googleapis/google-cloud-python/pull/8172))

## 0.2.0

05-15-2019 15:20 PDT


### Implementation Changes
- Add routing header to method metadata (via synth).  ([#7605](https://github.com/googleapis/google-cloud-python/pull/7605))
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))
- Protoc-generated serialization update. ([#7101](https://github.com/googleapis/google-cloud-python/pull/7101))
- GAPIC generation fixes. ([#7059](https://github.com/googleapis/google-cloud-python/pull/7059))
- Pick up order-of-enum fix from GAPIC generator. ([#6882](https://github.com/googleapis/google-cloud-python/pull/6882))

### New Features
- Generate v1beta. ([#7992](https://github.com/googleapis/google-cloud-python/pull/7992))

### Documentation
- Updated client library documentation URLs. ([#7307](https://github.com/googleapis/google-cloud-python/pull/7307))
- Update copyright headers

### Internal / Testing Changes
- Update noxfile (via synth). ([#7803](https://github.com/googleapis/google-cloud-python/pull/7803))
- Fix 'docs' session in nox. ([#7788](https://github.com/googleapis/google-cloud-python/pull/7788))
- Add nox session 'docs' (via synth). ([#7747](https://github.com/googleapis/google-cloud-python/pull/7747))
- Copy lintified proto files (via synth). ([#7474](https://github.com/googleapis/google-cloud-python/pull/7474))
- Add clarifying comment to blacken nox target. ([#7409](https://github.com/googleapis/google-cloud-python/pull/7409))
- Add protos as an artifact to library ([#7205](https://github.com/googleapis/google-cloud-python/pull/7205))

## 0.1.1

12-18-2018 10:45 PST


### Implementation Changes
- Import `iam.policy` from `google.api_core`. ([#6741](https://github.com/googleapis/google-cloud-python/pull/6741))
- Avoid overwriting `__module__` of messages from shared modules. ([#5364](https://github.com/googleapis/google-cloud-python/pull/5364))

### Dependencies
- Bump minimum `api_core` version for all GAPIC libs to 1.4.1. ([#6391](https://github.com/googleapis/google-cloud-python/pull/6391))

### Documentation
- Document Python 2 deprecation ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))
- Normalize use of support level badges ([#6159](https://github.com/googleapis/google-cloud-python/pull/6159))
- Replace links to `/stable/` with `/latest/`. ([#5901](https://github.com/googleapis/google-cloud-python/pull/5901))

### Internal / Testing Changes
- Blacken all gen'd libs ([#6792](https://github.com/googleapis/google-cloud-python/pull/6792))
- Omit local deps ([#6701](https://github.com/googleapis/google-cloud-python/pull/6701))
- Run black at end of synth.py ([#6698](https://github.com/googleapis/google-cloud-python/pull/6698))
- Run Black on Generated libraries ([#6666](https://github.com/googleapis/google-cloud-python/pull/6666))
- Add templates for flake8, coveragerc, noxfile, and black. ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))
- Add / fix badges for PyPI / versions. ([#6158](https://github.com/googleapis/google-cloud-python/pull/6158))
- Use new Nox ([#6175](https://github.com/googleapis/google-cloud-python/pull/6175))
- Add 'synth.py'. ([#6087](https://github.com/googleapis/google-cloud-python/pull/6087))
- Use inplace nox installs ([#5865](https://github.com/googleapis/google-cloud-python/pull/5865))
- Add Test runs for Python 3.7 and remove 3.4 ([#5295](https://github.com/googleapis/google-cloud-python/pull/5295))
- Add dot files for websecurityscanner ([#5286](https://github.com/googleapis/google-cloud-python/pull/5286))

## 0.1.0

### New Features
- Add v1alpha1 websecurityscanner endpoint
