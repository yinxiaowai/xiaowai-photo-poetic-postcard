# Contributing

Thank you for improving Photo Poetic Postcard.

## Good contributions

- platform-specific installation corrections backed by official documentation;
- model-neutral prompt improvements that preserve the core invariants;
- accessibility, translation, and typography improvements;
- improvements to packaging and validation tools;
- authorized examples with clear source and permission notes.

## Before opening a pull request

1. Keep the public workflow at one input photo → one final image.
2. Do not hard-code a commercial image vendor as the only supported model.
3. Do not weaken source-photo fidelity or allow a full-scene repaint below.
4. Do not add an example unless you own it or have documented permission to publish it.
5. Run:

   ```bash
   python tools/validate_repo.py
   python tools/build_packages.py
   ```

6. Explain the host, image capability, test photo rights, and observed result.

By contributing text, you agree that it may be distributed under CC BY-NC-SA 4.0. By contributing code under `tools/`, you agree that it may be distributed under MIT. Do not contribute material you cannot license on those terms.

## Publishing standalone MD updates

Follow [Standalone MD versions](docs/PROMPT_VERSIONS.md). Update public versioned entry links together with `VERSION`; validation rejects stale or development-only entries. Releases include exact tagged Chinese/English MD files and a version/hash manifest. Keep existing tags and assets immutable, and verify latest-download targets after publication.
